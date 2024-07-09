# pydic={
#     "key1":"val1",
#     "key2":"val2",
#     "key3":"val3"
# }
# print(pydic)
# print(pydic.keys())
#
dicCar = {
    "brand":"Hyundai",
    "model":"i10",
    "year":2020,
    "color":"grey",
    "mileage":1000
}
# print(dicCar)
# # print(dicCar["brand"])
# # print(dicCar.get("color"))
# # print(dicCar["brand1"])
# # print(dicCar.get("color1"))
# dicCar["year"]=2022
# print(dicCar)
#
# for i in dicCar:
#     print(i)
#     print(dicCar[i])
#
# for i in dicCar.values():
#     print(i)
#
# for i in dicCar.keys():
#     print(i)

for x,y in dicCar.items():
    print(x,y)

if "model" in dicCar: print(dicCar["model"])

print("mileage" in dicCar)

print(len(dicCar))

dicCar["color1"]="red"
print(dicCar)