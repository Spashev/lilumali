from pydantic import BaseModel
from typing import List


class BudgetBase(BaseModel):
    month: str
    income: int
    consumption: int
    profit: int
    kpn: int

    class Config:
        from_attributes = True


class BudgetCreate(BudgetBase):
    company_id: int


class Budget(BudgetBase):
    id: int
    company_name: str


class CompanyBase(BaseModel):
    name: str

    class Config:
        from_attributes = True


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    id: int


class CompanyWithBudgets(CompanyBase):
    id: int
    budgets: List[BudgetBase]
