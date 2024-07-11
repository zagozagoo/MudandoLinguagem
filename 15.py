# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>
# #include<string.h>

# float calculo(float p_precolitro, float p_valorpgto);

# void main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	float precolitro = 0, valorpgto = 0, res = 0;
# 	char nome[50];
	
# 	printf("Informe seu nome:\n");
# 	fflush(stdin);
# 	gets(nome);
	
# 	printf("Informe o valor por litro de gasolina:\n");
# 	fflush(stdin);
# 	scanf("%f", &precolitro);
	
# 	printf("Informe o valor de pagamento:\n");
# 	fflush(stdin);
# 	scanf("%f", &valorpgto);
	
# 	res = calculo(precolitro,valorpgto);
# 	printf("\n%s voc� vai abastecer %.3f litros de gasolina. \n",nome,res);
	
# 	system("pause");
	
# }

# float calculo(float p_precolitro, float p_valorpgto){
# 	float res = 0;
# 	res = p_valorpgto / p_precolitro;
	
# 	return res;
# }

def calculo(p_precolitro, p_valorpgto):
    res = p_valorpgto / p_precolitro
    return res

def main():
    import locale
    locale.setlocale(locale.LC_ALL, 'Portuguese')
    
    precolitro = 0
    valorpgto = 0
    
    nome = input("Informe seu nome:\n")
    
    try:
        precolitro = float(input("Informe o valor por litro de gasolina:\n"))
        valorpgto = float(input("Informe o valor de pagamento:\n"))
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um numero valido.")
        return
    
    res = calculo(precolitro, valorpgto)
    print("\n%s você vai abastecer %.3f litros de gasolina.\n" % (nome, res))
    
    input("Pressione Enter para sair.")

if __name__ == "__main__":
    main()
