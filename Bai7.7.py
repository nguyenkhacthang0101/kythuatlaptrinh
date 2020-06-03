f = open('list1.txt')
f1 = open('output.txt','a')

copy = False

for line in f.readlines():
    if 'tests/filr/myworld' in line:
        copy = True
    if copy:
        f1.write(line)
f1.close
f.close
