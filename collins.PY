class Neighbor:
    def __init__(self, name, age, height, skin_color, character, education):
        self.name = name
        self.age = age
        self.height = height
        self.skin_color = skin_color
        self.character = character
        self.education = education

    def describe(self):
        print(f"--- Neighbour's Details: {self.name} ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years old")
        print(f"Height: {self.height}")
        print(f"Skin Color: {self.skin_color}")
        print(f"Personality: He is {self.chacter}.")
        print(f"Educational Level: He have a {self.education} degree.")
        print("-" * (len(self.name) + 26))
my_neighbor = Neighbor(
       name="Collins Kimanzi",
       age=24,
       height="5'0",
       skin_color="dark",
       hobby="Hiking",
       education="Bachelor's Degree"
)
my_neighbor.describe()