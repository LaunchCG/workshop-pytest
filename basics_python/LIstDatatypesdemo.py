

###### List data types are mutable we can change or update the values of list
####   wheras tuples are immutable
def testListdemo():
    a = [1, 2, "Python",5 , "testing", 6, 7, 10]

    print(a[0])
    print(a[3])
    print(a[-1]) #last value of the list or array
    print(a[0:5]) # print from 1st value to index 3
    print("===========================================")
    ###=====>>> adding value to list
    a.insert(2, "frame")
    print(a)
    a.append("End value")
    print(a)

    ##  update the value
    a[2] = "PYTHON"
    print(a)

    del a[2]
    print(a)