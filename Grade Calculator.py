# subroutine to calculate average
def calculate_average(total_points, count):
    if count == 0:
        return 0
    return total_points/count

# main program
print("==== Grade Calculator ====")
num_tests = 3
total = 0

for i in range (num_tests):
    valid_score = False
    while not valid_score:
        score = int(input(f" Enter Score for test {i+1} (0-100):"))
        if score >= 0 and score <= 100:
            valid_score = True
        else:
            print("Invalid score please enter a number between 1 and 100")
    total += score

final_avg = calculate_average(total, num_tests)
print("============================")
print(f" The average score is {final_avg}")
print("============================")
