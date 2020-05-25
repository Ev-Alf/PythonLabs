def chastota(lang,path):
    with open(path, "r") as file:
        text = file.read().lower()
        dtext = {i:text.count(i) for i in lang}
        for i in sorted(dtext.items(),key = lambda i: i[1],reverse=True):
            print(i[0],"-",round(i[1]/len(dtext),2),"%")

eng = "qwertyuiopasdfghjklzxcvbnm"
rus = "ёйцукенгшщзхъфывапролджэячсмитьбю"
chastota(eng,"Ex1E.txt")
print("===============")
chastota(rus,"Ex1R.txt")
