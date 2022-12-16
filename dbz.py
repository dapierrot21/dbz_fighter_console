class Fighter:
    def __init__(self, fighter_name, level):
        self.fighter_name = fighter_name
        self.level = level
        self.stanima = 8
        self.max_health = level * 7
        self.cant_fight = False

    def __repr__(self):
        print("Your fighter is {name} with a power level of {level} and hp bar of {max_health}.".format(
            name=self.fighter_name, level=self.level, max_health=self.max_health))

    def senzu_bean(self):
        # Only a fight that can't fight use a senzu bean so ca fight is switch to False when called.
        self.cant_fight = False
        if self.max_health == 0:
            self.max_health = 15
            print("{name} can fight some more now!".format(
                name=self.fighter_name))

    def can_still_fight(self):
        self.cant_fight = True
        if self.max_health != 0:
            self.max_health = 0
            print("{name} is down and can not fight.".format(
                name=self.fighter_name))

    def attack(self, other_fighter):
        if self.cant_fight:
            print("{name} is knocked down.".format(name=self.fighter_name))

        if self.stanima == 0:
            print("{name} does not have any stanima to attack right now.".format(
                name=self.fighter_name))
        else:
            print("{name} attacked {other_fighter} for this much {damage} damage.".format(
                name=self.fighter_name, other_fighter=other_fighter.fighter_name, damage=other_fighter.max_health - 80))
            other_fighter.max_health -= 80
            self.stanima -= 2

    def block(self, other_fighter):
        if self.cant_fight:
            print("{name} is knocked down.".format(name=self.fighter_name))

        if self.stanima == 0:
            print("{name} does not have any stanima to block right now.".format(
                name=self.fighter_name))
        else:
            print("{name} blocked {other_fighter} for a decrease in this much {damage} damage.".format(
                name=self.fighter_name, other_fighter=other_fighter.fighter_name, damage=other_fighter.max_health + 30))
            other_fighter.max_health += 30
            self.stanima -= 1


class Player:

    def __init__(self, list_of_fighters, name):
        self.name = name
        self.fighters = list_of_fighters
        self.current_fighter = 0
        self.player_senzu_bean = 3
        self.add_stanima = 3

    def __repr__(self):
        print("The player {name} has the following fighters".format(
            name=self.name))

        for fighter in self.fighters:
            print(fighter.fighter_name)

        return "The current active fighter is {name}".format(name=self.fighters[self.current_fighter].fighter_name)

    def use_senzu_bean(self):
        if self.player_senzu_bean != 0:
            print("{name} just receieved a senzu bean!".format(
                name=self.fighters[self.current_fighter].fighter_name))
            self.fighters[self.current_fighter].senzu_bean()
            self.player_senzu_bean -= 1
        else:
            print("You have no more senzu beans my friend.")

    def use_stanima(self):
        if self.add_stanima != 0:
            print("{name} just recieved stanima to attack.".format(
                name=self.fighters[self.current_fighter].fighter_name))
            self.fighters[self.current_fighter].stanima += 1
        else:
            print("You dont have anything stanima to give.")

    def attack_your_enemy(self, other_player):
        my_fighter = self.fighters[self.current_fighter]
        my_enemy = other_player.fighters[other_player.current_fighter]
        my_fighter.attack(my_enemy)

    def block_your_enemy(self, other_player):
        my_fighter = self.fighters[self.current_fighter]
        my_enemy = other_player.fighters[other_player.current_fighter]
        my_fighter.block(my_enemy)


print("Welcome to Dragonball Z Console Fighters!!!")
print("\n")
print("Now let\'s pick our players!!!")

player1 = input("What is your name player one?")
player2 = input("What is your name player two?")

print("We have {player1} vs {player2}.".format(
    player1=player1, player2=player2))
print("\n")
print("Now it\'s to select your champions!!!!")

goku = Fighter("Goku", 1100)
vegeta = Fighter("Vegeta", 1009)
frieza = Fighter("Frieza", 1104)
gohan = Fighter("Gohan", 850)
piccolo = Fighter("Piccolo", 790)
jiren = Fighter("Jiren", 1250)

player_one_fighters = []
player_two_fighters = []


choice = input(
    "Player 1 do you want Goku or Vegeta? The other will go to Player 2.")

if choice == "Goku":
    player_one_fighters.append(goku)
    player_two_fighters.append(vegeta)
elif choice == "Vegeta":
    player_one_fighters.append(vegeta)
    player_two_fighters.append(goku)

choice = input(
    "Player 1 do you want Frieza or Gohan? The other will go to Player 2.")

if choice == "Frieza":
    player_one_fighters.append(frieza)
    player_two_fighters.append(gohan)
elif choice == "Gohan":
    player_one_fighters.append(gohan)
    player_two_fighters.append(frieza)


choice = input(
    "Player 1 do you want Piccolo or Jiren? The other will go to Player 2.")

if choice == "Piccolo":
    player_one_fighters.append(piccolo)
    player_two_fighters.append(jiren)
elif choice == "Jiren":
    player_one_fighters.append(jiren)
    player_two_fighters.append(piccolo)


player_one = Player(player_one_fighters, player1)
player_two = Player(player_two_fighters, player2)


print("\n")

print("No let\'s fight!!!!!!")

player_one.attack_your_enemy(player_two)
player_two.attack_your_enemy(player_one)
player_one.block_your_enemy(player_two)
player_two.block_your_enemy(player_one)
player_one.use_senzu_bean()
player_two.use_stanima()
