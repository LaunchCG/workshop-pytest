import mysql.connector


def test_create_new_user():
    cnx = mysql.connector.connect (user ='root', password = 'root',# type: ignore
                                   host = '127.0.0.1',
                                   database = 'pytest_workshop')
    
    cursor = cnx.cursor()
    
    add_consultant = ("INSERT INTO consultant "
                      "(consultant_name, consultant_title, consultant_location, consultant_discipline) "
                      "VALUES (%s, %s, %s, %s)")
    
    data_consultant = ("Malcolm Haslop", "Quality Assurance Engineer", "Argentina", "Test & Test Automation")
    
    # Import new employee
    cursor.execute(add_consultant, data_consultant)
    
    # Make sure data is commited to the database
    cnx.commit()
    
    cursor.close()
    cnx.close()
    

def test_read_new_consultant():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')
    
    cursor = cnx.cursor()
    
    read_consultant_query = ("SELECT idconsultant, consultant_name, consultant_title, consultant_location, "
                             "consultant_discipline FROM consultant")
    
    # Execute and print consultant information
    cursor.execute(read_consultant_query)
    
    for (idconsultant, consultant_name, consultant_title, consultant_location, consultant_discipline) in cursor:
        print(f"{idconsultant} {consultant_name} - {consultant_title} is located in {consultant_location} "
              f"and is part of the {consultant_discipline} Discipline")
        
        if consultant_name == 'Malcolm Haslop':
            assert consultant_title == 'Quality Assurance Engineer'
            assert consultant_location == 'Argentina'
            assert consultant_discipline == 'Test & Test Automation'
            
    cursor.close()
    cnx.close()