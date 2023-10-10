#  List   
import  os 
os.system("cls")
lst = [12.2,  "Salom",  True, 'o', 1235]

print(lst)
for  i  in  range(len(lst)):
    print(lst[i])

 # Append 

lst.append("Faundation N37")
print(lst)

# Insert 

lst.insert(1,  False)
print(lst)

lst1 = [12.2,  "Salom",  True, 'o', 1235]
print(lst1)
print()

# Pop  
lst1.pop(2)
print(f"Pop   o'chirdi  {lst1}")


# Remove  
lst1.remove("Salom")
print(f"Remove  o'chirdi  {lst1}")



son_List  =  [34,3,63,578,9,3423,3536,2,1,56]
print(son_List)
print()

#   Sort  

son_List.sort()
print(son_List)

# Reverse 

son_List.reverse()
print(son_List)




# Extend

bir_List  = [12,345,True,56,575,75,8]
print(f"Bu  Birinchi  List  =>  {bir_List}")
ikki_List = ["Assalomu  Aleykum", "Faundation N37"]
print(f"Bu  Ikkinchi   List  =>  {ikki_List}")


bir_List.extend(ikki_List)
print()
print(F" Bir ====>  {bir_List}")

# Ikkinchi Listga Birinchi  Listni  Oldik
ikki_List.extend(bir_List)
print()
print(f" Ikkinchi   {ikki_List}")


# Copy 

lis2 = ["salom",  12, 25,  32,"Tugadi"]
print(F"Listni  o'zi  {lis2}")
kopi = lis2.copy()
print(f"Kopi  Qilingan  List ==>    {kopi}")



lst3 = [1,2,3,"salom",5,1,2,12,"salom",4,1,5,1,4,1]
# Count 
soni = lst3.count("salom")
print(f"Salom  Soni =>   {soni} ta ")

# Index 
index = lst3.index(12)
print(f"12  ning  Indexsi =>   {index}")

# Clear  

lst3.clear()
print(f"Tozalangan  List  {lst3}")

soz  = ['easdfa', 'radsfa', 'tadfa', 'aaaaafd', 'bfdasf',  'gafdadsad',  'adfdd']
soz.sort()
print(soz)

# Tuple  

tpl  = ("Salom ",  12,  True,  'i',  12.2, 'i')
print(tpl)

# Tuple  Count  

_soni = tpl.count('i')
print(f" necha  ekanligi  =>  {_soni}")

# Tuple  Index 

index = tpl.index('i')
print(f" Index  ==>   {index}")












