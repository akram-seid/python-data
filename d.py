x = "9.2.25.6    Variety:     Melkam (WSV 387)"
string = ""
for i in range(len(x)):
    if x[i].isdigit() and x[i + 1] == '.':
        string = (x[i + 2:])
        break
for i in range(len(string)):
    if string[i] == ' ' and string[i + 1] != ' ':
        string = (string[i + 1:])
        break
print(string)
