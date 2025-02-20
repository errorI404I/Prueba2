from pydantic import BaseModel

class Session(BaseModel):
    access_token: str
    token_type: str

class SessionCreate(BaseModel):
    title: str 