def test_demo():

    #### Numaric and string data types...................
    
    a = 3
    b, c, d, e = "Ram", "Raath", "Testing", 1083.3245678
    name = [1, 3, 2, "python"]
    # print("value of a is: " +str(a))

    ##  format method
    print("{} {} {} {}".format("value of a is: ", a, "name value is: ", name))
    print(type(a), type(e))

## simple print statement
# print(f"value a is : {a}")

##  variable is sting print
# print("b value is : "+b)

##  simple for loop
# for item in name:
#     print(item)
##  index mechanism
# print(name[3])

##  for loop for printing only one data type
    for item in name:
        if isinstance(item, int):
            print(item)
