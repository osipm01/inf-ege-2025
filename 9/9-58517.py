
f = open("C:/Users/endoc/Documents/GitHub/inf-ege-2025/9/9-58517.txt", 'r')

cnt = 0
for s in f:
    a = list(map(int, s.split()))
    if a.count(min(a))==1:
        if len(a)!=len(set(a)):
            sr=((sum(a)-max(a))/5)*3
            if max(a)>sr:
                cnt+=1
print(cnt)