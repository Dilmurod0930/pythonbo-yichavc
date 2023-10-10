# Funksiyalar 

# def  faktar (n):
#     fak = 1  
#     for  i  in  range(1, n + 1 ):
#         fak = fak * i
#     return  fak
# son = int  (input("Son  Kiriting  >>>>>>  "))
# faktarial  = faktar(son)
# print(f"{son} ni  Faktariali  {faktarial}")


#######################################################################


# List  ichidagi  elementlarni  faktarialini  chiqaradigan  funksiya  


# def  listMalumot(son):
#     lis =[]
#     if  ( son >  5):
#         for  i in  range(son):
#             malumot = int (input("Sonni  Kiriting  >>>>⚡  "))
#             lis.append(malumot)
#     else :
#         print("Brat  5  dan Katta  son  kiriting  !!😡")

#     return lis

# def  listFaktar (ls):
#     lt = []
#     for i  in  range(len(ls)):
#         print(ls[i])
#         fak  = 1
#         for  j  in range(1, ls[i]+1):
#             fak  = fak  *  j
#         lt.append(fak)
#     return  lt 

    
# son = int(input("Nechta  Son  Qo'shasiz  >>>"))
# lt  =  listMalumot(son)
# lc1 = listFaktar(lt)
# print(F"List  Elementlarini  faktariali >>>> {lc1}")
# print(lt)


#######################################################################

# def sonlar ():
#     son = int  (input("Son  Kiriting >>>>>>  "))
#     lst = []
#     while  (son  > 0):
#         s  = son %  10
#         lst.append(s)
#         son  = son // 10
#     lst.reverse() 
#     return  lst

# def  qaytar (lst):
#     yig  = 0
#     kop = 1
#     ls = []
#     for  i  in  range(len(lst)):
#         if  (i  %  2 == 0 ):
#             yig  += lst[i]
#         if not  (i  %  2 == 0 ):
#             kop = lst[i] **2 
#             ls.append(kop)
#     return  yig ,ls


# lst  = sonlar()
# ls  =  qaytar(lst)
# print(ls)








def  aniqla(soz  ):
    katta  = 0
    kichik  = 0
    for  i  in  soz :
        if  (i.isupper()):
            katta += 1
        if  (i.islower()):
            kichik +=  1
    return  katta  ,  kichik 


def  aniqla1(soz):
    katta  = 0
    kichik  = 0
    for i  in  soz :
        if  (i  in  "QWERTYUIOPASDFGHJKLZXCVBNM"):
            katta += 1
        if  (i in  "qwertyuiopasdfghjklzxcvbnm"):
            kichik += 1
    return katta,  kichik


soz  = input  ("Matin  Kiriting >>>>>  ")
lst =  aniqla(soz)
la = aniqla1(soz)
print(lst)
print(la)