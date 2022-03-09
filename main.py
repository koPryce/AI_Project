from pyswip import Prolog

prolog = Prolog()

prolog.consult("AI_Project.pl")

c = list(prolog.query("faster(What,dog)"))

print(c)

