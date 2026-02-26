name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
sap = input("Enter SAPID: ")
course = "B.Tech. CSE AI&ML"

m1 = int(input("PDS Marks: "))
m2 = int(input("Python Marks: "))
m3 = int(input("Chemistry Marks: "))
m4 = int(input("English Marks: "))
m5 = int(input("Physics: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5
cgpa = percentage / 10

if 9.1 <= cgpa <= 10: grade = "O"
elif 8.1 <= cgpa <= 9: grade = "A+"
elif 7.1 <= cgpa <= 8: grade = "A"
elif 6.1 <= cgpa <= 7: grade = "B+"
elif 5.1 <= cgpa <= 6: grade = "B"
elif 3.5 <= cgpa <= 5: grade = "C+"
else: grade = "F"

print(f"\nName: {name}\nRoll Number: {roll} SAPID: {sap}")
print(f"Course: {course}\n" + "-"*20)
print(f"Percentage: {percentage}%")
print(f"CGPA: {cgpa} | Grade: {grade}")