from pydantic import BaseModel, EmailStr, ValidationError, field_validator


class AuthRegisterDTO(BaseModel):
    email:EmailStr
    password:str
    name:str
    lastname:str
    document:float
 
    @field_validator('password')
    def password_length(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v

    @field_validator('name')
    def name_must_be_alphabetic(cls, v):
        if not v.replace(' ', '').isalpha():
            raise ValueError('Name must only contain alphabetic characters')
        return v

    @field_validator('lastname')
    def lastname_must_be_alphabetic(cls, v):
        if not v.replace(' ', '').isalpha():
            raise ValueError('Lastname must only contain alphabetic characters')
        return v

    @field_validator('document')
    def document_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Document must be a positive number')
        return v

class AuthLoginDTO(BaseModel):
    email:EmailStr
    password:str
    @field_validator('password')
    def password_length(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v