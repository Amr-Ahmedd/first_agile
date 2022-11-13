x = int(input("Enter the list size "))
size_list = []
print("enter values of your list ")

for i in range(0, x):
    item = input()
    if item.isdigit():
        size_list.append(item)
print("User list is ", size_list)
print("1")
amr = 31
am = 1