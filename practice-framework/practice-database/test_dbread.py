import mysql.connector

def test_read_user_entry():

    cnx = mysql.connector.connect(user='root', password='Deb@launch', host='localhost', database='pytest_workshop')

    cursor = cnx.cursor()

    read_consultant_query=("SELECT idconsultant, consultant_name, consultant_title, "
                           "consultant_location, consultant_discipline from consultant")

    cursor.execute(read_consultant_query)

    result = cursor.fetchall()
    print(result)

    cursor.close()
    cnx.close()