# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

s1 = input()
s2 = input()

for i in range(len(s1)):
    if ord(s1[i].lower()) <  ord(s2[i].lower()):
        print(-1)
        break
    elif ord(s1[i].lower()) >  ord(s2[i].lower()):
        print(1)
        break
else:
    print(0)