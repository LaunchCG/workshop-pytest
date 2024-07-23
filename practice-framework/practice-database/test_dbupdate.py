import mysql.connector

def test_update_consulatant():
    cnx = mysql.connector.connect(user='root', password='Deb@launch', host='localhost', database='pytest_workshop')

    cursor = cnx.cursor()

    update_consultant_query = ("UPDATE consultant "
                               "SET consultant_title = 'Software Development Eng in Test' "
                               "WHERE consultant_name = 'Debasish Karmakar'")

    cursor.execute(update_consultant_query)

    cnx.commit()

    cursor.close()
    cnx.close()