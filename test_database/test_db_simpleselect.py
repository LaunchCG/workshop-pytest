import mysql.connector


def test_create_new_user():
    cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='pytest_workshop')
    cursor = cnx.cursor()

    # read_consultant_query = ("SELECT * FROM consultant WHERE consultant_name = 'Pradeep Edara'")

    read_consultant_query = ("select idconsultant,consultant_name,consultant_title,consultant_location, "
                             "consultant_discipline from consultant")

    cursor.execute(read_consultant_query)

    result = cursor.fetchall()

    print(len(result))

    for row in result:
        print(row)

    cursor.close()
    cnx.close()
