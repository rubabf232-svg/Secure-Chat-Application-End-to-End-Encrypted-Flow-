from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    password: str = Field(min_length=8)
    public_key: str


class LoginRequest(BaseModel):
    username: str
    password: str


class MessageRequest(BaseModel):
    receiver: str
    encrypted_message: str