import os

from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import FastAPI, Depends, HTTPException, status

from consultive_api.controllers.frauds import router as fraud_router
from consultive_api.controllers.persons import router as person_router
from consultive_api.schemas.users import User, UserInDB
from consultive_api.config.database import get_db
from consultive_api.repositories.users import UserRepository
from consultive_api.services.security import SecurityService

user_repo = UserRepository()
security_service = SecurityService(os.getenv('SECRET_KEY'))
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="Consultive API")
app.include_router(
    fraud_router,
    prefix="/v0",
    tags=["Frauds and Evidences"]
)
app.include_router(
    person_router,
    prefix="/v0",
    tags=["Persons"]
)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = security_service.decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

@app.get("/health")
def health_check():
    return {"health": "OK!"}

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
                db: Session = Depends(get_db)):
    user_obj = user_repo.retrieve(db, form_data.username)
    if not user_obj:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    user = UserInDB(username=user_obj.username, hashed_password=user_obj.password)
    if not security_service.check_pwd(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": security_service.encode_user(user.username), "token_type": "bearer"}

@app.get("/users/me")
async def who_am_i(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

