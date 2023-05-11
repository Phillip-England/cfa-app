class UserResponse:
    def __init__(self, _id: str, email: str):
        self._id = str(_id)
        self.email = email

    def __dict__(self):
        return {"_id": self._id, "email": self.email}
