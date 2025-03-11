x = input()
print("您輸入的是",x)

if(x<0):
	print("您輸入的值為負數")

elif(x==0):
	print("您輸入的值等於0")

else:
	for i in range(1,x+1):
		print(i)

