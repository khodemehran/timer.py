import time

input1 = int(input('enter time by second:'))

minute = 0 
sec = 0

for k in range(input1):
    
    sec += 1
    time.sleep(1)
    print(sec)
    if sec == 60:
        minute+=1
        print(minute)
        
    
print(sec,minute)

