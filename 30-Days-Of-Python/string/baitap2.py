"""
In ra tất cả các ký tự trong string (chuỗi) mà là chữ số .isdigit()

"""

"""
Kí tự trong Python là string có chiều dài bằng một, ví dụ "a", "3"

"""

phucDepTrai = input("Nhập chuỗi của bạn: ")


for hung in phucDepTrai:
    if hung.isdigit():
        print(hung , end="")

print(phucDepTrai[:-1])