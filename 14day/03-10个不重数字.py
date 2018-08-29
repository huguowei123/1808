import random
l = []
def num():
	while True:
		num = random.randint(1,100)
		if num not in l:
			l.append(num)
			if len(l) == 10:
				print(l)
				break
num()
a = l[7]	
print("索引为7值是%d"%a)
l.sort()
print(l)
min = 0
msx = len(l) - 1
while True:
	center = int((min+max)/2)
	if l[center] > a:
		max = center - 1
	elif l[center] < a:
		min = center + 1
	elif l[center] == a:
		print("升序后索引%d"%center)
		break
