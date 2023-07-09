import random
from utils import to_int

class NotEnoughPlayers(Exception):
    pass

class WereWolf:
    def __init__(self,players:list,num_of_role:list):
        self.players=players
        self.roles=["villager","fortune-teller","Psychic","knight","madman","werewolves"]
        self.num_role=to_int(num_of_role)
        self.players_role={}
        self._add_role()

    def _add_role(self):
        if sum(self.num_role)!=len(self.players):
            raise NotEnoughPlayers("The number of roles must be equal to the number of players.")
        else:
            for i in enumerate(self.roles):
                role=i[1]
                num=self.num_role[i[0]]
                for j in range(num):
                    rp=random.choice(self.players)
                    if not role in self.players_role:
                        self.players_role[role]=[rp]
                    else:
                        self.players_role[role].append(rp)
                    self.players.remove(rp)

werewolf=WereWolf(["a","b","c","d","e","f","g"],[2,1,1,1,1,1])
print(werewolf.players_role)