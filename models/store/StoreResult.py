class StoreResult:
    def __init__(self, _id: str, user: str, name: str, number: int):
        self._id = str(_id)
        self.user = user
        self.name = name
        self.number = number

    def __dict__(self):
        return {"_id": self._id, "name": self.name, "number": self.number}
