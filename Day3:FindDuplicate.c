#include <stdio.h>
#include <stdlib.h>
int duplicated_number(int arr[], int n_arr){
   for(int i=0; i<n_arr; i++){
      for(int j=0; j<n_arr; j++){
         if(i==j){
            continue;
         }
         else if(arr[i] - arr[j] == 0){
               return arr[i];
         }
      }
   }
}

int main(){
   int n = 4;           
   int n_arr = n+1;
   int arr[]={3,1,3,4,2};
   int duplicated;
   // checking if all the array elements are in the range of n
   for(int i=0; i<n_arr; i++){
      if(arr[i]<n_arr){
         duplicated = duplicated_number(arr,n_arr);
      }
      else{
         printf("%d indexed element with value %d is grater than or equal to %d\n", i,arr[i],n_arr);
         exit(0);
         
      }  

   }
   printf("Duplicated number = %d",duplicated);
}
