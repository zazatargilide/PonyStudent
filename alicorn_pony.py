class Pony:
    def __init__(self, name, surname, color, magic_type=None):
        self.name = name
        self.surname = surname
        self.fullname = self.name + " " + self.surname
        self.color = color
        self.magic_type = magic_type

class Pegasus(Pony):
    def __init__(self, name, surname, color, wings_material, wings_color, magic_type="Weather"):
        Pony.__init__(self, name, surname, color, magic_type)
        self.wings_material = wings_material
        self.wings_color = wings_color

class Unicorn(Pony):
    def __init__(self, name, surname, color, horn_shape, horn_color, magic_type="Telekinetic"):
        Pony.__init__(self, name, surname, color, magic_type)
        self.horn_shape = horn_shape
        self.horn_color = horn_color

class Alicorn(Pegasus, Unicorn):
    def __init__(self, name, surname, color, wings_material, wings_color, horn_shape, horn_color, magic_type="Powerful Magic"):
        Pegasus.__init__(self, name, surname, color, wings_material, wings_color, magic_type)
        Unicorn.__init__(self, name, surname, color, horn_shape, horn_color, magic_type)

twilight = Pony("Twilight", "Sparkle", "purple", "Friendship")
applejack = Pony("Applejack", "Apple", "orange")

rainbow_dash = Pegasus("Rainbow", "Dash", "blue", "feather", "rainbow", "Speed")
fluttershy = Pegasus("Fluttershy", "Meadow", "yellow", "feather", "pink", "Nature")

rarity = Unicorn("Rarity", "Belle", "white", "spiral", "blue", "Glamour")
starlight = Unicorn("Starlight", "Glimmer", "pink", "twist", "purple", "Time Travel")

princess_celestia = Alicorn("Celestia", "Regalia", "white", "feather", "gold", "spiral", "gold", "Sun Control")
princess_luna = Alicorn("Luna", "Eclipse", "navy blue", "feather", "silver", "curved", "silver", "Moon Control")
princess_cadence = Alicorn("Cadence", "Heart", "pink", "feather", "gold", "straight", "blue", "Love")

