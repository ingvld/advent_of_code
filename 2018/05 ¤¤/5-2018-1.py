polymer = open('5-input').readline()

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

print(len(polymer))
