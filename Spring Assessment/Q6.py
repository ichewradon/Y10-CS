def countDays(openDays):
    allVisitors = 0
    over200 = 0
    
    for day in range(openDays):
        daily_visitors = int(input(f"How many visitors on day {day + 1}?"))
        allVisitors += daily_visitors
        
        if daily_visitors > 200:
            over200 += 1
            
    print(f"Total visitors: {allVisitors}")
    print(f"Days with over 200 visitors: {over200}")

num_days = int(input("How many days open? "))
countDays(num_days)
