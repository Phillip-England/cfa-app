from pymongo.collection import Collection

from models import SessionModel, SessionResult


def insert_session(session_collection: Collection, session: SessionModel):
    result = session_collection.insert_one({"user": session.user})
    session_result = SessionResult(result.inserted_id, session.user)
    return session_result
