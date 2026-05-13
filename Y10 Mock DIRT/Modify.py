import time

for i in range(5):
    temp = int(input("Enter temperature: "))
    if temp > 30:
        for i in range(3):
            print("ALARM")
            time.sleep(1)