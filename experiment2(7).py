total_seconds = int(input("Enter seconds: "))
hours = total_seconds // 3600
remaining_sec = total_seconds % 3600
minutes = remaining_sec // 60
seconds = remaining_sec % 60
print(f"{hours} Hours, {minutes} Minutes, {seconds} Seconds")