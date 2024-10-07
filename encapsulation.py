class village:
    def __init__(self):
        self.village_name = "kottamarudur"
        self.num_of_male = "2000"
        self.num_of_female = "1800"
        self.num_of_aged_people = "300"
        self.migrated_people = "150"
village1=village()
print(village1.village_name)
print(village1.num_of_male)
print(village1.num_of_female)
print(village1.__num_of_aged_people)
print(village1.__migrated_people)
