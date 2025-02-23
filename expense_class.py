import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self,title = None,amount = None):
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.id = uuid.uuid4()

    def update(self, title = None,amount=None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "id": str(self.id),
        }




    