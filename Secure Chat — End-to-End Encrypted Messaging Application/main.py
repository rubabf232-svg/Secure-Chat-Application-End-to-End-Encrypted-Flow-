from fastapi import (
    FastAPI,
    HTTPException,
    WebSocket,
    WebSocketDisconnect
)

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .database import (
    get_connection,
    init_db
)

from .models import (
    RegisterRequest,
    LoginRequest,
    MessageRequest
)

from .auth import (
    hash_password,
    verify_password,
    create_token
)

from .websocket_manager import ConnectionManager


app = FastAPI(
    title="Secure Chat E2E",
    description="End-to-End Encrypted Chat Application",
    version="1.0.0"
)

manager = ConnectionManager()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


@app.on_event("startup")
def startup():

    init_db()


@app.get("/")
def home():

    return FileResponse(
        "static/index.html"
    )


@app.post("/register")
def register(data: RegisterRequest):

    connection = get_connection()

    existing = connection.execute(
        "SELECT id FROM users WHERE username = ?",
        (data.username,)
    ).fetchone()

    if existing:
        connection.close()

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    password_hash = hash_password(
        data.password
    )

    connection.execute(
        """
        INSERT INTO users
        (username, password_hash, public_key)
        VALUES (?, ?, ?)
        """,
        (
            data.username,
            password_hash,
            data.public_key
        )
    )

    connection.commit()
    connection.close()

    return {
        "message": "Registration successful"
    }


@app.post("/login")
def login(data: LoginRequest):

    connection = get_connection()

    user = connection.execute(
        """
        SELECT username, password_hash
        FROM users
        WHERE username = ?
        """,
        (data.username,)
    ).fetchone()

    connection.close()

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(
        data.password,
        user["password_hash"]
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_token(
        user["username"]
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@app.get("/users/{username}/public-key")
def get_public_key(username: str):

    connection = get_connection()

    user = connection.execute(
        """
        SELECT public_key
        FROM users
        WHERE username = ?
        """,
        (username,)
    ).fetchone()

    connection.close()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "username": username,
        "public_key": user["public_key"]
    }


@app.post("/messages")
def save_message(data: MessageRequest):

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO messages
        (sender, receiver, encrypted_message)
        VALUES (?, ?, ?)
        """,
        (
            "client",
            data.receiver,
            data.encrypted_message
        )
    )

    connection.commit()
    connection.close()

    return {
        "message": "Encrypted message stored"
    }


@app.websocket("/ws/{username}")
async def websocket_endpoint(
    websocket: WebSocket,
    username: str
):

    await manager.connect(
        username,
        websocket
    )

    try:

        while True:

            data = await websocket.receive_json()

            receiver = data.get("receiver")
            encrypted_message = data.get(
                "encrypted_message"
            )

            if not receiver or not encrypted_message:
                continue

            await manager.send_to_user(
                receiver,
                {
                    "sender": username,
                    "encrypted_message":
                        encrypted_message
                }
            )

    except WebSocketDisconnect:

        manager.disconnect(
            username
        )