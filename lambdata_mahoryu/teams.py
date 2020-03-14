# example teams.py (OOP approach)

class Team():
    def __init__(self, name, city, players="Player 1"):
        self.name = name
        self.city = city
        self.players = players

    def advertise(self):
        print(f"HEY COME TO {self.city.upper()} TO SEE OUR GAMES!!!")

    def full_name(self):
        print(f"{self.city} {self.name}")

class BaseballTeam(Team):
    def __init__(self, name, city, players="Player 1", starting_pitcher="PITCHER"):
        super().__init__(name, city, players)
        self.starting_pitcher = starting_pitcher

    def advertise(self):
        print(f"HEY COME TO {self.city.upper()} TO SEE OUR PITCHER "
              f"{self.starting_pitcher}!!!")

if __name__ == "__main__":

    football_team = Team("Cowboys","Dallas")
    football_team.full_name()

    teams = [
        {"city": "New York", "name": "Yankees", "pitcher": "John"},
        {"city": "New York", "name": "Mets", "pitcher": "Jane"},
        {"city": "Boston", "name": "Red Sox", "pitcher": "Ames"},
        {"city": "New Haven", "name": "Ravens", "pitcher": "Vishal"},
        {"city": "Washington", "name": "Nationals", "pitcher": "Cody"}
    ]
    for team_atributes in teams:
        team = BaseballTeam(name=team_atributes["name"], city=team_atributes["city"], starting_pitcher=team_atributes["pitcher"])
        print("-------")
        # print(full_name(team))
        # advertise(team)
        print(team.full_name())
        team.advertise()

    team = Team(name="Wizard", city="Washington")  # initialize
    # print(team)
    # print(type(team))
    print(team.name)  # invoking attributes
    print(team.city)  # invoking attributes

    team2 = Team(name="Giants", city="New York")  # initialize
    # print(team2)
    # print(type(team2))
    print(team2.name)  # invoking attributes
    print(team2.city)  # invoking attributes