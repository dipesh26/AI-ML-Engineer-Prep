# Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
pet = str(input("Enter the species of your pet (Dog/Cat): ")).lower()
pet_age = int(input("Enter the age of your pet: "))

if pet == "dog":
    if pet_age < 2:
        print("Puppy food")
    else:
        print("Senior dog food")
elif pet == "cat":
    if pet_age < 2:
        print("kitten food")
    else:
        print("Senior cat food")