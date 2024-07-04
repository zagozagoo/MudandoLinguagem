# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>

# struct imovel_dados{
# 	int numcad ;
# 	float valorIPTU ;
# 	int mesesatrasado;
# 	float valorMulta;
# };

# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	struct imovel_dados ap[3];
# 	int cont,calculos = 0;


# 	for(cont = 0; cont < 3; cont++){
			
# 		printf("\nINFOME O NUMERO DE CADASTRO(%d� imovel):\n",cont+1);
# 		fflush(stdin);
# 		scanf("%d",&ap[cont].numcad);
# 		printf("\nINFOME O VALOR DO IPTU:\n");
# 		fflush(stdin);
# 		scanf("%f",&ap[cont].valorIPTU);
# 		printf("\nINFOME QUANTOS MESES ATRASADO:\n");
# 		fflush(stdin);
# 		scanf("%d",&ap[cont].mesesatrasado);
		
# 		ap[cont].valorMulta = 50.00 * ap[cont].mesesatrasado;
# 		calculos++;

# 	}
# 	for(cont = 0;cont<3;cont++){
# 	printf("\nCADASTRO: %d\nVALOR IPTU: %.2f\nMESES EM ATRASO: %d\nMULTA: %.2f\n\n\n",ap[cont].numcad, ap[cont].valorIPTU, ap[cont].mesesatrasado ,ap[cont].valorMulta);
	
# }
# 	printf("Numero de imoveis calculados: %d imov�is.\n\n",calculos);
# 	system("pause");
# 	return 0;
# }

class ImovelDados:
    def __init__(self, numcad, valorIPTU, mesesatrasado, valorMulta):
        self.numcad = numcad
        self.valorIPTU = valorIPTU
        self.mesesatrasado = mesesatrasado
        self.valorMulta = valorMulta

def main():
    imoveis = []

    for i in range(3):
        print(f"\nINFORME O NÚMERO DE CADASTRO ({i+1}º imóvel):")
        numcad = input_int("")
        valorIPTU = input_float("INFORME O VALOR DO IPTU:\n")
        mesesatrasado = input_int("INFORME QUANTOS MESES ATRASADO:\n")

        valorMulta = 50.00 * mesesatrasado

        imovel = ImovelDados(numcad, valorIPTU, mesesatrasado, valorMulta)
        imoveis.append(imovel)

    for imovel in imoveis:
        print(f"\nCADASTRO: {imovel.numcad}")
        print(f"VALOR IPTU: R${imovel.valorIPTU:.2f}")
        print(f"MESES EM ATRASO: {imovel.mesesatrasado}")
        print(f"MULTA: R${imovel.valorMulta:.2f}\n")

    print(f"Número de imóveis calculados: {len(imoveis)} imóveis.")

if __name__ == "__main__":
    main()
