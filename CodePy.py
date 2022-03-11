
users=[]
n=int(input('Enter users count: '))
for i in range(n):
 d={}
 d['name']=input('Enter username: ')
 d['age']=input('Enter userage: ')
 users.append(d)
name=input('Enter name to search: ')
for j in range(n):
 if users[j]['name']==name:
  print(users[j]['age'])
  break
 else:
  print('there is no user with given name!')
  