
# Dette er det samme som...
tall = []
for i in range(10):
    tall.append(i)

# Dette!
tall = [i for i in range(10)]

# Kan også lage 2D-liste:
matrise = [[i for i in range(10)] for _ in range(10)]

# Slicing:
print(matrise[4:][2:5])

tall = [[1, 2], [3, 4]]

