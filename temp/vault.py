#1 idea of a vault
class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0 ): # currency in wizardry: Galleon=17 Sickles, 1 Sickle=29 Knuts
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts"

potter = Vault(100, 50, 25)
print(potter) # call __str__

weasley = Vault(25, 50, 100)
print(weasley) # call __str__

# other by convention : int + int same as Vault + Vault
# potter = self, weasley = other