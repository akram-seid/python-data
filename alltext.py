import glob

txt_files = glob.glob("large/*.txt")

a = []
for i in range(len(txt_files)):
    with open(txt_files[i], "r") as fi:
        for x in fi:
            a.append(x.strip('\n'))

z = set([x for x in a if a.count(x) > 4])
final = list(z)
final.sort()
for i in range(len(final)):
    print(final[i])

