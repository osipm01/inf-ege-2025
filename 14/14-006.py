
# def f(n):
#     for i in range(2,int(n**0.5)+1):
#         if n % i ==0: return False
#     return True



def is_valid(n):
    for i in range(2, int(n**0.5)+1):
        if n % i ==0: return False
    return True
    

alph = "0123456789AB"
dat = []

for x in alph:
    for y in alph:
        val = int(f'5{x}9{x}4', 12) + int(f'7{x}{x}6', 14) + int(f'55{x}{x}8', 16) - int(f'3{x}{y}7', 19)
        if is_valid(val):
            print(int(x, 12) * int(y, 12))