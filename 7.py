# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>
# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int num = 0,cont = 0;
	
# 	printf("_____________________tabuada do 7________________________________\n");
# 	for(cont = 1;cont<=10;cont++){
# 		num = 7;
# 		printf("%d X %d = %d \n",7,cont,7*cont);
# 	}
# 	printf("_____________________tabuada do 8________________________________\n");
# 	for(cont = 1;cont<=10;cont++){
# 		num = 8;
# 		printf("%d X %d = %d \n",8,cont,8*cont);
# 	}
	
# 	system("pause");
# 	return 0;
# }

def main():
    print("_____________________tabuada do 7________________________________")
    for cont in range(1, 11):
        num = 7
        print(f"{num} X {cont} = {num * cont}")
    
    print("_____________________tabuada do 8________________________________")
    for cont in range(1, 11):
        num = 8
        print(f"{num} X {cont} = {num * cont}")

    print("_____________________tabuada do 9________________________________")
    for cont in range(1, 11):
        num = 9
        print(f"{num} X {cont} = {num * cont}")

if __name__ == "__main__":
    main()
