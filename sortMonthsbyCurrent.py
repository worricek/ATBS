from datetime import datetime

months=['january','february','march','april','may','june','july','august','september','october','november','december']
orderedMonths=[]
now=datetime.now().month
counter=now
flag=0

while True:
    orderedMonths.append(months[counter-1])
    if counter == 12:
        counter = 1
        continue
    if counter == now-1:
        break
    counter+=1

print(orderedMonths)
