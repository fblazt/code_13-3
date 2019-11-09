import json

class list_school:
    def __init__(self, name, year_in, year_out, major):
        self.name = name
        self.year_in = year_in
        self.year_out = year_out
        self.major = major

Firman = list_school("Firman", 2018, 2019, "Sistem Informasi")

class skills:
    def __init__(self, skill_name, level):
        self.skill_name = skill_name
        self.level = level
        
skill1 = skills("Python", "Beginner")
skill2 = skills("Figma", "Beginner")

def biodata(name, age):
    return {
        "name" : "Firman",
        "age" : 20,
        "address" : "Jl. Medayu Utara XXX-C No.33",
        "hobbies" : ["Fotografi", "Desain", "Coding"],
        "is_married" : False,
        "list_school" : [Firman.name, Firman.year_in, Firman.year_out, Firman.major],
        "skills" : [skill1.skill_name, skill1.level, skill2.skill_name, skill2.level],
        "interest_in_coding" : True
    }

result = json.dumps(biodata("Firman", 20))
print(result)