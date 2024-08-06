num = 0
while True:
    is_bullying = False
    n = int(input())
    num += 1
    
    if n == 0:
        break
        
    people_list = []
    for i in range(n):
        paper = list(input().split(' '))
        people_list.append(paper)

    print(f"Group {num}")
    for i in range(n):
        target = people_list[i]
        for j in range(n):
            if target[j] == "N":
                is_bullying = True
                print(f"{people_list[(n + i - j)%n][0]} was nasty about {target[0]}")
    if not is_bullying:
        print("Nobody was nasty")
    print()

"""
c=1
while n:=int(input()):
 print('Group',c)
 r,f=[input().split()for _ in range(n)],1
 for i in range(n):
  for j in range(1,n):
   if r[i][j]=='N':f=0;print(r[i-j][0],'was nasty about',r[i][0])
 if f:print('Nobody was nasty')
 c+=1
 print()
 """
