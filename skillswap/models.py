import uuid
from datetime import datetime

class User:
    def __init__(self, name: str, email: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.skills = []  # List of skill IDs
        self.exchanges = []  # List of exchange IDs

    def validate_email(self):
        if '@' not in self.email:
            raise ValueError("Invalid email address")

class Skill:
    def __init__(self, name: str, user_id: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.user_id = user_id
        self.is_offered = True

class Exchange:
    def __init__(self, offerer_id: str, receiver_id: str, offered_skill_id: str, requested_skill_id: str):
        self.id = str(uuid.uuid4())
        self.offerer_id = offerer_id
        self.receiver_id = receiver_id
        self.offered_skill_id = offered_skill_id
        self.requested_skill_id = requested_skill_id
        self.created_at = datetime.now()