# Pydantic
from pydantic import BaseModel, EmailStr, Field

# FastAPI
from fastapi import FastAPI, status, Body

# Python
import json
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
 
class UserRegister(User):
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

def signup(user: UserRegister = Body(...)):

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
    with open('users.json', 'r+', encoding='utf-8') as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict['user_id'] = str(user_dict['user_id'])
        user_dict['birth_date'] = str(user_dict['birth_date'])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))

    return user

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
    '''
    Show all users

    This path operation show all users in the app

    Parameters:
            -

    Returns a json with all users in the app, with the following keys:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_day: datetime
    '''
    with open('users.json','r', encoding='utf-8') as f:
        results = json.loads(f.read())
    
    return results

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
    '''
    Show all tweets

    This path operation show all tweet in the app

    Parameters:
            -

    Returns a json with all users in the app, with the following keys:
            - tweet_id: UUID
            - Content: str
            - Created_at: datetime 
            - Updated_at: datetime (Optional)
            - By: User 
    '''
    with open('tweets.json','r', encoding='utf-8') as f:
        results = json.loads(f.read())
    
    return results

### Post a tweet
@app.post(
    path='/post',
    response_model= Tweet,
    status_code= status.HTTP_201_CREATED,
    summary= 'Post a tweet',
    tags= ['Tweets']
    )

def post(tweet: Tweet = Body(...)):
    '''
    Post a tweet

    This path operation post a tweet in app

    Parameters:
        - **Request body parameter**
            -   Tweet: Tweet
    
    Returns a JSON with the basic tweet information:
            - tweet_id: UUID
            - Content: str
            - Created_at: datetime 
            - Updated_at: datetime (Optional)
            - By: User 
    '''
    with open('tweets.json', 'r+', encoding='utf-8') as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict['tweet_id'] = str(tweet_dict['tweet_id'])
        tweet_dict['created_at'] = str(tweet_dict['created_at'])
        tweet_dict['updated_at'] = str(tweet_dict['updated_at'])

        tweet_dict['by']['user_id'] = str(tweet_dict['by']['user_id'])
        tweet_dict['by']['birth_date'] = str(tweet_dict['by']['birth_date'])

        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))

    return tweet


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