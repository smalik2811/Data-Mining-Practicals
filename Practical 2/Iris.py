class Iris:
    AllowedSpecies = [ "setosa", "versicolor", "virginica"]

    def __init__(self, SepalLenght, SepalWidth, PetalLength, PetalWidth, Species):
    
        self.sepalLength = SepalLenght
        self.sepalWidth = SepalWidth
        self.petalLength = PetalLength
        self.petalWidth = PetalWidth
        self.species = Species    

    def isComplete(self):
        try:
            self.sepalLength = float(self.sepalLength)
            self.sepalWidth = float(self.sepalWidth)
            self.petalLength = float(self.petalLength)
            self.petalWidth = float(self.petalWidth)
            self.species in self.AllowedSpecies
            return True
        except:
            return False

    def cleanData(self):
        if type(self.sepalLength) is not float:
            self.sepalLength = "NA"
        if type(self.sepalWidth) is not float:
            self.sepalWidth = "NA"
        if type(self.petalLength) is not float:
            self.petalLength = "NA"
        if type(self.petalWidth) is not float:
            self.petalWidth = "NA"
        if self.species not in self.AllowedSpecies:
            self.species = "NA"

    def checkConstraints(self):
        result = [0,0,0,0,0]

        if self.species not in self.AllowedSpecies:
            result[0] = 1

        if self.petalLength < 0 or self.petalWidth < 0 or self.sepalLength < 0 or self.sepalWidth < 0:
            result[1] = 1
        
        if self.petalLength < 2 * self.petalWidth:
            result[2] = 1

        if self.sepalLength > 30:
            result[3] = 1
        
        if self.sepalLength <= self.petalLength:
            result[4] = 1

        return result

    def __str__(self) -> str:
        return "{},{},{},{},\"{}\"\n".format(self.sepalLength, self.sepalWidth, self.petalLength, self.petalWidth, self.species)