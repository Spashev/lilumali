from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from app.database.base import get_db
from app.models.budget import Company, Budget
from app.schemas.budget import CompanyCreate, CompanyWithBudgets

router = APIRouter(tags=["company"])


@router.get("/", response_model=List[CompanyWithBudgets])
def read_budgets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    companies = db.query(Company).offset(skip).limit(limit).all()
    return companies


@router.post("/")
def create_budget(request: CompanyCreate, db: Session = Depends(get_db)):
    new_company = Company(**request.model_dump())

    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    return new_company


@router.delete("/{pk}")
def delete_budget(pk: int, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.id == pk).first()

    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")

    db.delete(company)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{pk}")
def update_budget(request: CompanyCreate, pk: int, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.id == pk).first()

    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")

    for key, value in request.model_dump().items():
        setattr(company, key, value)

    db.commit()
    db.refresh(company)

    return company
