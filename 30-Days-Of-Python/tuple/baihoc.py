tuple_1 = (12, 3.5, "Hello", True, (5, 6, 7)) # nhớ thêm 1 phần tử dấu phẩy
print(tuple_1)
print(type(tuple_1))  # Output: <class 'tuple'>


tuple_2 =(12,"phuc tran", 3.5)
print(len(tuple_2))  # Output: 3
for x in tuple_2:
    print(x, end=" ")  # Output: 12 phuc tran 3.5

tuple_3 = (4,"phuc dep trai", 2, 3)
tuple_4 = ("anh", "em",43,51)
new_tuple = tuple_3 + tuple_4
print(f"New tuple: {new_tuple}")  # Output: (4, 'phuc dep trai', 2)

tuple_5 = (1,2,3,4,5, "bac")
list_1 = list(tuple_5) 
# list_1.append("phuc tran")

list_1.remove("bac")
new_tuple_5 = tuple(list_1)
print(f"new tuple : {new_tuple_5}")  # Output: (1, 2, 3, 4, 5, 'bac', 'phuc tran')


tuple_10 = (145,24,32,524)
print(tuple_10.count(24))


tuple_11 = ("a", 124, 524, "b")
tuple_12 = ("a", 124, 524, "b")

print(f"ID of tuple_11: {id(tuple_11)}")
print(f"ID of tuple_12: {id(tuple_12)}")

tuple_13 = ([142,5,24],"a", 124, 524, "b")

tuple_13[0][0] = 0
print(tuple_13)  # Output: ('z', 124, 524, 'b')