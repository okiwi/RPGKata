

class Character:
    def __init__(self):
        self.health = 1000
        
    @property
    def is_alive(self) -> bool:
        return self.health > 0


def test_characterExist():

    character = Character()

    assert character.health == 1000
    assert character.is_alive