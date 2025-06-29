from uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class BookModel(Base):
    __tablename__ = 'books'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    title : Mapped[str]
    author : Mapped[str]