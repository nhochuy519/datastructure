arr =[1,2,3]
tu = (1,2,3)
se = {1,2,3,4,3}

help(Exception)

try :
    tu[0]=1
    print('hello')
except Exception as err : 
    print('tuple khong the truy cap qua chi muc')
    print(err)

try :
    x = int("abc")
    tu[0]=1
    print('hello')
    
except TypeError as err : 
    print('tuple khong the truy cap qua chi muc')
    print(err)


try :
    x = int("abc")
    tu[0]====
    print('hello')
    
except SyntaxError as err : 
    # bat loi cu phap
    print(err)

#TypeError, ValueError, IndexError, SyntaxEror

# Ví dụ 1: Cộng chuỗi với số nguyên
x = "abc" + 123  # Gây ra TypeError
# Ví dụ 1: Chuyển đổi chuỗi không phải là số thành số nguyên
x = int("abc")  # Gây ra ValueError
# Ví dụ 1: Truy cập phần tử không tồn tại trong danh sách
lst = [1, 2, 3]
x = lst[5]  # Gây ra IndexError