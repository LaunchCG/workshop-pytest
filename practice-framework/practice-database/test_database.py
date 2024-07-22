import mysql.connector


def test_create_new_user():

    cnx= mysql.connector.connect(user='root', password='Deb@launch', host='localhost', database='PytestWorkshop')

    cursor = cnx.cursor()

    add_consultant = (
        'INSERT INTO pytest_workshop.consultant'"(consultant_name, consultant_title, consultant_location, consultant_discipline )"
        "VALUES(%s,%s,%s,%s)")

    data_consultant = ('Debasish kmr', 'Quality Assurance Engineer', 'India', 'Test & Test Automation')

    cursor.execute(add_consultant, data_consultant)

    cnx.commit()

    cursor.close()
    cnx.close()
