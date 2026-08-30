from app.crypto import (
    generate_key_pair,
    encrypt_message,
    decrypt_message
)


def test_encryption():

    private_key, public_key = (
        generate_key_pair()
    )

    original = "Hello Secure Chat"

    encrypted = encrypt_message(
        original,
        public_key
    )

    decrypted = decrypt_message(
        encrypted,
        private_key
    )

    assert decrypted == original