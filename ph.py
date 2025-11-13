print("Welcome to the pH Analyzer Game!")
print("Enter the name of a solution to find its approximate pH value.\n")

solutions = {
    "lemon juice": 2.0,
    "vinegar": 3.0,
    "milk": 6.5,
    "water": 7.0,
    "soap": 9.0,
    "bleach": 12.0,
    "coffee": 5.0,
    "blood": 7.4
}

name = input("Enter a solution name: ")

if name in solutions:
    ph = solutions[name]
    print("\npH of", name, "is approximately", ph)
    if ph < 7:
        print("It is acidic in nature.")
    elif ph == 7:
        print("It is neutral in nature.")
    else:
        print("It is basic in nature.")
else:
    print("That solution is not in the list.")
    print("Try: lemon juice, vinegar, milk, water, soap, bleach, coffee, blood.")

print("Thanks for using the pH Analyzer!")
