# a. Default Argument: 'msg' has a pre-set value if not provided
def greet(name, msg="Good Morning"):
    print(f"Hello {name}, {msg}")

# b. Keyword Argument: Order doesn't matter if names are used
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}")

# c. Variable length argument (*args): Accepts any number of inputs
def sum_all(*numbers):
    return sum(numbers)

# Examples
print("--- Default Argument ---")
greet("Nikunj") 

print("\n--- Keyword Argument ---")
describe_pet(pet_name="Woody", animal_type="Hamster")

print("\n--- Variable Length Argument ---")
print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 5, 10, 15, 20: {sum_all(5, 10, 15, 20)}")