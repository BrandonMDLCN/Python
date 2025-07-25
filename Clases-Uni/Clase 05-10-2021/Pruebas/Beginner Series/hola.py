def lovefunc( flower1, flower2 ):
    f1 = flower1%2
    f2 = flower2%2
    if f1 ==0 and f2 !=0:    
        print(True)
    if f1 != 0 and f2 == 0:
        print(True)
    if f1 == f2:
        print(False)



lovefunc(655,307)#, False)
lovefunc(239,67)#, False)
lovefunc(0,1)#, True)
lovefunc(0,0)#, False)