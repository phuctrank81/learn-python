# my_list = [12, 3.5, "Hello", True, None]

# print(type(my_list))

# my_list = [12, 3.5, "Hello", True, [5, 6, 7]]
# print(len(my_list))  Output: 5
# print(my_list[0])    Output: 12
# print(my_list[1:])
# print(my_list[:-1])   Output: [5, 6, 7]

# my_list = [12, 3.5, "Hello", True, [5, 6, 7]]
# for x in my_list:
#     print(x, end=" ")

# list_1 = [1, 4.5, 10]
# list_2 = ["anh", "em"]
# concat_list = list_1 + list_2
# print(concat_list)

# list_phuc = [1, 4.5, 10]
# list_phuc[1] = "hello"
# print(list_phuc)  # Output: [1, 'hello', 10]

# 1. add list element using append()
# 2. add element .extend()
# 3. sort list .sort() or sorted()
# 4. reverse list .reverse()
# 5  insert element .insert(index, value)
# 6. delete element del or .remove()
# 7. trả về index đầu tiên của elemnet được khớp .index() (Ko có error)
# 8. pop(index) ko truyền xóa ele cuối 

""" 1 """
my_lst = [1,2,3]
my_lst.append(4)
print(my_lst)  # Output: [1, 2, 3, 4]

""" 2 """
phucTran = [10,2,4]
phucTran.extend(["phuc"])
print(phucTran)  # Output: [10, 2, 4, 'phuc']

""" 3 """
trangTran = [4,-4,-23,45]
trangTran.sort()
print(trangTran)  # Output: [-23, -4, 4, 45]

newTrang = sorted(trangTran)
print(newTrang)  # Output: [-23, -4, 4, 45]

""" 4 """
locTran = [1,4,5,-5]
# locTran.reverse()
print(locTran)  # Output: [-5, 5, 4, 1]
new_list = locTran[::-1]
print(new_list)  

""" 5 """
insertList = [1,2,3,4]
insertList.insert(0,45)
print(insertList)  # Output: [45, 1, 2, 3, 4]

""" 6 """
phucdepTrai = [1,2,3,4,5]
# del phucdepTrai[0]
del phucdepTrai[:2]
print(phucdepTrai)  # Output: [2, 3, 4, 5]

""" 7 """
conCac = [1,4523,34,52]
numbberIndex = conCac.index(34)
print(numbberIndex)  # Output: 0