collection = []
common = []
while True:
    field = input()
    if field != "end" and field not in collection:
        collection.append(field)
    if field == "end":
        break
for i in range(len(collection)):
    print(collection[i])
