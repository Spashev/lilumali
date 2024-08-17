from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from app.database.base import get_db
from app.models.budget import Budget, Company
from app.schemas.budget import BudgetCreate, Budget as BaseBudget

router = APIRouter(tags=["budget"])


@router.get("/", response_model=List[BaseBudget])
def read_budgets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    budgets = db.query(
        Budget.id,
        Budget.month,
        Budget.income,
        Budget.consumption,
        Budget.profit,
        Budget.kpn,
        Company.name.label("company_name")
    ).join(Company).offset(skip).limit(limit).all()

    return [BaseBudget(
        id=budget.id,
        month=budget.month,
        income=budget.income,
        consumption=budget.consumption,
        profit=budget.profit,
        kpn=budget.kpn,
        company_name=budget.company_name
    ) for budget in budgets]


@router.post("/")
def create_budget(request: BudgetCreate, db: Session = Depends(get_db)):
    new_budget = Budget(**request.model_dump())

    db.add(new_budget)
    db.commit()
    db.refresh(new_budget)

    return new_budget


@router.delete("/{pk}")
def delete_budget(pk: int, db: Session = Depends(get_db)):
    budget = db.query(Budget).filter(Budget.id == pk).first()

    if not budget:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Budget not found")

    db.delete(budget)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{pk}")
def update_budget(request: BudgetCreate, pk: int, db: Session = Depends(get_db)):
    budget = db.query(Budget).filter(Budget.id == pk).first()

    if not budget:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Budget not found")

    for key, value in request.model_dump().items():
        setattr(budget, key, value)

    db.commit()
    db.refresh(budget)

    return budget
