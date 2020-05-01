fin = open('input.txt', 'r', encoding='utf8')
fon = open('output.txt', 'w', encoding='utf8')
lines = fin.readlines()
lines.sort()
for i in lines:
    print(*i.split()[:2] + i.split()[3:], file=fon)
fin.close()
fon.close()
