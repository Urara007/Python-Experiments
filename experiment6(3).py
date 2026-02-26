n = int(input("Enter number of students: "))
scores = list(map(int, input("Enter scores separated by space: ").split()))
unique_scores = sorted(list(set(scores)))
if len(unique_scores) > 1:
    print(f"Runner-up score: {unique_scores[-2]}")
else:
    print("No runner-up available.")