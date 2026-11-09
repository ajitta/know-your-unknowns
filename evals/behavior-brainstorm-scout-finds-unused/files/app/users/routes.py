"""Request handlers for users."""


def routes(users):
    def create(data):
        user = users.create(data["name"], data["email"], data.get("role", "customer"),
                            data.get("plan"))
        return {"id": user.id, "role": user.role}

    def show(data):
        user = users.get(data["user_id"])
        return {"id": user.id, "name": user.name, "email": user.email, "role": user.role,
                "plan": user.plan, "is_active": user.is_active}

    return {
        ("POST", "/users"): create,
        ("GET", "/users/show"): show,
    }
