print("----------------------------------------")

phonebook = {}
phonebook["person1"] = 123456789
phonebook["person2"] = 1123456789
print(phonebook)

#or

phonebook1 = {
    "person1" : 987654321,
    "person2" : 2345678
}
print(phonebook1)

#iteration
for name, number in phonebook.items():
    print("Name: %s; Number: %d" %(name, number))

#delete a value from dictionary
del phonebook["person1"]
print(phonebook)
#or
phonebook1.pop("person2")
print(phonebook1)

if "person1" in phonebook:
    print("Person1 is found in the phonebook")
else:
    print("Person1 is not found in phonebook")

