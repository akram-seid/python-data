x = "9.2.25.    Variety:     Melkam (WSV 387)"
xx = ""
for i in range(len(x)):
    if (x[i].isdigit() or x[i] == ".") and (x[i+1] != " "):
        print("**"+x[i+1])
        x = x.replace(x[i], '^')
for i in x:
    if i != "^":
        xx += i
xx = xx.split(" ")
for i in xx:
    if i != "":
        print(i, end=" ")
