import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_tenant_db():
  engine = create_engine("sqlite://python_expense_db")
  Session = sessionmaker(bind=engine)
  session = Session()
  return session, engine

