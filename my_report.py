# name = input('请输入您的姓名：')
# gender = input('请输入您的性别：')
# age= input('请输入您的年龄：')
# university = input('请输入您的学校：')
# print('正在生成您的简历......\n')
# import time
# time.sleep(3)
# print('*'*30)
# print('简历'.center(30,'\000')+'\n')
# print('姓名：' + '\t' + name)
# print('性别：' + '\t' + gender)
# print('年龄：' + '\t' + age)
# print('学校：' + '\t' + university)
# print('*'*30)

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