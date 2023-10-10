# kiritilgan   soni  faktarialini  topadigan  funksiya  tuzish  

# def  fakratial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     print(fact)
#     return  fact

# fakratial(int(input("Son  Kiriting >>> ")))
# faktar = fakratial(5)
# print(faktar)


# #############################################################################


#   kiritilgan  sonni  toq  indexdagilarini  kvadratini 
#  juft  indexdagi  sonlarni  yig'indisini  chiqaradigan  funksiya  tusing  


# def  hisobla ():
#     son = int (input("Son  Kiriting "))
#     lis = []
#     while  (son > 0 ):
#         s  = son  % 10 
#         lis.append(s)
#         son  =  son  //  10
#     print(f"List  Elementlari  Teskari  tartibda    {lis}")
#     lis.reverse()
#     lct = []
#     yig  = 0
#     for  j  in range(len(lis)) :
#         if  (j  %  2 == 0):
#             yig  += lis[j]
#         if  not  (j  %  2 == 0):
#             kop = lis[j] **2 
#             lct.append(kop)
#     print(f"List  Elementlari   {lis}")
#     print(f"Juft  Index  Yig'indisi ==>   {yig}")
#     print(f"Toq   Index  Kvadrati  ==>   {lct}")

# hisobla()


# #############################################################################

# list  ichidagi  sonlarni  3  ga  bo'linadiganini  qaytaradigan
#   funksiya  tuzing  \


# def  lis3GaBol(ls):
#     ls3_bolinadigan  = []
#     for  j  in  range(len(ls)):
#          if  (ls[j] %  3  == 0):
#              ls3_bolinadigan.append(ls[j])
#     # print(f"List  Ichida  3 ga  Bo'linadigan  Sonlar ==>  {ls3_bolinadigan}")
#     return ls3_bolinadigan


# soni  = int  (input ("Nechta  Son  Kiritasiz  >>>  "))
# ls  = []
# for  i in  range(soni):
#     malumot= int(input(f"{i+1} - Soni  Kiriting >>>>> "))
#     ls.append(malumot)
# print(f"List  Elementlari  ==> {ls}")

# lis =  lis3GaBol(ls)
# print(f"3  ga  bo'linadigan  sonlar   {lis}")


# #############################################################################
# string  kiritiladi  unda kechta  kata  harf  va  nechta 
#  kichik  harif qatnashganini  taytruvchi  funksiya  tuzing  

# def  qaytar(s):
#     harf_katta = 0
#     harf_kichik = 0
#     for  i  in  s:
#         if (i.islower()):
#             harf_kichik += 1
#         elif(i.isupper()):
#             harf_katta += 1
#     return  harf_katta  , harf_kichik   
# soz  = input("So'z  kiriting  ==>  ")
# print(qaytar(soz))


                # Ikkinchi  usuli  

# def  aniqla  (string):
#     katta  = 0
#     kichik = 0
#     for  i  in  range(len (string)):
#         if  (string[i] in  "QWERTYUIOPASDFGHJKLZXCVBNM"):
#             katta += 1
#         elif (string[i] in "qwertyuiopasdfghjklzxcvbnm"):
#             kichik += 1
#     return  katta  ,  kichik

# soz  =  input("So'z  Kiriting  >>>>>>>>  ")
# print(aniqla(soz))



# #############################################################################

# Function tuzing, list qabul qilsin va 
#  listdagi eng katta qiymatni qaytarsin



num  = [1,2,3,4,5,6]
nm  =  list (filter(lambda  s  : s %  2  == 0 , num))
print(list(nm))



# #############################################################################



# Masalan foydalanuvchi 5 sonini kiritdi. Shunda siz
#  foydalanuvchidan 5 ta element qabul qiling va ularning 
# kvadratlarini list tarzida qaytaruvchi function tuzing







# #############################################################################
# Funksiyada   Foydalanuvchi n son kiritadi. 1 dan n gacha 
# bo'lgan tub sonlardan bitta list hosil qiling. 