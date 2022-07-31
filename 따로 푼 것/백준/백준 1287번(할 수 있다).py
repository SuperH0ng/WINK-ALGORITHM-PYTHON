n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
e = ['+', '-', '/', '*']
n_cnt = 0
e_cnt = 0
now_n = False

exp = input()
for s in exp :
    if s in n :
        if now_n == False :
            n_cnt += 1
            now_n = True
    elif s in e :
        e_cnt += 1
        now_n = False
    if e_cnt > n_cnt :
        print("ROCK")
        quit()

if n_cnt == 0 :
    print("ROCK")
    quit()
    
try :
    print(eval(exp.replace('/','//')))
except :
    print("ROCK")