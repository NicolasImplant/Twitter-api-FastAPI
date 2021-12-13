# Pydantic
from pydantic import BaseModel, EmailStr, Field

# FastAPI
from fastapi import FastAPI, status

# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List



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
 
class UserRegister(UserBase):
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

# Path Operations

## Users

### Resgister a user
@app.post(
    path= '/signup',
    response_model= User,
    status_code=status.HTTP_201_CREATED,
    summary= 'Register a User',
    tags=['Users'])

def signup():
    '''
    Signup a user

    This path operation reguister a usser in app

    Parameters:
        - **Request body parameter**
            -   User: UserRegister
    
    Returns a JSON with the basic user information
        - user:id : UUID
        - email   : String
        - last_name : String
        - frist_name: String
        - Brith_date: datetime
    '''



    pass

### LogIn a user
@app.post(
    path= '/login',
    response_model= User,
    status_code= status.HTTP_200_OK,
    summary= 'LogIn a User',
    tags=['Users']
)

def login():
    pass

### Show all users
@app.get(
    path='/users',
    response_model= List[User],
    status_code= status.HTTP_200_OK,
    summary= 'Show all users',
    tags= ['Users']
)

def show_all_users():
    pass

### Show one user
@app.get(
    path= '/users/{user_id}',
    response_model= User,
    status_code= status.HTTP_200_OK,
    summary= 'Show a user',
    tags=['Users']
)

def show_a_user():
    pass

### Delete a user
@app.delete(
    path='/users/{user_id}/delete',
    response_model= User,
    status_code= status.HTTP_200_OK,
    summary= 'Delete a user',
    tags= ['Users']
)

def delete_a_user():
    pass

### Update a user
@app.put(
    path= '/users/{user_id}/update',
    response_model= User,
    status_code= status.HTTP_200_OK,
    summary= 'Update a user',
    tags= ['Users']
)

def update_a_user():
    pass

## Tweets

### Show all tweets
@app.get(
    path='/',
    response_model= List[Tweet],
    status_code= status.HTTP_200_OK,
    summary= 'Show all tweets',
    tags=['Tweets']
    )

def home():
    return {'Twitter API': 'Working!'}

### Post a tweet
@app.post(
    path='/post',
    response_model= Tweet,
    status_code= status.HTTP_201_CREATED,
    summary= 'Post a tweet',
    tags= ['Tweets']
    )

def post():
    pass

### Show a tweet

@app.get(
    path='/tweets/{tweet_id}',
    response_model= Tweet,
    status_code= status.HTTP_200_OK,
    summary= 'Show a tweet',
    tags=['Tweets'])

def show_a_tweet():
    pass

### Delete a tweet

@app.delete(
    path= '/tweets/{tweet_id}/delete',
    response_model= Tweet,
    status_code= status.HTTP_200_OK,
    summary= 'Delete a tweet',
    tags=['Tweets'])

def delete_a_tweet():
    pass

### Update a tweet
#### Especial function not in original version of twiter

@app.put(
    path= '/tweets/{tweet_id}/update',
    response_model= Tweet,
    status_code= status.HTTP_200_OK,
    summary= 'Update a tweet',
    tags=['Tweets'])

def update_a_tweet():
    pass