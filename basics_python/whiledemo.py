it = 10
while it>2:
    print(it)
    it = it-1

print("while loop execution is ended, out of the loop")

print("========================================")
i = 10
while i>1:
    if i==3:
        break
    print(i)
    i = i-1

print("while loop execution is ended, out of the loop")

print("=====================================")

a = 10
while a > 1:
    if a == 9:
        a = a-1
        continue
    if a == 3:
        break
    print(a)

    a = a-1

print("while loop execution is ended, out of the loop")