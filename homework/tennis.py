from human import Human
class Tennis:
    def __init__(self, skill = None, rang = None):
        self.Skill = skill
        self.Rang = rang
    def __str__(self):
        return f"Skill - {self.Skill}\n" \
               f"Rang - {self.Rang}\n"
