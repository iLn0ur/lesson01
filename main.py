time_in_sec = int(input("enter sec:"))
#time_in_sec = 9006100
correct_time = [time_in_sec % 60]
time_in_sec = time_in_sec // 60
if time_in_sec > 0:
    correct_time.append(time_in_sec % 60)
    time_in_sec = time_in_sec // 60

if time_in_sec > 0:
    correct_time.append(time_in_sec % 24)
    time_in_sec = time_in_sec // 24

if time_in_sec > 0:
    correct_time.append(time_in_sec)

time_list = ['sec', 'min', 'hours', 'days']

for i, el in reversed(list(enumerate(correct_time))):
    print(el, time_list[i], end=" ")

print()

# second task

list_cube = [i * i * i for i in range(1000) if i % 2]
final_sum = 0
for el in list_cube:
    sum_el = 0
    for i in str(el):
        sum_el += int(i)
    if not sum_el % 7:
        final_sum += el

print("final:", final_sum)

list_cube = [i + 17 for i in list_cube]
final_sum = 0
for el in list_cube:
    sum_el = 0
    for i in str(el):
        sum_el += int(i)
    if not sum_el % 7:
        final_sum += el

print("final:", final_sum)

# third task

list_percents = ["процент", "процента", "процентов"]

for i in range(1, 101):
    if (i > 5) and (i < 21):
        print(i, list_percents[2])
        continue
    elif i % 10 == 1:
        print(i, list_percents[0])
        continue
    elif (i % 10 > 1) and (i % 10 < 5):
        print(i, list_percents[1])
        continue
    else:
        print(i, list_percents[2])
