# # %% Berilgan  list  foydalanuvchi  1  ta  son  kiritadi 
# # kiritilgan  soncha  elementni  silsni  oldingi  
# # tarafiga  o'tqazib  qo'yish  


# nums = [1, 2, 3, 4, 5, 6, 7]
# k = int ( input("Son  Kiriting  ==>  "))
# for i in range(k):
#     a = nums[-1]
#     for j in range(len(nums)-1,0,-1) :
#         nums[j] = nums[j-1]
#     nums[0] = a
# print(nums)


# # %% 

# Orol va  suv  suvni ichida  nechta  orol  borligini  aniqlaydigan  dastur 


class  Orol:
    def  orolTop(self ,  matristsa:  list [list[str]]) ->  int:
        hisobla = 0
        orol = len(matristsa)
        suv = len(matristsa[0])
        def tekshir(i, j):
            matristsa[i][j] = - 1
            if (i < orol - 1 and  matristsa[i + 1][j] == "1"):
                tekshir(i + 1  , j)
            if  (i > 0 and  matristsa[i - 1][j] == "1"):
                tekshir(i - 1 ,  j)
            if  (j <  suv - 1  and  matristsa[i][j + 1] ==  "1"):
                tekshir(i, j + 1 )
            if  (j > 0 and  matristsa[i][j - 1] == "1"):
                tekshir(i, j - 1 )
                
        for  o  in range (orol):
            for  s  in  range(suv):
                if  matristsa[o][s] == "1":
                    hisobla  = hisobla  + 1
                    tekshir(o , s)
        return  hisobla
orol = Orol()
matrix = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(orol.orolTop(matrix))