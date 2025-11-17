class Item:
    def __init__(self, name, short, weight, value):
        self.name = name
        self.short = short
        self.weight = weight
        self.value = value

    def __repr__(self):
        return self.short


items = [
    Item("rifle", "r", 3, 25),
    Item("pistol", "p", 2, 15),
    Item("ammo", "a", 2, 15),
    Item("medkit", "m", 2, 20),
    Item("inhaler", "i", 1, 5),
    Item("knife", "k", 1, 15),
    Item("axe", "x", 3, 20),
    Item("talisman", "t", 1, 25),
    Item("flask", "f", 1, 15),
    Item("antidote", "d", 1, 10),
    Item("supplies", "s", 2, 20),
    Item("crossbow", "c", 2, 20)
]

capacity = 9
required = "i"



max_value = -1000
best_choice = []


def backtrack(i, items_, weight, value):
    global max_value, best_choice
    
    if weight > capacity:
        return 0
    
    required_ = any(i.short == required for i in items_)

    if required_ and value > max_value:
        max_value = value
        best_choice = items_.copy()
        

    if i == len(items):
        return 0

    backtrack(i + 1, items_, weight, value)

    item = items[i]
    items_.append(item)

    backtrack(i + 1,
              items_,
              weight + item.weight,
              value + item.value)

    items_.pop()



backtrack(0, [], 0, 0)

inventory = [[" " for _ in range(3)] for _ in range(3)]

l = []
for it in best_choice:
    l += [it.short] * it.weight


index = 0
for r in range(3):
    for c in range(3):
        inventory[r][c] = l[index]
        index += 1

for i in best_choice:
    items.remove(i)
s = 0
for i in items:
    s += i.value


for row in inventory:
    print(row)
print()
print("Итоговые очки выживания:", max_value - s)
