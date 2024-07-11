# #include <stdio.h>
# #include <string.h>

# #define TAM 3

#  struct ficha_candidato {
#  int codigo;
#  float salario;
#  char mail [50];
#  };
 
# int main () {
	
#  struct ficha_candidato candidato[TAM];
#  int i;

#  for (i = 0; i < TAM; i++) {
#  fflush(stdin);
#  printf("\nInforme o codigo do candidato: ");
#  scanf("%d",&candidato[i].codigo);
 
#  fflush(stdin);
#  printf("\nInforme o salario: ");
#  scanf("%f",&candidato[i].salario);

#  fflush(stdin);
#  printf("\nInforme o Mail: ");
#  gets(candidato[i].mail);
#  }

#  printf("************************************************************\n");
#  printf("************************************************************\n");

#  for (i = 0; i < TAM; i++) {
#  printf("\nCandidato %d ", i + 1);
#  printf("\n%d", candidato[i].codigo);
#  printf("\n%.2f", candidato[i].salario);
#  printf("\n%s", candidato[i].mail);
#  }

#  system("pause");
#  return 0;
# } 

class FichaCandidato:
    def __init__(self, codigo, salario, mail):
        self.codigo = codigo
        self.salario = salario
        self.mail = mail

def main():
    TAM = 3
    candidatos = []

    for i in range(TAM):
        codigo = int(input("\nInforme o código do candidato: "))
        salario = float(input("\nInforme o salário: "))
        mail = input("\nInforme o e-mail: ")

        candidato = FichaCandidato(codigo, salario, mail)
        candidatos.append(candidato)

    print("************************************************************")
    print("************************************************************")

    for i, candidato in enumerate(candidatos):
        print(f"\nCandidato {i + 1}")
        print(candidato.codigo)
        print(f"{candidato.salario:.2f}")
        print(candidato.mail)

if __name__ == "__main__":
    main()
