# #include<stdio.h>
# #include<stdlib.h>

# int main(){
# 	int code, age;
# 	float height, weight;
	
# 	printf("Qual o codigo:");
# 	 scanf("%d", &code);
# 	printf("Qual o idade:");
#    	 scanf("%d", &age);
# 	printf("Qual o altura:");
# 	 scanf("%f", &height);
# 	printf("Qual o peso:");
# 	 scanf("%f", &weight);
# 	printf("\n");
	
# 	printf("O CODIGO:%d \nA IDADE:%d \nA ALTURA:%.2f \nO PESO:%.2f \n", code, age,height, weight);
	
# 	system("pause");
# 	return 0;	
# }

def main():
    code = int(input("Qual o codigo: "))
    age = int(input("Qual a idade: "))
    height = float(input("Qual a altura: "))
    weight = float(input("Qual o peso: "))
    
    print("\n")
    print(f"O CODIGO: {code}")
    print(f"A IDADE: {age}")
    print(f"A ALTURA: {height:.2f}")
    print(f"O PESO: {weight:.2f}")

if __name__ == "__main__":
    main()