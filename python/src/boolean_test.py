a = set()
print(a)

a.add(1)
print(a)

a.add(2)

for x in a:
    print(x)

given_list1 = [1, 1, 2, 4, 2]

new_set1 = set()

for x in given_list1:
    new_set1.add(x)

print(new_set1)

given_list2 = [1, 3, 4, 1, 3]
new_set2 =set()
total = 0

for x in given_list2:
    new_set2.add(x)
for x in new_set2:
    total += x
total = sum(new_set2)

print(total)