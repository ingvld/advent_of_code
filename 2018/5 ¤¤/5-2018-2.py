import re

def react_polymer(polymer):
    reacted = True

    while reacted:
        reacted = False

        post_reaction_polymer = ''

        i = 0
        while i < len(polymer)-1:
            if polymer[i].swapcase() == polymer[i+1]:
                reacted = True
                i += 2
            else:
                post_reaction_polymer += polymer[i]
                i += 1
        
        if i == len(polymer)-1:
            post_reaction_polymer += polymer[-1]

        polymer = post_reaction_polymer

    return len(polymer)


original_polymer = open('5-input').readline()

uniqueunits = set()

for unit in original_polymer:
    uniqueunits.add(unit.lower())

shortest_polymer = len(original_polymer)

for unit in uniqueunits:
    reacted_length = react_polymer(original_polymer.replace(unit,'').replace(unit.upper(),''))
    if reacted_length < shortest_polymer:
        shortest_polymer = reacted_length

print(shortest_polymer)