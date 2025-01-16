file = open('nums.txt', 'r')
content = file.readlines()
print(content)
print(int(content[-1])+int(content[5]))