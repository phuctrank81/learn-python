"""
Kiểm tra xem có được vào rạp chiếu phim không

"""

age = 40
has_ticket = True
has_parent = True

# điều kiện để vào xem phim
# phải có vé phim và tuổi từ 18 trở lên hoặc bằng 18
# phải vừa có thỏa mãn về vé , vừa thỏa mãn về tuổi tác
can_enter = has_ticket and (age >= 18 or has_parent)
print("Được vào rạp chiếu phim:", can_enter)
