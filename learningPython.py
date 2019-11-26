#1126 While循环作业
st = list('1948736495')
ou = []
ji = []
st_length = len(st)
i,j = 0,0
while i < st_length:
    if int(st[i]) % 2 != 0:
        ou.append(st[i])
        i = i + 1
    else:
        ji.append(st[i])
        i = i + 1
print(ou)
print('*'*20)
print(ji)