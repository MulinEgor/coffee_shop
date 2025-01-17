from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.models import Base


class Category(Base):
    """
    Sqlalchemy модель категории.
    """
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    