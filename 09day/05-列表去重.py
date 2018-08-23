list = [1,2,3,3]
list1 = []
for i in list:
	if i not in list1:
		list1.append(i)
print(list1)
'''
print(list(set(list1)))
'''

print(list(set(list)))
'''
