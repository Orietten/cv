data = {}
while True:
    s = input()
    if s == 'конец':
        break
    prod = s.split(': ')[0]
    prices = s.split(': ')[1].split(': ')[0]
    data[prod]= prices

products = input()
products = products.split(', ')

months = {1:0, 2:0, 3:0}
for p in products:
    months[1] += int(data[p][0])
    months[2] += int(data[p][1])
    months[3] += int(data[p][2])

months_values = months.values()  
mini = min(months_values)     

for a in months:
    if months[a] == mini:
        print(a)
        print(mini)
    
N = int(input())
channels_rating = {}
for i in range (N):
    s = input()
    new_spisok = s.split(': ')
    
    channels = new_spisok[1].split(', ')
    mx_rt = len(channels)
    for ch in channels_rating:
        if ch in channels:
            channels_rating[ch] += mx_rt
        else:
           channels_rating[ch] = mx_rt
        mx_rt -= 1

maxi = max(channels_rating.values())

for ch in channels_rating:
    if channels_rating[ch] == maxi:
        print(ch)




