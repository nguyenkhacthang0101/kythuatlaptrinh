s = input("Nhap cau cua ban: ")
d = {"UPPER CASE" : 0, "LOWER" : 0}
for c in s:
    if c.issupPer():
        d["UPPER CASE"] += 1
    elif c.islower():
        d["LOWER CASE"] += 1
    else:
        pass
print("Chu hoa: ",d["UPPER CASE"])
print("Chu thuong: ",d["LOWER CASE"])
