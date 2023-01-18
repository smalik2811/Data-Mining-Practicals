class People:
    def __init__(self, age, ageGroup, height, status, yearsMarrried):
        self.age = int(age)
        self.ageGroup = ageGroup
        self.height = float(height)
        self.status = status
        self.yearsMarried = int(yearsMarrried)

    def validateE(self):
        allowed_married_status = ["married", "single", "widowed"]

        if self.age < 0 or self.age > 150:
            return False

        if self.age <= self.yearsMarried:
            return False
        
        if not self.status in allowed_married_status:
            return False

        if self.age > 18 and self.ageGroup == "child":
            return False
        
        if self.age >= 18 and self.age <= 65 and not self.ageGroup == "adult":
            return False

        if self.age < 65 and self.ageGroup == "elderly":
            return False
        
        return True