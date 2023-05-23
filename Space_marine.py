import random


ultramarine_names = [
    "Marneus Calgar",
    "Cato Sicarius",
    "Uriel Ventris",
    "Aeonid Thiel",
    "Agemman",
    "Tigurius",
    "Aethon",
    "Avitus",
    "Tiberius",
    "Galenus",
    "Octavian",
    "Severus",
    "Cassian",
    "Valerian",
    "Corvin",
    "Decimus",
    "Lucian",
    "Lucius",
    "Maximus",
    "Gaius",
    "Marius",
    "Titus",
    "Felix",
    "Lucullus",
    "Decius",
    "Pertinax",
    "Valentinian",
    "Gaius Julius",
    "Theodoric",
    "Aurelius",
    "Quintus",
    "Rufus",
    "Castor",
    "Cincinnatus",
    "Didius",
    "Fabian",
    "Gracchus",
    "Hadrian",
    "Horatius",
    "Julius",
    "Justinian",
    "Marcellus",
    "Marcus",
    "Nero",
    "Ovidius",
    "Publius",
    "Remus",
    "Scipio",
    "Seneca",
    "Sulla",
    "Tacticus",
    "Valerius",
    "Vespasian",
    "Virgil",
    "Xerxes",
    "Zephyrus",
    "Aelian",
    "Alaric",
    "Antares",
    "Aquilon",
    "Archimedes",
    "Arcturus",
    "Ares",
    "Argus",
    "Asmodeus",
    "Aurum",
    "Bellerophon",
    "Calibos",
    "Castellan",
    "Centurion",
    "Chromius",
    "Corvus",
    "Crassus",
    "Decimus Maximus",
    "Dominus",
    "Draco",
    "Drusus",
    "Eleutherios",
    "Emilian",
    "Equinox",
    "Fabius",
    "Falkus",
    "Ferox",
    "Gallus",
    "Garro",
    "Gideon",
    "Gorgon",
    "Gravitas",
    "Hector",
    "Helios",
    "Ignatius",
    "Inquisitorius",
    "Janus",
    "Javelin",
    "Jupiter",
    "Justus",
    "Kestros",
    "Korax",
    "Leonidas",
    "Libertas",
    "Lysander",
    "Magnus",
    "Marcellian",
    "Maximilian",
    "Mortifer",
    "Nemesis",
    "Nemean",
    "Nocturnus",
    "Octavianus",
    "Orpheus",
    "Paladin",
    "Patricius",
    "Pentheus",
    "Phoebus",
    "Placidus",
    "Prometheus",
    "Proteus",
    "Pyrrhus",
    "Quirinus",
    "Radamanthys",
    "Ragnar",
    "Remulus",
    "Romulus",
    "Sanguinius",
    "Scarius",
    "Scipionis",
    "Septimus",
    "Seraphim",
    "Silvanus"]

class Day:
    def __init__(self,number):
        self.day = int(number)
        self.missions = [generate_mission(number),generate_mission(number),generate_mission(number)]

class Company:
    def __init__(self,company_roster,location):
        self.location = location
        self.roster = company_roster
        self.captain = company_roster[0][0]
    def print_company(self):
        print_company(self.roster)
        

class SpaceMarine:
    def __init__(self, name, rank):
        if rank == "Captain":
            self.name = name
            self.rank = rank
            self.int = random.randint(40, 60)
            self.stg = random.randint(40, 60)
            self.end = random.randint(40, 60)
            self.char = random.randint(40, 60)
            self.psi = random.randint(-800, 10)
            self.ws = random.randint(40, 60)
            self.bs = random.randint(40, 60)
            self.talent = random.randint(10, 100)
        elif rank == "Lieutenant":
            self.name = name
            self.rank = rank
            self.int = random.randint(30, 40)
            self.stg = random.randint(30, 40)
            self.end = random.randint(30, 40)
            self.char = random.randint(20, 40)
            self.psi = random.randint(-800, 10)
            self.ws = random.randint(20, 40)
            self.bs = random.randint(20, 40)
            self.talent = random.randint(5, 100)
        else:
            self.name = name
            self.rank = rank
            self.int = random.randint(10, 30)
            self.stg = random.randint(10, 30)
            self.end = random.randint(10, 30)
            self.char = random.randint(10, 30)
            self.psi = random.randint(-800, 10)
            self.ws = random.randint(10, 30)
            self.bs = random.randint(10, 30)
            self.talent = random.randint(0, 100)

    def __str__(self):
        return f"{self.rank} {self.name}"

def generate_mission(number):
    #generates a random mission
    mission = []
    mission = [random.randint(1,100),random.randint(1,100),random.randint(1,10)]
    return mission


def generate_tenth():
    tenth_company = [[], [], [], [], [], [], [], [], []]
    command = []

    for squad in tenth_company:
        for i in range(0, 10):
            if i == 0:
                squad.append(SpaceMarine(random.choice(ultramarine_names),"Scout Sergent"))
            else:
                squad.append(SpaceMarine(random.choice(ultramarine_names),"Scout"))

    for i in range(0,3):
        if i == 0:
            command.append(SpaceMarine(random.choice(ultramarine_names),"Captain"))
        else:
            command.append(SpaceMarine(random.choice(ultramarine_names),"Lieutenant"))

    tenth_company.insert(0,command)
    
    return tenth_company

def generate_battle_company():
    company = [[],[], [], [], [], [], [], [], [], []]
    command = []
    troop_role = 0

    for squad in company:
        if troop_role == 0:
            for i in range(0,3):
                if i == 0:
                    squad.append(SpaceMarine(random.choice(ultramarine_names),"Captain"))
                else:
                    squad.append(SpaceMarine(random.choice(ultramarine_names),"Lieutenant"))
            troop_role += 1
        elif troop_role in [1,2,3,4,5]:
            for i in range(0, 10):
                if i == 0:
                    squad.append(SpaceMarine(random.choice(ultramarine_names),"Tactical Sergent"))
                else:
                    squad.append(SpaceMarine(random.choice(ultramarine_names),"Tactical Marine"))
            troop_role += 1
        elif troop_role in [6,7]:
            for i in range(0, 10):
                if i == 0:
                    squad.append(SpaceMarine(random.choice(ultramarine_names),"Assault Sergent"))
                else:
                    squad.append(SpaceMarine(random.choice(ultramarine_names),"Assault Marine"))
            troop_role += 1
        else:
            for i in range(0, 10):
                if i == 0:
                    squad.append(SpaceMarine(random.choice(ultramarine_names),"Devestator Sergent"))
                else:
                    squad.append(SpaceMarine(random.choice(ultramarine_names),"Devestator Marine"))
            troop_role += 1

    
    return company

# Printing the tenth company squads
def print_company(company):
    print("---------------------")
    for i, squad in enumerate(company):
        print(f"Squad {i + 1}:")
        for marine in squad:
            print(marine)
        print()

def main():
    tenth_company = Company(generate_tenth(),(0,0))
    second_company = Company(generate_battle_company(),(0,0))
    chapter = [second_company,tenth_company]
    current_day = 1

    while current_day <= 100:
        current_day = Day(current_day)
        print(current_day.missions)
        cheese = input("what the dog doin'")


main()
