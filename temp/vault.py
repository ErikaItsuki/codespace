#1 idea of a vault
class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0 ): # currency in wizardry: Galleon=17 Sickles, 1 Sickle=29 Knuts
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    def __str__(self):
        return f"{self.galleons}"

potter = Vault(100, 50, 25)
print(potter)
weasley = Vault(25, 50, 100)
print(weasley)