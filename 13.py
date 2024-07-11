# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>

# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int valores[10], par[5], impar[5];
# 	int cont, y = 0, x = 0;
	
# 	for(cont = 0;cont<10;cont++){
# 		printf("informe o %d� valor:",cont);
# 		fflush(stdin);
# 		scanf("%d",&valores[cont]);
# 	}
	
# 	for(cont = 0;cont<10;cont++){

# 		if(valores[cont] % 2 == 0){
# 			par[x] = valores[cont];
# 			x++;
# 		}
# 		else{
# 			impar[y] = valores[cont];
# 			y++;
# 		}
		
# 	}
# 	printf("NUMEROS PARES *0,02:\n");
# 	for(cont = 0;cont< x;cont++){
# 		printf("\n %d \n",par[cont]);
# 	}
# 	printf("NUMEROS IMPARES *0,05:\n");
# 		for(cont = 0;cont< x;cont++){
# 		printf("\n %d \n",impar[cont]);
# 	}
	
	
# 	system("pause");
# 	return 0;
# }

def main():
    valores = [0] * 10
    par = []
    impar = []

    for cont in range(10):
        valores[cont] = int(input(f"Informe o {cont + 1}º valor: "))

    for valor in valores:
        if valor % 2 == 0:
            par.append(valor)
        else:
            impar.append(valor)

    print("NUMEROS PARES *0,02:")
    for p in par:
        print(f"\n {p} \n")

    print("NUMEROS IMPARES *0,05:")
    for i in impar:
        print(f"\n {i} \n")

if __name__ == "__main__":
    main()
