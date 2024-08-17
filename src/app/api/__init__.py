from fastapi import APIRouter

from app.api import healthcheck
from app.api.v1 import budget, company

router = APIRouter()

router.include_router(healthcheck.router, prefix="")
router.include_router(budget.router, prefix="/budget")
router.include_router(company.router, prefix="/company")
