
from pathlib import Path
p = Path.cwd()

p = p / "nom.txt"
print(p)

# p.touch()
# je l'ai rempli manuellement avec copier coller du git hub



with open(p, "r") as f:
    data = f.read().splitlines()
# print(data)

prenoms = []
for i in data:
    prenoms.extend(i.split())

# print(prenoms)

prenomFinal = [i.strip(",. ") for i in prenoms]

# print(prenomFinal)
with open(p, "w") as f:
    f.write("\n".join(sorted(prenomFinal)))


print(p.read_text())




