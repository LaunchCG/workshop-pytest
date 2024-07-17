### tuples are mutable we can not change or modify tuples values it means lock
## list and tuples does the same thing but only diference is mutable and immutable
#### list--> [] and tuples--> ()

def test_tuplesdemo():
     value = (1, 2, 3, "Test", 7.8)
     print(value[0])
     #value[1] = "70"
     print(value)
     print(value[-1])
     print(value[0:3])

####=======>>> Dictionary==========>>>#### key: value pair in {}
print("----------------------dictionaryyy result ---------------------")
def test_dictio():
    val = {1: "intr", "str": 3, 4.6:"test"}
    print(val[1])
    print(val["str"], val[4.6])

##  Create dictionaries at run time and add data into it
    print("=======dictionaries adding the data at run time=========")
    dict = {}

    dict["firstname"] = "Python"
    dict["lastname"] = "pytest"
    dict[1] = "testing"
    print(dict)  ### output: {'firstname': 'Python', 'lastname': 'pytest', 1: 'testing'}
