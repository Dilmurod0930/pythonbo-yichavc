


# my_dict = {"Name":[],"Address":[],"Age":[]}

# my_dict["Name"].append("Kimsan")
# my_dict["Address"].append("Bilmadim")
# my_dict["Age"].append(110)	
# print(my_dict)




# dic1 = {}
# dic2 = {}
# nechta  = int (input("Nechta  Malumot  Kiritasi ==> "))
# for  i  in  range(nechta):
#     key  = input("Keyni  Kiriting  ==>  ")
#     vale  = input ("Valueni  KIriting  ==> ")
#     dic1.setdefault(key, vale)
# dic2  = dic1.copy()
# dic1.clear()
# print(f"Tozalangan  Dic 1 ==>   {dic1}")
# print()
# print(f"Copi  Qilingan  Malumot  ==>  {dic2}")

# Update  Dic

# meva = {'Olma_Narxi':'67', 'Kartoshka_Narxi':87}
# qolibKetgan_Meva = {'Pamidor_Narxi': 48, 'Non_Narxi': 55}
# print(f"Birnchi  Harid ==>  {meva}")
# meva.update(qolibKetgan_Meva)
# print(f"Qayta  Harid  ==>  {meva}")


#   List ichida  elementlarni  ikki  marta 
#  takrorlanganlarini  o'chirib  yuborish  

# ls  = ["s", "s", 'dima', "qalaysan"]
# soni = int  (input("Nechta  Malumot  Kiritasiz  ==> "))
# for  i  in  range(soni):
#     malumot  = input(f"{i+1} Malumotni  Kiriting  ==> ")
#     ls.append(malumot)
# print(ls)
# s = set(ls)
# print(s)


 #%% Faqat Veluesni  chiqArish  





# sales = { 'apple': 34, 'orange': 5, 'range': 10, 'grapes': 4 }
# print(sales.values())


# N37  guruh 


# dc  = {"Ismi": "Anvar ", "Yil": 2023}
# print(f"Elon  Qilingan  Dic ==>  {dc}")
# dc ["Kasbi"] = "Senga Nima"
# print(f"Qo'shilgandan  Keyingi  Dic ==> {dc}")
# key = input ("Keyni  Kiriting ==> ")
# value = input("Valueni  Kiriting ==> ")
# dc.setdefault(key,  value)
# print(f"Funksiya  bilan  qo'shildi ==>   {dc}")


# dic = {}
# soni = int (input ("NEchta  malumot  Kiritasiz  ==> "))
# for  i  in  range(soni):
#     key = input("Key  ==>  ")
#     value  = input("Value  ==>  ")
#     dic.setdefault(key,  value)
# print(dic)
# #######################################################

# dic1 = {}
# dic1_Soni = int (input("NEchta  malumot  qo'shasiz  ==> "))
# for  i in  range(dic1_Soni):
#     key  = input("Key  ==> ")
#     value  = input ("Value ==> ")
#     dic1.setdefault(key,  value)
# print(f"Birinchi  DIC ==>  {dic1}")

# dic2 = {}
# dic2_Soni = int (input("NEchta  malumot  qo'shasiz  ==> "))
# for  i in  range(dic2_Soni):
#     key  = input("Key  ==> ")
#     value  = input ("Value ==> ")
#     dic2.setdefault(key,  value)
# print(f"Ikkinchi   DIC ==>  {dic2}")

# dic1.update(dic2)
# print()
# print(f"Update  Qilingan  DIC ==>   {dic1}")








# lis = []
# soni  = int  (input("Nechta  element  kiritasiz  ==> "))
# for  i  in  range(soni):
#     malumot  = input (F"{i + 1}Malumotni  Kiriting ==> ")
#     lis.append(malumot)
# print(F"Kiritilgan  List  {lis}")
# ls  = set(lis)
# print(ls)




# ls1  =["O'n", "Yigirma",  "O'ttiz"]
# ls2= [100, 200, 300]
# dc ={}

# for  i in  range(len(ls1)):
#     dc.setdefault(ls1[i], ls2[i])

# print(dc)




dic  = {'a':123,  'b':200, "c": 300, 'd':677 }
for i , j in  dic.items():
    if  j >= 200:
        print(f"'{i}': {j}")












# 38 gutuh  



#%%  Faqat Keyni    chiqrish 
# numbers = {1: 'one', 2: 'two', 3: 'three'}
# dictionaryKeys = numbers.keys()
# print(dictionaryKeys)


#%%  

# Dic  berilgan  shu  berilgan  dic  ni  keysini berganda 
#  dicdan  o'chirib  velusin  ekranga  bostiring   

# marks = { 'Physics': 67, 'Chemistry': 72, 'Math': 89 }
# element = marks.pop('Chemistry')
# print('Popped Marks:', element)
# print(marks)



