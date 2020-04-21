n=int(input('Enter Your Number :'))
for i in range(n-1):
	print(''+n+'*')
for j in range(1,n):
	print(''*(j-1)+'*'+' '*(n-j)+'*'+' '*(n-j)+' *')
print(' '*n+'*')