# start
i = 0
highest_rate = 0
lowest_rate = 5
while i < 10:
    rate = int(input("rate the movie"))
    if rate > 5 or rate < 1:
        continue
    else:
        i = i + 1
    if rate >= highest_rate:
        highest_rate = rate
    if rate <= lowest_rate:
        lowest_rate = rate
print("The highest rate is", highest_rate)
print("The lowest rate is", lowest_rate)
# stop








