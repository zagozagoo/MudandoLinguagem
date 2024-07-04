# #include<stdio.h>
# #include<locale.h>

# float ideal_homem ( float p_altH);
# float ideal_mulher ( float p_altF);

# void main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	float alt = 0,resh = 0,resf = 0;
# 	char sexo;
	
# 	printf("Informe seu sexo((M) Masculino e (F) Feminino):\n");
# 	fflush(stdin);
# 	scanf("%c",&sexo);
	
# 	printf("_________________________________________________\n");
	
# 	printf("Informe sua altura (com (,) separando metros de centimetros):\n");
# 	fflush(stdin);
# 	scanf("%f",&alt);
	
# 	printf("_________________________________________________\n");
	
# 	if(sexo =='M' || sexo =='m'){
# 		resh = ideal_homem(alt);
# 		printf("RESPOSTA");
# 		printf("\nSeu peso ideal é:%.2f kilos.\n",resh);
# 		printf("_________________________________________________\n");
# 	}
# 	else{
# 		resf = ideal_mulher(alt);
# 		printf("RESPOSTA");
# 		printf("\nSeu peso ideal é:%.2f kilos.\n",resf);
# 		printf("\n\n_________________________________________________\n");
# 	}

	
# 	system("pause");

# }


# float ideal_homem ( float p_altH){
# 	float valorH;
	
# 	valorH = (72.7 * p_altH) - 58;
# 	return valorH;
# }

# float ideal_mulher ( float p_altF){
# 	float valorF;
	
# 	valorF = (62.1 * p_altF) - 44.7;
# 	return valorF;
# }

import sys
import locale

def ideal_homem(p_altH):
    valorH = (72.7 * p_altH) - 58
    return valorH

def ideal_mulher(p_altF):
    valorF = (62.1 * p_altF) - 44.7
    return valorF

def main():

    alt_str = input("Informe sua altura (usando virgula): ")
    alt_str = alt_str.replace(',', '.')  # troca virgula pelo ponto
    alt = float(alt_str)
    
    print("_________________________________________________\n")
    
    sexo = input("Informe seu sexo ((M) Masculino e (F) Feminino): ").upper()
    
    print("_________________________________________________\n")
    
    if sexo == 'M':
        resh = ideal_homem(alt)
        print("RESPOSTA")
        print(f"\nSeu peso ideal eh: {resh:.2f} kilos.\n")
        print("_________________________________________________\n")
    elif sexo == 'F':
        resf = ideal_mulher(alt)
        print("RESPOSTA")
        print(f"\nSeu peso ideal eh: {resf:.2f} kilos.\n")
        print("\n\n_________________________________________________\n")
    else:
        print("Sexo invalido. Informe M para Masculino ou F para Feminino.")
        sys.exit(1)

if __name__ == "__main__":
    main()
