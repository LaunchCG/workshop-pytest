import mysql.connector
from mysql.connector import cursor


def test_create_new_user():
    cnx = mysql.connector.connect(user='root',password='root', host='localhost', database='pytest_workshop')
    cursor = cnx.cursor()
    read_consultant_query = ("select idconsultant,consultant_name,consultant_title,consultant_location,"
                             "consultant_discipline from consultant")

    cursor.execute(read_consultant_query)

    result=cursor.fetchall()

    for (idconsultant, consultant_name, consultant_title, consultant_location,consultant_discipline) in result:
        print(f"{idconsultant} {consultant_name} - {consultant_title} is located in  {consultant_location} "
              f"and is part of the {consultant_discipline} Discipline")
        if consultant_name == 'Pradeep Edara':
            assert consultant_title == 'Software Development Engineer in Test'
            assert consultant_location == 'India'
            assert consultant_discipline == 'Test & Test Automation'

    cursor.close()
    cnx.close()