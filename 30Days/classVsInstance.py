class Person:
    age = 0
    def __init__(self,initialAge):
        
        # Add some more code to run some checks on initialAge
        if initialAge<0:
            print("Age is not valid, setting age to 0.")
            age=0
        else:
            age=initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if age>17:
            print("You are old.")
        elif age<13:
            print("You are young.")
        else:
            print("You are a teenager.")
    def yearPasses(self):
        # Increment the age of the person in here
        global age
        age += 1