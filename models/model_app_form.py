from pydantic import BaseModel, EmailStr


class ApplicationForm(BaseModel):
    email: EmailStr = None
    username: str = None
    phone: str = None
    comments: str = None
    referer: str = None
    formid: str = None
    sent: str = None 
    requestid: str = None
