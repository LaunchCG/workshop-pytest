import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import mysql.connector
from mysql.connector import Error
from schemas import Consultant, Discipline, Studio

print('loading environment variables...')
load_dotenv()

db_user = os.getenv('DATABASE_USER')
db_password = os.getenv('DATABASE_PASSWORD')
db_host = os.getenv('DATABASE_HOST')
db_name = os.getenv('DATABASE_NAME')


def get_db_cursor():
    cnx = mysql.connector.connect(user=db_user, password=db_password,host=db_host, database=db_name)
    cursor = cnx.cursor()
    return cursor, cnx

def terminate_db_connection(cnx, cursor):
        if cursor is not None and 'cursor' in locals():
            cursor.close()
        if cnx is not None and cnx.is_connected():
            cnx.close()


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/consultants")
def read_consultants():
    try:
        cursor = get_db_cursor()

        return_set = []
        read_consultant_query = ("SELECT idconsultant, consultant_name, consultant_title, consultant_location,"
                                " consultant_discipline FROM pytest_workshop.consultants")

        # Execute and Print consultant information
        cursor.execute(read_consultant_query)

        for (idconsultant, consultant_name, consultant_title, consultant_location, consultant_discipline) in cursor:
            print(f"{idconsultant} {consultant_name} - {consultant_title} is located in {consultant_location} "
                f"and is part of the {consultant_discipline} Discipline")

            return_set.append({"idconsultant": idconsultant,
                            "consultant_name": consultant_name,
                            "consultant_title": consultant_title,
                            "consultant_location": consultant_location,
                            "consultant_discipline": consultant_discipline})
        
        terminate_db_connection(cursor)

        response = {"consultants": return_set}
        return response

    except Error as e:
        print(f"Error: {e}")
        return JSONResponse(content=f"Database error: {e}", status_code=500)


@app.get("/disciplines")
def read_disciplines():
    try:
        cursor = get_db_cursor()

        return_set = []
        read_consultant_query = "SELECT iddisciplines, discipline_name, studio_name FROM pytest_workshop.disciplines"

        # Execute and Print consultant information
        cursor.execute(read_consultant_query)

        for (iddisciplines, discipline_name, studio_name) in cursor:
            print(f"{iddisciplines} {discipline_name} is in the {studio_name} studio")

            return_set.append({"iddisciplines": iddisciplines,
                            "discipline_name": discipline_name,
                            "studio_name": studio_name})
        
        terminate_db_connection(cursor)

        response = {"disciplines": return_set}
        return response

    except Error as e:
        print(f"Error: {e}")
        return JSONResponse(content=f"Database error: {e}", status_code=500)


@app.get("/studios")
def read_studios():
    try:
        cursor = get_db_cursor()

        return_set = []
        read_consultant_query = "SELECT idstudios, studio_name FROM pytest_workshop.studios"

        # Execute and Print consultant information
        cursor.execute(read_consultant_query)

        for (idstudios, studio_name) in cursor:
            print(f"{idstudios} {studio_name}")

            return_set.append({"idstudios": idstudios,
                            "studio_name": studio_name})
        
        terminate_db_connection(cursor)

        response = {"studios": return_set}
        return response

    except Error as e:
        print(f"Error: {e}")
        return JSONResponse(content=f"Database error: {e}", status_code=500)


@app.post("/consultants/post")
def create_consultants(consultant: Consultant):
    try:
        cursor, cnx = get_db_cursor()

        add_consultant = ("INSERT INTO consultants "
                        "(consultant_name, consultant_title, consultant_location, consultant_discipline) "
                        "VALUES (%s, %s, %s, %s)")

        data_consultant = (consultant.consultant_name, consultant.consultant_title,
                        consultant.consultant_location, consultant.consultant_discipline)

        # Insert new consultant
        cursor.execute(add_consultant, data_consultant)

        # Make sure data is committed to the database and close connection is necessary
        print('comitting transaction...')
        cnx.commit()
        print('closing database connection...')
        terminate_db_connection(cnx, cursor)

        response = {"consultant_name_return": consultant.consultant_name,
                "consultant_title_return": consultant.consultant_title,
                "consultant_location_return": consultant.consultant_location,
                "consultant_discipline_return": consultant.consultant_discipline}
        
        return JSONResponse(content=response, status_code=200)

    except Error as e:
        print(f"Error: {e}")
        return JSONResponse(content=f"Database error: {e}", status_code=500)


@app.post("/disciplines/post")
async def create_disciplines(discipline: Discipline):

    try:
        cursor, cnx = get_db_cursor()

        add_discipline = ("INSERT INTO disciplines "
                        "(discipline_name, studio_name) "
                        "VALUES (%s, %s)")

        data_discipline = (discipline.discipline_name, discipline.studio_name)

        # Insert new consultant
        cursor.execute(add_discipline, data_discipline)

        # Make sure data is committed to the database and close connection is necessary
        print('comitting transaction...')
        cnx.commit()
        print('closing database connection...')
        terminate_db_connection(cnx, cursor)

        response = {"discipline_name_returned": discipline.discipline_name,
                "studio_name_returned": discipline.studio_name}
        
        return JSONResponse(content=response, status_code=200)
    
    except Error as e:
        print(f"Error: {e}")
        return JSONResponse(content=f"Database error: {e}", status_code=500)


@app.post("/studios/post")
async def create_studios(studio: Studio):

    try:
        cursor, cnx = get_db_cursor()

        add_studio = f"INSERT INTO studios (studio_name) VALUES ('{studio.studio_name}')"
        print(add_studio)

        # Insert new consultant
        cursor.execute(add_studio)

        # Make sure data is committed to the database and close connection is necessary
        print('comitting transaction...')
        cnx.commit()
        print('closing database connection...')
        terminate_db_connection(cnx, cursor)

        response = {"studio_name_created": studio.studio_name}

        return JSONResponse(content=response, status_code=200)

    except Error as e:
        print(f"Error: {e}")
        return JSONResponse(content=f"Database error: {e}", status_code=500)


@app.put("/disciplines/put")
async def update_disciplines(discipline: Discipline):

    try:
        cursor, cnx = get_db_cursor()

        update_discipline = ("UPDATE disciplines SET "
                            "studio_name = %s "
                            "WHERE discipline_name = %s")

        data_discipline = (discipline.studio_name, discipline.discipline_name)

        # Insert new consultant
        cursor.execute(update_discipline, data_discipline)

        # Make sure data is committed to the database and close connection is necessary
        print('comitting transaction...')
        cnx.commit()
        print('closing database connection...')
        terminate_db_connection(cnx, cursor)

        response = {"discipline_name_updated": discipline.discipline_name, 
                    "studio_name_updated": discipline.studio_name}
        
        return JSONResponse(content=response, status_code=200)

    except Error as e:
        print(f"Error: {e}")
        return JSONResponse(content=f"Database error: {e}", status_code=500)


@app.delete("/studios/delete")
async def update_studios(studio: Studio):

    try:
        cursor, cnx = get_db_cursor()
        delete_studio = f"DELETE FROM studios WHERE studio_name = '{studio.studio_name}'"
        # Insert new consultant
        cursor.execute(delete_studio)

        # Make sure data is committed to the database and close connection is necessary
        print('comitting transaction...')
        cnx.commit()
        print('closing database connection...')
        terminate_db_connection(cnx, cursor)

        response = {"studio_name_removed": studio.studio_name}

        return JSONResponse(content=response, status_code=200)
    
    except Error as e:
        print(f"Error: {e}")
        return JSONResponse(content=f"Database error: {e}", status_code=500)

