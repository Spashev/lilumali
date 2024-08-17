from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey


class Base(DeclarativeBase):
    pass


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    budgets: Mapped[list["Budget"]] = relationship("Budget", back_populates="company")


class Budget(Base):
    __tablename__ = "budgets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    month: Mapped[str] = mapped_column(String(255), nullable=False)
    income: Mapped[int] = mapped_column(Integer, nullable=False)
    consumption: Mapped[int] = mapped_column(Integer, nullable=False)
    profit: Mapped[int] = mapped_column(Integer, nullable=False)
    kpn: Mapped[int] = mapped_column(Integer, nullable=False)
    company_id: Mapped[int] = mapped_column(Integer, ForeignKey("companies.id"), nullable=False)

    company: Mapped["Company"] = relationship("Company", back_populates="budgets")
