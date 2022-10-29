with open("rows2.txt", "r") as fi:
    variety_txt = []
    rows = []
    main = []
    for x in fi:
        variety_txt.append(x)
        variety_txt.sort()
    for i in range(len(variety_txt)):
        rows.append(variety_txt[i].lower())
    for i in range(len(rows)):
        if rows[i] not in main:
            main.append(rows[i])
    for i in range(len(main)):
        print(main[i])
