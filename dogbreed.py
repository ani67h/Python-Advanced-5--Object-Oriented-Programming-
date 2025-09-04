class Dog:
    animal = "dog"
    character = "loyal, playful and friendly"

    def __init__(self, ty_pe="", color="", character = ""):
        self.ty_pe = ty_pe
        self.color = color
        self.character = character

    def n_us(self):
        self.nus1 = "American Pit Bull Terrier"
        self.nus2 = "Boston Terrier"
        self.nus3 = "Alaskan Malamute"
        self.nus4 = "American Cocker Spaniel"
        self.nus5 = "Chihuahua"

    def eu(self):
        self.eu1 = "German Shepherd"
        self.eu2 = "Golden Retriever"
        self.eu3 = "Bull"
        self.eu4 = "Rottweiler"
        self.eu5 = "Dalmatian"

    def nus_color(self):
        self.nus1_color = "brindle"
        self.nus2_color = "black"
        self.nus3_color = "grey"
        self.nus4_color = "golden"
        self.nus5_color = "fawn"

    def eu_color(self):
        self.eur_color1 = "tan"    
        self.eur_color2 = "golden"    
        self.eur_color3 = "fawn"    
        self.eur_color4 = "black"    
        self.eur_color5 = "white"

    def output(self):
        print("\n",self.nus1, Dog.animal, "is", self.nus1_color, "colored and it is very", Dog.character,"\n")
        print(self.nus2, Dog.animal, "is", self.nus2_color, "colored and it is very", Dog.character,"\n")
        print(self.nus3, Dog.animal, "is", self.nus3_color, "colored and it is very", Dog.character,"\n")
        print(self.nus4, Dog.animal, "is", self.nus4_color, "colored and it is very", Dog.character,"\n")
        print(self.nus5, Dog.animal, "is", self.nus5_color, "colored and it is very", Dog.character,"\n")
        print(self.eu1, Dog.animal, "is", self.eur_color1, "colored and it is very", Dog.character,"\n")
        print(self.eu2, Dog.animal, "is", self.eur_color2, "colored and it is very", Dog.character,"\n")
        print(self.eu3, Dog.animal, "is", self.eur_color3, "colored and it is very", Dog.character,"\n")
        print(self.eu4, Dog.animal, "is", self.eur_color4, "colored and it is very", Dog.character,"\n")
        print(self.eu5, Dog.animal, "is", self.eur_color5, "colored and it is very", Dog.character,"\n")


d1 = Dog()
d1.n_us()
d1.eu()
d1.nus_color()
d1.eu_color()
d1.output()
