
from typing import Annotated, Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from structlog import get_logger

from consultive_api.repositories.frauds import FraudRepository
from consultive_api.config.database import get_db
from consultive_api.repositories.persons import PersonRepository
from consultive_api.schemas.frauds import FraudsByPerson
from consultive_api.schemas.persons import Person

router = APIRouter()
person_repo = PersonRepository()
fraud_repo = FraudRepository()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
log = get_logger()


@router.get("/persons", status_code=status.HTTP_200_OK, response_model=list[Person])
def persons(
        token: Annotated[str, Depends(oauth2_scheme)], 
        db: Session = Depends(get_db), 
        page: Optional[int] = Header(1), 
        limit: Optional[int] = Header(10)
    ):
    log.info("[Person Controller] Listing Persons...")
    return person_repo.list(db, page, limit)

@router.get("/persons/{id}", status_code=status.HTTP_200_OK, response_model=Person)
def person(token: Annotated[str, Depends(oauth2_scheme)], id: int, db: Session = Depends(get_db)):
    log.info("[Person Controller] Retrieving Person...")
    response = person_repo.retrieve(db, id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    return response


@router.get("/persons/{id}/frauds", status_code=status.HTTP_200_OK, response_model=list[FraudsByPerson])
def person_frauds(
        token: Annotated[str, Depends(oauth2_scheme)], 
        id: int,
        db: Session = Depends(get_db), 
        page: Optional[int] = Header(1), 
        limit: Optional[int] = Header(10)
    ): 
    log.info("[Person Controller] Listing Person Frauds...")
    response = fraud_repo.list(db, page, limit, id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There are no records registered")
    return response
