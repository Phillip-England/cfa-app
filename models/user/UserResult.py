from bson import ObjectId


class UserResult:
    def __init__(self, _id: ObjectId, email: str, password: str):
        self._id = str(_id)
        self.email = email
        self.password = password
