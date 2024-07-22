import mysql.connector


def test_create_new_user():
    cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='pytest_workshop')
    cursor = cnx.cursor()

    # add_consultant = ("INSERT INTO consultant "
    #                   "(consultant_name, consultant_title,consultant_location,consultant_discipline) "
    #                   "VALUES (%s, %s, %s, %s)")
    #
    # data_consultant = ('Pradeep Edara2', 'SDET', 'INDIA', 'Test & Test Automation')

    # cursor.execute(add_consultant,data_consultant)

    add_consultant = ("INSERT INTO consultant "
                      "(consultant_name, consultant_title,consultant_location,consultant_discipline) "
                      "VALUES ('Pradeep Kumar Reddy', 'SDET', 'INDIA', 'Test & Test Automation')")
    cursor.execute(add_consultant)

    cnx.commit()

    cursor.close()
    cnx.close()
