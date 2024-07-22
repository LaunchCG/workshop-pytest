import mysql.connector


def test_create_new_user():
    cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='pytest_workshop')
    cursor = cnx.cursor()

    update_consultant = ("Update consultant Set consultant_location ='BHARATH' Where consultant_name = 'Pradeep Edara'")

    cursor.execute(update_consultant)

    cnx.commit()

    cursor.close()
    cnx.close()
