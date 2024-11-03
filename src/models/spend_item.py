from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func

from models.base import Base

class SpendItem(Base):
  __tablename__ = "spend_item"

  id = Column(Integer, autoincrement=True, primary_key=True)
  amount = Column(Integer)
  date = Column(DateTime(timezone=True), server_default=func.now())