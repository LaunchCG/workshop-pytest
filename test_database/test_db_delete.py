import mysql.connector


def test_create_new_user():
    cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='pytest_workshop')
    cursor = cnx.cursor()

    update_consultant = ("Delete from consultant where consultant_name ='Pradeep Kumar Reddy Edara'")

    cursor.execute(update_consultant)

    cnx.commit()

    cursor.close()
    cnx.close()
