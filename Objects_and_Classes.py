print("----------------------------------------")

class class1:
    classVariable = "value of class variable"

    def class1Function(self):
        print("This function is inside a class.")


anObject = class1()

#anObject.classVariable
print(anObject.classVariable)

print(anObject.class1Function())