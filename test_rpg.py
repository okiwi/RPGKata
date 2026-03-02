

class Character:
    def __init__(self):
        self.health = 1000



def test_characterExist():

    character = Character()

    assert character.health == 1000
    