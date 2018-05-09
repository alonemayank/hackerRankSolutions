class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,fn,ln,idn,sc):
        self._fn=fn
        self._ln=ln
        self._idn=idn
        self._sc=sc

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def printPerson(self):
        print("Name: {}, {}".format(self._ln,self._fn))
        print("ID: {}".format(self._idn))
    
    def calculate(self):
        total=0
        for i in self._sc:
            total+=i
        score = total/len(self._sc)
        if score >= 90:
            return 'O'
        elif score >= 80:
            return 'E'
        elif score >=70:
            return 'A'
        elif score >= 55:
            return 'P'
        elif score >= 40:
            return 'D'
        else:
            return 'T'
         
    