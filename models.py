from dataclasses import dataclass

@dataclass
class Team:

    name: str
    matches: int
    wins: int
    losses: int
    runs_scored: int
    overs_faced: float
    runs_conceded: int
    overs_bowled: float

    def points(self):

        return self.wins * 2
