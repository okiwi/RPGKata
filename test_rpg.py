

class Character:
    def __init__(self):
        self.damage_taken = 0
        self.max_health = 1000
        self.health = self.max_health
        
    @property
    def is_alive(self) -> bool:
        return self.health > 0

    @property
    def level(self) -> int:
        return self.damage_taken // 1000 + 1
    
    def attack(self, targeted_character: Character, damage: int):
        if targeted_character is self:
            print("PLEASE DO NOT HARM YOURSELF")
            return
        targeted_character.health = max(targeted_character.health - damage,0)
        targeted_character.damage_taken += damage
            

    def heal(self, health: int):
        self.health = min(self.health + health, self.max_health)

def test_character_exists():

    character = Character()

    assert character.health == 1000
    assert character.is_alive
    assert character.level == 1

def test_character_takes_damage():

    character1 = Character()
    character2 = Character()

    character1.attack(character2, 500)

    assert character2.health == 500
    assert character2.is_alive


def test_character_dies_after_damage():

    character1 = Character()
    character2 = Character()

    character1.attack(character2, 1000)

    assert character2.health == 0
    assert not character2.is_alive

def test_character_dead_has_health_zero():

    character1 = Character()
    character2 = Character()

    character1.attack(character2, 1500)

    assert character2.health == 0

def test_is_character_healed_correctly():
    
    character1 = Character()
    character2 = Character()

    character1.attack(character2, 500)
    character2.heal(1000)

    assert character2.health == 1000

def test_leveling_up():

    character1 = Character()
    character2 = Character()

    character1.attack(character2, 500)
    character2.heal(1000)
    character1.attack(character2, 500)
    
    assert character2.level == 2

def test_character_cant_hurt_self():
    # arrange
    character1 = Character()
    # act
    character1.attack(character1, 500)
    # assert
    assert character1.health == 1000 # you can't attack yourself

