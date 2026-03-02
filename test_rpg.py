

class Character:
    def __init__(self):
        self.health = 1000
        
    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def attack(self, targeted_character: Character, damage: int):
        targeted_character.health = max(targeted_character.health - damage,0)

def test_characterExist():

    character = Character()

    assert character.health == 1000
    assert character.is_alive

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