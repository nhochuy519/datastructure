

path = 'a_test.txt'


# with chủ yếu được sử dụng để tự động đóng tài nguyên sau khi hoàn tất việc sử dụng
with open(path,'r') as f: # r read : đọc file
    # print(f.read()) # in ra nd file
    # print(f.readlines()) # in ra nd và đưa nó vào list
    for value in f :
        # print(value)
        print(value.rstrip()) # xoá khoảng cách
    
with open('writeFile.txt','w') as f : # w ghi file ghi đè
    f.write('nishinomiya konomi')

with open('writeFile.txt','a') as f : # ghi theem append
    f.write("\nrola takizawa")


 