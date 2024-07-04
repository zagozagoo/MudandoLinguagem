# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>
# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	char sexo;
# 	int idade;
	
# 	printf("QUAL A IDADE: \n");
# 	fflush(stdin);
# 	scanf("%d", &idade);
	
# 	printf("QUAL O SEXO, (M) PARA MASCULINO OU (F) PARA FEMININO: \n");
# 	fflush(stdin);
# 	scanf("%c",&sexo);
	
# 	if(sexo == 'M'){
# 		if(idade >=16){
# 			printf("voce tem direito a compra de ingressos \n");
# 		}
# 		else{
# 			printf("voce nao pode comprar ingressos \n");
# 		}
# 	}
# 	else{
# 		if(idade >= 18){
# 			printf("voce tem direito a compra de ingressos \n");
		
# 		}
# 		else{
# 			printf("voce nao pode comprar ingressos \n");
# 		}
# 	}
# 	system("pause");
# 	return 0;
# }

def main():
    idade = int(input("Qual a idade: "))
    sexo = str(input("QUAL O SEXO, (M) PARA MASCULINO OU (F) PARA FEMININO: "))
    print("\n")

    if sexo == "F":
        if idade >= 16:
            print("Voce tem direito a compra de ingressos! \n")
        else:
            print("Voce nao pode comprar ingressos :( \n")
    
    if sexo == "M":
        print("HOMENS NAO ESTAO CONVIDADOS PARA A FESTINHA DO GLITTER")

if __name__ == "__main__":
    main()
    