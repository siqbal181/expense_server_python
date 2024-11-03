from typing import List

from data.db_setup import get_tenant_db
from data.item_structure import SpendItemStructure

from models.spend_item import SpendItem

def get_spend_items() -> List[SpendItem]:
  session, _ = get_tenant_db()
  return session.query(SpendItem).all()

# TODO: Add spend type properly 
def add_spend_item(spend_item: SpendItemStructure):
  spend_item_object = SpendItem(amount=spend_item.amount)
  session, _ = get_tenant_db()
  session.add(spend_item_object)
  session.commit()

# def delete_spend_item(item_id: int):
#   db_session = get_tenant_db()
#   db_session.query
