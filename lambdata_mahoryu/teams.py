# example teams.py (functional approach)

class Team():
    def __init__(self, name, city):
        self.name = name
        self.city = city

def advertise(my_team):
    print(f"HEY COME TO {my_team['city'].upper()} TO SEE OUR GAMES!!!")

def full_name(my_team):
    return f"{my_team['city']} {my_team['name']}"

if __name__ == "__main__":
    # teams = [
    #     {"city": "New York", "name": "Yankees"},
    #     {"city": "New York", "name": "Mets"},
    #     {"city": "Boston", "name": "Red Sox"},
    #     {"city": "New Haven", "name": "Ravens"},
    #     {"city": "Washington", "name": "Nationals"}
    # ]
    # for team in teams:
    #     print("-------")
    #     print(full_name(team))
    #     advertise(team)

    team = Team(name="Wizard", city="Washington")  # initialize
    print(team)
    print(type(team))
    print(team.name)  # invoking attributes
    print(team.city)  # invoking attributes

    team2 = Team(name="Giants", city="New York")  # initialize
    print(team2)
    print(type(team2))
    print(team2.name)  # invoking attributes
    print(team2.city)  # invoking attributes