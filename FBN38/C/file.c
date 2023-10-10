#include  <stdio.h>
#include  <string.h>

int main  (){
    FILE  *f = fopen("C:\\Users\\Dilma\\Documents\\NajotTalim\\C_code\\FAKTARYAL.txt","a");
    int  son,  fakt = 1;
    printf  ("Brtan  Son  kiriting ");
    scanf  ("%d",&son);

    for  (int  i  = 1;  i  <=  son;  i++ ){
        fakt  = fakt  *  i;
    }
    fprintf(f, "\n%d ni  Faktaryali   ==> %d", son, fakt);
    printf("%d  Ni  Factaryali ===>  %d ", son,  fakt);
    printf("BU Malumot  Faylga Yozildi");
    fclose(f);
    return  0;
}