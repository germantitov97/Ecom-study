# start
i = 0
i_old = 0
while True:
    age = int(input("type age: "))
    if age < 12:
        print('too young +12 only')
        continue
    if age > 18:
        print('too old +18 not allowed')
        break
    else:
        i = i + 1
    if age >= 16:
        i_old += 1
    if i == 5:
        break
print('total of', i, 'players')
print('player in 16-18 age are: ',i_old,)

# stop














