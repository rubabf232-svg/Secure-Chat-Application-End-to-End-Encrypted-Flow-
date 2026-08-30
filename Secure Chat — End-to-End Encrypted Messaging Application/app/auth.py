import os
import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set up password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Environment variables and cryptographic constants
SECRET_KEY = os.getenv("JWT_SECRET", "change-this-secret-in-production")
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    """Hashes a plain-text password using bcrypt."""
    return pwd_context.hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    """Verifies a plain-text password against a stored hash."""
    return pwd_context.verify(password, password_hash)

def create_token(username: str) -> str:
    """Generates a JWT token containing the username."""
    payload = {"sub": username}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    """Decodes a JWT token and returns the username, or None if invalid."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except (jwt.InvalidTokenError, jwt.DecodeError):
        return None
