print(chr(65)) # chữ A 

print(ord('A'))

numberToString = [chr(_) for _ in range(60,100)]
keyValue = [{chr(k):v} for k,v in zip(range(60,100),range(60,100))]

lambdaFCTest =lambda x,y:x+y
print(lambdaFCTest(1,2))

# toán tử ba ngôi
number =2
test3ngoi = 'so chan' if(number%2==0) else 'so le'
print(test3ngoi)


print(keyValue)