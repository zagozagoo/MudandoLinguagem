# #include <stdio.h>
# #include <stdlib.h>
# #include<locale.h>

# int mns(int meudeus, int jesus);

# int main() {
#    setlocale(LC_ALL,"Portuguese");
    
#     int n1 = 0, nx_n1 = 0, resp;
    
#     printf("Informe o primeiro numero:\n ");
#     fflush(stdin);
#     scanf("%d", &n1);
#     printf("Informe o numeros de vezes que o primeiro numero sera somado:\n ");
#     fflush(stdin);
#     scanf("%d", &nx_n1);
    
#     resp = mns(n1, nx_n1);
    
#     printf("\nRESPOSTA: %d\n\n", resp);
    
#     return (0);
#     system("pause");
# }

# int mns(int senhordagloria, int oq_esta_contecendo){
    
#     if(oq_esta_contecendo == 1){
#         return senhordagloria;
#     } else {
#         return senhordagloria + mns(senhordagloria, oq_esta_contecendo-1);
#     } 
# }

def mns(senhordagloria, oq_esta_contecendo):
    if oq_esta_contecendo == 1:
        return senhordagloria
    else:
        return senhordagloria + mns(senhordagloria, oq_esta_contecendo - 1)

def main():

    n1 = int(input("Informe o primeiro numero: "))
    nx_n1 = int(input("Informe o numero de vezes que o primeiro numero sera somado: "))

    resp = mns(n1, nx_n1)

    print(f"\nRESPOSTA: {resp}\n")

if __name__ == "__main__":
    main()
