"""Creating and looking up users."""
from app.users.models import ROLES, User


class UserService:
    def __init__(self, store):
        self.store = store

    def create(self, name, email, role="customer", plan=None):
        if role not in ROLES:
            raise ValueError("unknown role %r" % role)
        email = email.strip().lower()
        if any(user.email == email for user in self.store.all("users")):
            raise ValueError("%s is already registered" % email)
        user = User(id=self.store.next_id("users"), name=name.strip(), email=email,
                    role=role, plan=plan)
        return self.store.put("users", user)

    def get(self, user_id):
        user = self.store.get("users", user_id)
        if user is None:
            raise KeyError("no user %s" % user_id)
        return user

    def agents(self):
        return [u for u in self.store.all("users") if u.role == "agent" and u.is_active]

    def deactivate(self, user_id):
        user = self.get(user_id)
        user.is_active = False
        return user
