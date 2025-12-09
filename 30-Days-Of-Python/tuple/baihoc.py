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
print(new_tuple)  # Output: (4, 'phuc dep trai', 2)
