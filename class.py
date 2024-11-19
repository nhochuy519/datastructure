class Human :
    def __init__(self,age,name): # hàm khỏi tạo
        self._age=age
        self._name =name
    
    def __str__(self): # phương thức dùng để định nghĩa cách mà đối tượng sẽ được biểu diễn dưới dạng chuỗi
        return f"{self._name} {self._age}"
    #Khi bạn gọi print() trên một đối tượng, Python sẽ tự động 
    # gọi phương thức __str__ để lấy chuỗi mô tả cho đối tượng đó. Phương thức này giúp bạn tùy chỉnh cách mà thông tin về đối tượng được hiển thị.

    def __repr__(self) : # dùng để tái tạo đối tượng
        return "hi"
    
    def older_younger_than(self,age:int)-> str:
        if self._age > age : 
            print('Tuoi cua doi tuong lon hon')
        elif self._age == age:
            print("tuoi bang nhau")
        else:
            print('Tuoi cu doi tuong do nho hon')
h = Human(age=18,name="Konomi")

print(h._age)
print(h)
print(h.__str__())
print(repr(h))

h.older_younger_than(20)


help(print)


