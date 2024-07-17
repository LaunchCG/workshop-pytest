# file = open('test.txt')
# file.close()

#read the file and store all the lines in list
#reverse the list
#write the list back to the file

#### here 'r' args is for read the file indication,,, if you don't mention 'r' or 'w' it will take read file by default
#### and 'w' args is for write the file indication

with open('test.txt', 'r') as reader:        ### by this approach no need to write file.close(),
    content = reader.readlines()
    reversed_Content = reversed(content)
    rev_list_cont = list(reversed_Content)
    with open('test.txt', 'w') as writer:
        for line in rev_list_cont:
            writer.write(line)



###
# with open('test.txt', 'r') as reader:
#     content = reader.readlines()
#
# # Reverse the content
# reversed_content = list(reversed(content))  # Convert the reversed iterator to a list
#
# # Write the reversed content back to the file
# with open('test.txt', 'w') as writer:
#     for line in reversed_content:
#         writer.write(line)

