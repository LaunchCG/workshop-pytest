import mysql.connector
 
 
cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')

cursor = cnx.cursor()

return_set = []
read_consultant_query = ("SELECT idconsultant, consultant_name, consultant_title, consultant_location,"
                             " consultant_discipline FROM pytest_workshop.consultant")

 # Execute and Print consultant information
cursor.execute(read_consultant_query)

for (idconsultant, consultant_name, consultant_title, consultant_location, consultant_discipline) in cursor:
    print(f"{idconsultant} {consultant_name} - {consultant_title} is located in {consultant_location} "
          f"and is part of the {consultant_discipline} Discipline")
    return_set.append({"idconsultant": idconsultant,
                       "consultant_name": consultant_name,
                       "consultant_title": consultant_title,
                       "consultant_location": consultant_location,
                       "consultant_discipline": consultant_discipline})
    
results = {"consultant": return_set}
print (results)