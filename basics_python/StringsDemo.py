
str = "PythonPytesttestingdmeo12345"
str1 = "    stringsecond       "
str2 = "Pytest"

print(str[2])  # index of string
print(str[0:4]) # if you want substring in python
print(str+str2)  #concatenation

print(str2 in str) # substring check

var = str.split("1")
print(var)
print(var[1])

print(str1.strip())  # trim
str1.rstrip()  ## right space trim
str1.lstrip()  ## left space trim