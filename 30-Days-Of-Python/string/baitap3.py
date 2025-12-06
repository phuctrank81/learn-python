"""

Đếm số lượng nguyên âm xuất hiện trong một câu tiếng Anh.

nguyên âm trong tiếng anh: u, e, o, a, i

"""

sentence = input("Nhập vào một câu tiếng Anh: ")

count = 0


vowels ="ueoai"

sentence = sentence.lower()

for char in sentence:
    if char in vowels:
        count += 1

print("Số lượng nguyên âm trong câu là :", count)