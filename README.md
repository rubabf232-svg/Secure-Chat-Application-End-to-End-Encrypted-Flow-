# Secure-Chat-Application-End-to-End-Encrypted-Flow-
🔐 Secure real-time chat application built with Python, FastAPI, WebSockets, JWT authentication, password hashing, and end-to-end encryption architecture.
# 🔐 Secure Chat — End-to-End Encrypted Messaging Application

A privacy-focused real-time chat application built with **Python, FastAPI, WebSockets, JWT authentication, password hashing, and public-key cryptography**.

The project demonstrates how secure messaging systems can be designed around encrypted message handling and client-side cryptographic concepts.

---

## 🚀 Features

* 🔐 End-to-End Encryption Architecture
* 🔑 Public-Key Cryptography
* 👤 User Registration & Login
* 🔒 Secure Password Hashing
* 🎫 JWT-Based Authentication
* 💬 Real-Time WebSocket Messaging
* 🗄️ SQLite Database
* 🛡️ Secure Message Handling
* 📊 Security-Focused Architecture
* 🧪 Cryptography Unit Tests
* 📄 JSON/API-based communication

---

## 🛠️ Technologies

* **Python 3**
* **FastAPI**
* **WebSockets**
* **SQLite**
* **Cryptography**
* **PyJWT**
* **Passlib**
* **HTML5**
* **CSS3**
* **JavaScript**

---

## 📁 Project Structure

```text
secure-chat-e2e/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── auth.py
│   ├── crypto.py
│   └── websocket_manager.py
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── tests/
│   └── test_crypto.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rubabf232-svg/secure-chat-e2e.git
cd secure-chat-e2e
```

### 2. Create Virtual Environment

#### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

---

## 🔑 Environment Configuration

Create a `.env` file in the project root:

```env
JWT_SECRET=replace-with-a-long-random-secret
```

**Never upload `.env` to GitHub.**

The `.gitignore` file already excludes it from version control.

---

## ▶️ Run the Application

Start the FastAPI server:

```powershell
python -m uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Open the address in your browser.

---

## 💬 How It Works

The application uses **WebSockets** for real-time communication.

Basic architecture:

```text
        User A
          │
          │
          ▼
   Encrypt Message
          │
          ▼
   Encrypted Data
          │
          ▼
    FastAPI Server
          │
          │
          ▼
   Encrypted Data
          │
          ▼
        User B
          │
          ▼
   Decrypt Message
```

The goal of the architecture is to keep the server focused on authentication and message transport rather than requiring access to plaintext messages.

---

## 🔐 Cryptography

The project uses the Python `cryptography` library for public-key cryptographic operations.

The cryptographic module demonstrates:

* RSA key-pair generation
* Public-key encryption
* Private-key decryption
* OAEP padding
* SHA-256

Example flow:

```text
Public Key
    ↓
Encrypt Message
    ↓
Ciphertext
    ↓
Private Key
    ↓
Decrypt Message
    ↓
Original Message
```

---

## 🔒 Authentication

User authentication includes:

* Password hashing
* Password verification
* JWT token generation
* JWT token validation

Passwords are never intended to be stored as plaintext.

---

## 🧪 Testing

Run the cryptography test:

```powershell
pytest
```

The test verifies that an encrypted message can be successfully decrypted using the corresponding private key.

---

## 🛡️ Security Considerations

This project is designed for **educational and portfolio purposes**.

A production-grade secure messenger requires additional security controls, including:

* Audited end-to-end encryption protocols
* Strong client-side key management
* Forward secrecy
* Key verification
* Secure private-key storage
* TLS/HTTPS and WSS
* Replay protection
* Rate limiting
* Session management
* Secure file transfer
* Security auditing

For production messaging systems, established and independently reviewed protocols should be preferred over designing a custom cryptographic protocol.

---

## 🚧 Future Improvements

Planned improvements include:

* [ ] Complete client-side E2E encryption
* [ ] Automatic key-pair generation
* [ ] Secure private-key storage
* [ ] Forward secrecy
* [ ] User identity/key verification
* [ ] Encrypted file sharing
* [ ] Online/offline status
* [ ] Message delivery status
* [ ] Message timestamps
* [ ] HTTPS/WSS deployment
* [ ] Rate limiting
* [ ] Responsive mobile UI
* [ ] Docker support
* [ ] Production security hardening

---

## 🎯 Use Cases

This project can be used as a learning platform for:

* Cybersecurity
* Secure application development
* Cryptography
* WebSocket communication
* API security
* Authentication
* Privacy-focused application design

---

## ⚠️ Disclaimer

This project is provided for **educational and authorized security research purposes**.

It has not been independently security audited and should not be used as a production replacement for established secure messaging applications.

---

## 👩‍💻 Author

**Fatima Hussain**

Python • Cybersecurity • Problem Solving • Continuous Learning

---

## 📜 License

This project is licensed under the **MIT License**.

