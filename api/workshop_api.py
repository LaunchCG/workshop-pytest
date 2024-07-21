from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.get("/studios")
def read_root():
    return {"Hello": "World"}

@app.post("/studios/post")
def create_studio():
    return {"studio_name_created": "Another cool Studio"}

@app.put("/disciplines/put")
def update_discipline():
    return {"disciplines_name": "My cool Disciplines",
            "studio_name": "Software Engineering"}
    
@app.delete("/disciplines/delete")
def delete_discipline():
    return {"studio_name": "Another cool Studio"}