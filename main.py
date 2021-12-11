# Pydantic
from pydantic import BaseModel, EmailStr, Field

# FastAPI
from fastapi import FastAPI

# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional


app = FastAPI()

# Models

class UserBase(BaseModel):
    
    user_id: UUID = Field(...)

    email: EmailStr = Field(...)

class User(UserBase):

    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

    birth_date: Optional[date] = Field(default=None)
    
class UserLogin(UserBase):

        password: str = Field(
        ...,
        min_length=8,
        max_length=64
        )


class Tweet(BaseModel):
    
    tweet_id: UUID = Field(...)

    content: str = Field(
        ...,
        min_length=1,
        max_length=240
    )

    created_at: datetime = Field(default=datetime.now())

    updated_at: Optional[datetime] = Field(default=None)

    by: User = Field(...) 

@app.get(path='/')
def home():
    return {'Twitter API': 'Working!'}