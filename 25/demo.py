# решение каскадными циклами методом набора числа из цифр

# # 1?2157*4 до 10 в степени  10

a = ['','0','1','2', '3', '4', '5', '6', '7', '8', '9']

# for d in a[1:]:
#     for s1 in a:
#       for s2 in a:
#         for s3 in a: 
#             c = int('1'+d+'2157'+s1+s2+s3+'4')
#             if c % 2024 == 0:
#                 print(c, c//2024)

# 1?4*6?8 2622

for d1 in a[1:]:
    for s1 in a:
        for s2 in a:
            for d2 in a[1:]:
                c = int('1' + d1 + '4' + s1 + s2 + '6' + d2 + '8')
                if c < 10 ** 8:
                    if c % 2622 == 0:
                        print(c, c // 2622)

# делители     
for a in range(174457, 174505 + 1):
    c=[]
    for j in range(2,a//2+1):
        if a%j==0:
            c.append(j)
    if len(c)==2:
        print(a, c)
