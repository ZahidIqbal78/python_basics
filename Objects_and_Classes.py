print("----------------------------------------")

class class1:
    classVariable = "value of class variable"

    def class1Function(self):
        print("This function is inside a class.")


anObject = class1()

#anObject.classVariable
print('1 ' + anObject.classVariable)

print(anObject.class1Function())


#lest change the value of the variable in class1
anObject.classVariable = "yabbbbaaa daaabbba doooo"
print('3 ' + anObject.classVariable)