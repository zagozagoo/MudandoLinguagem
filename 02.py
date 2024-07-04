# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>
# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int idade = 0,cont = 0,totalidade = 0;
# 	float media = 0;
	
# 	for(cont = 1;cont<=2;cont++){
# 		printf("Informe a idade da criança: \n");
# 		fflush(stdin);
# 		scanf("%d",&idade);
# 		totalidade = totalidade + idade;
# 	}
	
# 	media = (float)totalidade/2;
# 	printf("\nO total das idades é %d anos \n",totalidade);
# 	printf("\nA média de idade é %.f anos \n",media);
	
# 	system("pause");
# 	return 0;
# }

def main():
    import locale
    locale.setlocale(locale.LC_ALL, "Portuguese")

    totalidade = 0
    media = 0

    for cont in range(1, 3): 
        print("Informe a idade da criança:")
        idade = int(input()) 
        totalidade += idade  # junta as idades p fazer o total

    media = totalidade / 2.0

    print(f"\nO total das idades é {totalidade} anos")
    print(f"A média de idade é {media:.0f} anos")

if __name__ == "__main__":
    main()