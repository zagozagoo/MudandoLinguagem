# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>

# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int val[10];
# 	int busca = 0;
# 	int achou = 0;//0 - nao achou, // 1 - achou
# 	int cont;
	
# 	for(cont = 0;cont < 10; cont ++ ){
# 		printf("informe o %d� valor:",cont+1);
# 		fflush(stdin);
# 		scanf("%d",&val[cont]);
# 	}
	
# 	printf("\n Informe um valor pra ser procurado:");
# 	fflush(stdin);
# 	scanf("%d", &busca);
		
# 	for(cont = 0;cont < 10; cont ++ ){
# 		if(busca == val[cont]){
# 			achou = achou + 1;
# 		}
# 	}
# 	printf("O numero foi achado %d vezes.",achou);
	
# system("pause");
# return (0);
# }

def main():
    val = []
    achou = 0  #0 -> nao achou, 1 ou mais -> achou
    busca = 0
    
    for cont in range(10):
        val.append(int(input(f"Informe o {cont+1}º valor: ")))
    
    busca = int(input("\nInforme um valor para ser procurado: "))
    
    for cont in range(10):
        if busca == val[cont]:
            achou += 1
    
    print(f"\nO numero foi achado {achou} vezes\n")

if __name__ == "__main__":
    main()
