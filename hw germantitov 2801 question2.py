# start

while True:
    lower = int(input('lower value: '))
    higher = int(input('higher value: '))
    if higher <= lower:
        continue
    elif higher > lower:
        break
for _ in range(lower, higher + 1):
    print(_, end=' ')

# stop














