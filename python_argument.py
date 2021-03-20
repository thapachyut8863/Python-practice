#here we will talk about the function and its argument in python so we can have better knowledge about it:
#pass by value and pass by reference in python:
def update(list):
    print(id(list))
    list[1] = 25
    print(id(list))
    print("x",list)

list = [10,20,30,40]
print(id(list))
update(list)
print("list",list)    