from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = {
    1: {"name":"Manpreet","age":30},
    2: {"name":"Rose","age":25},
    3: {"name":"Jenny","age":30},
    4: {"name":"Tracy","age":23},
    5: {"name":"Julia","age":27},
    6: {"name":"Tina","age":29},
    7: { "name":"Diana","age":35}
}


class User(BaseModel):
    name:str
    age:int


@app.put("/user_db/data/info/update/{user_id}")
def user_upadate(user_id:int,user:User):
    if user_id in user_db:
        user_db[user_id]=user.dict()
        print(user_db)
        return {"message": "User updated successfully", "user": user_db[user_id]}
    else:
        return {"message": "User not found"}
    

@app.delete("/user_db/data/info/delete/{user_id}")
def delete_user(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}
    



