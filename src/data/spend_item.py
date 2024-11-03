from typing import List

from models.spend_item import SpendItem
from data.db_setup import get_tenant_db

def get_spend_items() -> List[SpendItem]:
  db_session = get_tenant_db()
  return db_session.query(SpendItem).all()

# TODO: Add spend type properly 
def add_spend_item(spend_item: SpendItem):
  db_session = get_tenant_db()
  db_session.add(spend_item)
  db_session.commit()

def delete_spend_item(item_id: int):
  db_session = get_tenant_db()
  db_session.query
