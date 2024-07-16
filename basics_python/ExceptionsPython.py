### use raise Exception........keywords for exceptions

ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart != 2:
    #raise Exception("Product cart can not matching")
    pass

# ======or======== use assertions

assert(ItemsInCart == 0)

# try ,catch(in python except)

## our own error print messge in exception block
try:
    with open('testog.txt', 'r') as reader:
        reader.readline()
except:
    print("some how i reached this block there is a failure in try block")


## actual exception mssge from python
try:
    with open('testog.txt', 'r') as reader:
        reader.readline()
except Exception as e:
    print("actuall expection retund: "+str(e))
    print("some how i reached this block there is a failure in try block")


### try, catch(except) and finally

try:
    with open('testog.txt', 'r') as reader:
        reader.readline()
except Exception as e:
    print("actual exception returned: "+str(e))

finally:
    print("cleaning up resources")
    print("cleaning up records")
    print("no matter what handled in try,except blocks but always i am going to execute")
