class Student:
    # Constructor to initialize details
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.marks = {"Physics": phy, "Chemistry": chem, "Maths": maths}

    # Method to display student details
    def display(self):
        print(f"\n--- Details for {self.name} ---")
        print(f"SAP ID: {self.sap_id}")
        print(f"Marks: {self.marks}")

    # Method to find marks percentage
    def find_marks_percentage(self):
        total_obtained = sum(self.marks.values())
        percentage = (total_obtained / 300) * 100
        return percentage

    # Method to display result (Pass/Fail)
    def display_result(self):
        # Assuming max marks per subject is 100
        # Pass if every subject > 40% (40 marks)
        passed = True
        for subject, score in self.marks.items():
            if score <= 40:
                passed = False
                break
        
        if passed:
            print("Status: PASS")
        else:
            print("Status: FAIL")

# Separate function to find average of the whole class
def find_class_average(student_list):
    if not student_list:
        return 0
    total_percentages = sum(s.find_marks_percentage() for s in student_list)
    return total_percentages / len(student_list)

# --- Execution ---
n = int(input("Enter number of students (n): "))
students_list = []

for i in range(n):
    print(f"\nEntering data for student {i+1}")
    name = input("Name: ")
    sap = input("SAP ID: ")
    p = float(input("Physics Marks: "))
    c = float(input("Chemistry Marks: "))
    m = float(input("Maths Marks: "))
    
    # Initializing student object
    obj = Student(name, sap, p, c, m)
    students_list.append(obj)

# Calling methods for each student
for s in students_list:
    s.display()
    print(f"Percentage: {s.find_marks_percentage():.2f}%")
    s.display_result()

# Finding class average
avg = find_class_average(students_list)
print(f"\n{'='*30}")
print(f"The Average Percentage of the Class is: {avg:.2f}%")
print('='*30)