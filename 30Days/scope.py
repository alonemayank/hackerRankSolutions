# Add your code here
    def __init__(self,arr):
        self.__elements=arr
    
    def computeDifference(self):
        local = set(self.__elements)
        local = sorted(local)
        self.maximumDifference = abs(int(local[0])-int(local[len(local)-1]))