# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>

# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int num_pessoas;
# 	char sexo;
# 	float alt,resp;
	
# 	printf("Qual a altura da pessoa? \n");
# 	fflush(stdin);
# 	scanf("%f",&alt);
	
# 	while(alt > 0){
		
# 	printf("Qual o sexo da pessoa?(M)Homens/(F)Mulheres \n");
# 	fflush(stdin);
# 	scanf("%c",&sexo);
	
# 		num_pessoas = num_pessoas + 1;
		
# 		if(sexo =='M'){
# 			resp =(72.7*alt)-58;
# 		}
# 		else{
# 			resp =(62.1*alt)-44.7;
# 		}
		
# 	printf(" Seu peso ideal é de: %.2f kilos \n\n\n",resp);
	
# 	printf("Qual a altura da pessoa? \n");
# 	fflush(stdin);
# 	scanf("%f",&alt);
		
# 	}
	
# 	printf(" %d participantes. \n \n",num_pessoas);
	
# 	system("pause");
# 	return 0;
# }

def main():
    num_pessoas = 0
    
    print("Qual a altura da pessoa?")
    alt = float(input())
    
    while alt > 0:
        print("Qual o sexo da pessoa? (M)/(F)")
        sexo = input().upper()
        
        num_pessoas += 1
        
        if sexo == 'M':
            resp = (72.7 * alt) - 58
        elif sexo == 'F':
            resp = (62.1 * alt) - 44.7
        else:
            print("Opção invalida. Informe M para Homens ou F para Mulheres.")
            continue
        
        print(f"Seu peso ideal eh de: {resp:.2f} kilos\n")
        
        print("Qual a altura da pessoa?")
        alt = float(input())
    
    print(f"{num_pessoas} participantes.\n")

if __name__ == "__main__":
    main()

 		