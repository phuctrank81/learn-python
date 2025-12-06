"""
abcd.txt ab.cd.txt
Tên file: abc abcd ab.cd
Extension: png txt txt
"""

my_str = input("Nhập vào tên file đầy đủ extension: ")

dot_position = -1

for i in range(len(my_str)):
    if my_str[i] == ".":
        dot_position = i
print("Extension là:", my_str[(dot_position):])
print("Tên file:", my_str[:dot_position])