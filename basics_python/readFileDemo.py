
file = open("test.txt")
# print(file.read(2))
# print(file.readline()) ## read one single line at a time
#print(file.read())   ## All the lines at a time


#####====while loops using readline function
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

#####====for loop using readlines method this method will save the file each line data into list
for filedata in file.readlines():
    print(filedata)


file.close()