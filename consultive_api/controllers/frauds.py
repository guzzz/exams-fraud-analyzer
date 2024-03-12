
from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from structlog import get_logger

from consultive_api.schemas.evidences import Evidences
from consultive_api.schemas.frauds import FraudWithDetails, FraudsWithDetails
from consultive_api.config.database import get_db
from consultive_api.repositories.frauds import FraudRepository
from consultive_api.repositories.evidences import EvidenceRepository

router = APIRouter()
repo = FraudRepository()
ev_repo = EvidenceRepository()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
log = get_logger()


@router.get("/frauds", status_code=status.HTTP_200_OK, response_model=list[FraudsWithDetails])
def frauds(
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Session = Depends(get_db),
        page: Optional[int] = Header(1), 
        limit: Optional[int] = Header(10)
    ):
    log.info("[Fraud Controller] Listing Frauds...")
    return repo.list(db, page, limit, None)

@router.get("/frauds/{id}", status_code=status.HTTP_200_OK, response_model=FraudWithDetails)
def fraud(token: Annotated[str, Depends(oauth2_scheme)], id: int, db: Session = Depends(get_db)):
    log.info("[Fraud Controller] Retrieving Fraud...")
    response = repo.retrieve(db, id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fraud not found")
    return response

@router.get("/frauds/{id}/evidences", status_code=status.HTTP_200_OK, response_model=Evidences)
def fraud(token: Annotated[str, Depends(oauth2_scheme)], id: int, db: Session = Depends(get_db)):
    log.info("[Fraud Controller] Listing Fraud Evidences...")
    bp_items = ev_repo.blood_pressure_list(db, id)
    hr_items = ev_repo.heart_rate_list(db, id)
    if not bp_items or not hr_items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fraud not found")
    return Evidences(blood_pressure_evidences=bp_items, heart_rate_evidences=hr_items)
