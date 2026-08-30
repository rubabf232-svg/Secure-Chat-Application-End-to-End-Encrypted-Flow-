let currentUser = null;
let socket = null;


async function register() {

    const username =
        document.getElementById("username").value;

    const password =
        document.getElementById("password").value;


    // Demo public key.
    // In a complete production client,
    // the key pair should be generated locally
    // and the private key must never be sent to
    // the server.

    const publicKey =
        "DEMO_PUBLIC_KEY";


    const response = await fetch(
        "/register",
        {
            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({
                username,
                password,
                public_key: publicKey
            })
        }
    );


    const data = await response.json();

    alert(data.message || data.detail);
}


async function login() {

    const username =
        document.getElementById("username").value;

    const password =
        document.getElementById("password").value;


    const response = await fetch(
        "/login",
        {
            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({
                username,
                password
            })
        }
    );


    const data = await response.json();


    if (!response.ok) {

        alert(data.detail);

        return;
    }


    currentUser = username;

    document.getElementById(
        "currentUser"
    ).textContent = username;

    document.getElementById(
        "auth"
    ).classList.add("hidden");

    document.getElementById(
        "chat"
    ).classList.remove("hidden");


    connectWebSocket();
}


function connectWebSocket() {

    socket = new WebSocket(
        `ws://${window.location.host}/ws/${currentUser}`
    );


    socket.onopen = function () {

        console.log(
            "Secure chat connection established."
        );
    };


    socket.onmessage = function (event) {

        const data = JSON.parse(
            event.data
        );


        addMessage(
            data.sender,
            data.encrypted_message
        );
    };


    socket.onclose = function () {

        console.log(
            "Connection closed."
        );
    };
}


function sendMessage() {

    const receiver =
        document.getElementById(
            "receiver"
        ).value;

    const message =
        document.getElementById(
            "message"
        ).value;


    if (!receiver || !message) {

        alert(
            "Enter receiver and message."
        );

        return;
    }


    /*
        IMPORTANT:

        The real E2E implementation should
        encrypt the plaintext locally using
        the receiver's public key BEFORE this
        WebSocket message is sent.

        This demo UI currently sends the
        provided value as encrypted_message.
    */


    socket.send(
        JSON.stringify({
            receiver: receiver,
            encrypted_message: message
        })
    );


    addMessage(
        "You",
        message
    );


    document.getElementById(
        "message"
    ).value = "";
}


function addMessage(
    sender,
    message
) {

    const container =
        document.getElementById(
            "messages"
        );


    const div =
        document.createElement(
            "div"
        );


    div.className = "message";


    div.textContent =
        `${sender}: ${message}`;


    container.appendChild(div);
}