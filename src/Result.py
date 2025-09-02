import repository.crud as crud
from datetime import datetime

def InsertResult(db, text, audio_name):
    data = {
        "text": text,
        "audio_name": audio_name,
        "updated_at": datetime.now().isoformat(),
    }
    response, message = crud.Create(db, "Result", data)
    return response, message

def GetResultByID(db, id):
    response, message = crud.GetByID(db, "Result", "*", id)
    return response, message


def GetAllResults(db):
    response, message = crud.GetAll(db, "Result", "*")
    return response, message

def UpdateResult(db, id, new_text, new_audio_name):
    data = {
        "text": new_text,
        "audio_name": new_audio_name,
        "updated_at": datetime.now().isoformat(),
    }
    response, message = crud.Update(db, "Result", data, id)
    return response, message

def DeleteResult(db, id):
    response, message = crud.Delete(db, "Result", id)
    return response, message