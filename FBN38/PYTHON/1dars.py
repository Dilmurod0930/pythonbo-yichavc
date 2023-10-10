import  os 
os.system("cls")
"""
# lst  = [12,45,67,3,45,67,78,89,900,12]
# lst.sort()
# print(lst)

# lst1  = []
# soni  = int (input("NEchta  son  kiritasiz ==>  "))
# for i  in  range(soni):
#     son = int (input (f"{i+1} Soni  Kiriting  ==>  "))
#     lst1.append(son)

# for  j  in  range(len(lst1)):
#     print(lst1[j], end = "  " )

# lst1.sort()
# print(lst1)


# yangi_list = []
# bosh_son  = int  (input("Boshlanish  sonini  kiriting  ==> "))
# tugash_son = int  (input("Tugash  sonini  kiriting  ==>  "))

# for  i  in  range   (bosh_son  ,  tugash_son + 1,  1):
#     if not  (i  %  2  == 0 ):
#         yangi_list.append(i)
# yangi_list.reverse()
# print(yangi_list)



# yangi_list1 = []
# bosh_son1  = int  (input("Boshlanish  sonini  kiriting  ==> "))
# tugash_son1 = int  (input("Tugash  sonini  kiriting  ==>  "))

# for  i  in  range   (bosh_son1  ,  tugash_son1 + 1,  1):
#     if   (i  %  2  == 0 ):
#         yangi_list1.append(i)
# print(yangi_list1)



# lst  = [12,45,67,3]
# print(f"Listda  indexlar  soni  {len(lst)}")
# nechta = int(input("Nechta  indexni  o'chitasiz  ==>"))
# if  (nechta  <  len(lst)+1):
#     for i  in  range(nechta):
#             index = int (input("Indexni  kiriting  ==> "))
#             lst.pop(index)
#             print(f"Listda {len(lst)} ta Index  Qoldi ")
# else:
#     print(f"List  ichita  {len(lst)}ta  index  index  bor")

# print(f"POPda  o'chirilgandan  qolgan  list  {lst}")


# text = input("Enter text: ")
# text1 = text.split()
# text1.sort()
# print(text1)



# text = input("Enter the text: ")
# words = text.split()
# words[0] = words[0][::-1]
# words[len(words) - 1] = words[len(words) - 1][::-1]
# words = " ".join(words)
# print(words)


 
# print("The factorial of 5 is : ", end="")
# print(math.factorial(5))

# faktar  = 1
# son_fak  = int  (input("Son  kiriting  ==>  "))
# for i  in range(1,son_fak+1):
#     faktar = faktar * i 
# print(faktar)



# list_faktar = [2,5,6,7,8,9,10,12]
# yangi_List_Faktar = []

# for  j  in  range(len(list_faktar)):
#     faktarila  = math.factorial(list_faktar[j])
#     yangi_List_Faktar.append(faktarila)

# print(list_faktar)
# print(yangi_List_Faktar)"""

# lst1  = []
# lst2  = []

# bir_list  = int  (input("Bitinchi  Listga Nechata  Malumot  Kiritasiz ==> "))
# for  i  in  range(bir_list):
#     bir_list_qosh  = int  (input("Sonlarni  kiriting  "))
#     lst1.append(bir_list_qosh)

# ikki_list  =  int  (input("Ikkinchi  Listga  Nechata  Malumot  Kiritasiz  ==> "))
# for  j  in  range  (ikki_list):
#     ikki_list_qosh  = int  (input("Ikkinchi  Listga  Sonlarni  Kiriting  ==>  "))
#     lst2.append(ikki_list_qosh)


# print(f"Birinchi  List  ==> {lst1}")
# print(f"Ikkinchi  List  ==>   {lst2}")

# lst1.pop()
# lst1.extend(lst2)
# print()
# print(f"Umumiy  Javob  ==>   {lst1}")

# yangi_list   = []  

# list_Soni = int(input("Listga  Nechta  Son  Kiritasiz  ==>  "))
# for i in range(list_Soni):
#     list_Son_Qosh  =  int  (input(f"{i  +  1} Son   => "))
#     yangi_list.append(list_Son_Qosh)
    
# print(f"List  Malumotlari  ==>  {yangi_list}")

# son_qosh  = int (input("Nechta  Son  Qo'shasiz  ==>  "))
# for  j  in  range(son_qosh):
#     son1 = int(input("Indexni  Kitiring ==>  "))
#     son2 = int(input("Malumotni  Kiriting  ==>  "))       
#     yangi_list.insert(son1,son2)

# print(f"Yangi  List  ==>   {yangi_list}")






# yangi_list   = []  
# list_Soni = int(input("Listga  Nechta  Son  Kiritasiz  ==>  "))
# for i in range(list_Soni):
#     list_Son_Qosh  =  int  (input(f"{i  +  1} Son   => "))
#     yangi_list.append(list_Son_Qosh)
    
# print(f"List  Malumotlari  ==>  {yangi_list}")

# tanla  =  input("Index Orqali  O'chirish  Uchun  || 0 || bosing\nQiymat  Orqali  O'chirish  Uchun  ||  1  ||  bosing  \nKiriting  ====>  ")

# if  (tanla  ==  '0'):
#     print(f"Listda  {len(yangi_list)} ta  Index  Bor !!\n{yangi_list}")
#     index  = int (input("Indexni  Kiriting  ==>  "))
#     yangi_list.pop(index)

# elif (tanla  == '1'):
#     print(f"Listda  {len(yangi_list)-1} ta  Index  Bor !!\n{yangi_list}")
#     index  = int (input("Qiymatni   Kiriting  ==>  "))
#     yangi_list.remove(index)


# else :
#     print("Axmoq  Qilaybsizmi  Birat  !!!!")
    
# print(f"List  Ma'lumotlari  ==>    {yangi_list}")





yangi_list   = [1,1,1,22,22,3,44,44,44,44,]  
list_Soni = int(input("Listga  Nechta  Son  Kiritasiz  ==>  "))
for i in range(list_Soni):
    list_Son_Qosh  =  int  (input(f"{i  +  1} Son   => "))
    yangi_list.append(list_Son_Qosh)

yangi_list  = tuple(yangi_list)
print(f"List  Malumotlari  ==>  {yangi_list}")



