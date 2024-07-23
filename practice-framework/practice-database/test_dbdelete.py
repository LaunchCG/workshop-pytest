import mysql.connector

def test_update_consulatant():
    cnx = mysql.connector.connect(user='root', password='Deb@launch', host='localhost', database='pytest_workshop')

    cursor = cnx.cursor()

    delete_consultant_query = ("DELETE FROM consultant WHERE consultant_name = 'Debasish Karmakar'")

    cursor.execute(delete_consultant_query)

    cnx.commit()

    cursor.close()
    cnx.close()
