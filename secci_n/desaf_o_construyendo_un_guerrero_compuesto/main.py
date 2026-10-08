class Weapon:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

class Warrior:
    def __init__(self, name):
        self.name = name
        self.weapon = None  # 1. Atributo para el arma

    def equip_weapon(self, weapon):
        self.weapon = weapon  # 2. Almacenar el arma

    def show_weapon(self):
        # 3. Mostrar arma o estado desarmado
        if self.weapon:
            print(f"{self.name} is holding a {self.weapon.name}")
        else:
            print(f"{self.name} is unarmed")

sword = Weapon("Sword", 5)
warrior = Warrior("Conan")

warrior.equip_weapon(sword)
warrior.show_weapon()