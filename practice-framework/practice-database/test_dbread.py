import mysql.connector


def test_read_user_entry():
    cnx = mysql.connector.connect(user='root', password='Deb@launch', host='localhost', database='pytest_workshop')

    cursor = cnx.cursor()

    read_consultant_query = (
        "SELECT idconsultant, consultant_name, consultant_title, consultant_location, consultant_discipline from consultant")

    cursor.execute(read_consultant_query)

    for (idconsultant, consultant_name, consultant_title, consultant_location, consultant_discipline) in cursor:
        print(
            f"{idconsultant} {consultant_name} {consultant_title} is located in {consultant_location} f and is part of the {consultant_discipline} Discipline")

    if consultant_name == 'Debasish Karmakar':
        assert consultant_title == 'Quality Assurance Engineer'
        assert consultant_location == 'INDIA'
        assert consultant_discipline == 'Test & Test Automation Discipline'

    cursor.close()
    cnx.close()
