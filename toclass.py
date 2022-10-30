print('')
with open("string2.txt", "r") as fi:
    variety_txt = []
    fields = []
    string = ''
    for x in fi:
        for i in range(len(x)):
            if "" in x[i]:
                string = (x[i:])
                rows = string.split("")
                if rows[1] not in variety_txt:
                    variety_txt.append(rows[1])
    for j in range(len(variety_txt)):
        row2 = variety_txt[j].split(":")
        if row2[0].strip(" ") not in fields:
            fields.append(row2[0].strip(" "))
for i in range(len(fields)):
    print(fields[i])
