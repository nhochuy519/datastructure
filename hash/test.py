"""
    Cách xử lý va chạm:
Có nhiều kỹ thuật xử lý va chạm, trong đó phổ biến nhất là:

Dùng chuỗi liên kết (Chaining): Thay vì lưu trực tiếp giá trị tại vị trí bị va chạm, ta có thể lưu một danh sách liên kết (linked list) hoặc mảng tại vị trí đó. Khi xảy ra va chạm, phần tử mới sẽ được thêm vào danh sách tại vị trí băm.

Tuyến tính thăm dò (Linear Probing): Khi xảy ra va chạm, ta tìm vị trí tiếp theo còn trống trong bảng và lưu phần tử vào đó.


unmutable : không thể thay đổi

"""


# hashsets

s = set()


# Add item into set - 0(1)
print(s)
s.add(1)
s.add(2)
s.add(3)
print(s)
# lookup if item in set - 0(1)
if 1 not in s:
    print(True)
# Remove item from set - 0(1)
s.remove(3)
print(s)
# Set construction - 0(S) - S is the length of the string
string = "aaaaaaabbbbbssssddddd"
sett = set(string)
print(sett)

# Loop over items in set - 0(n)
for x in s:
    print(x)
# hashmaps - Dictionaries
d = {
    "greg":1,
    "steve":2,
    'rob':3
}

# add key:val in dictionary : 0(1)
d["huy"]=4
print(d)
# check for presence of key in dictionary : 0(1)
if 'greg' in d:
    print(True)
# check the value corresponding to a key in the dictionary: 0(1)
print(d['huy'])

#loop over the key:val pairs of the dictionary: 0(n)
for key, val in d.items():
    print(f'key {key} :val {val}')

# Defaultdict
from collections import defaultdict
default = defaultdict(int) # khởi tại mặc đinh cho các giá trị của khoá không tồn tại bằng 0
print(default['huy'])
print(default)

# Counter 
from collections import Counter
# đếm số lượng ký tự hiện có trong chuỗi string
counter = Counter(string)
print(counter)


s=[1,2,3]
print(s[-1])