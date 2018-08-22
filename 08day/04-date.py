year = int(input("输入年"))
month = int(input("输入月"))
day = int(input("输入日"))
sum = day
days = [31,28,31,30,31,30,31,31,30,31,30,31]
i = 0
if(year%4 == 0 and year%100 != 0) or (year%400 == 0):
	days[1] = 29
while i < month-1:
	sum=sum+days[i]
	i+=1
print("今天是今年的第",sum,"天")
