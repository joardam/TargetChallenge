#Solução mais simples baseado na função que retorna o termo geral da sequência fibonacci
import numpy as np # type: ignore

fibonacci = lambda n: int(((1 + np.sqrt(5))**n - (1 - np.sqrt(5))**n) /
                           (2**n * np.sqrt(5)))


#Aqui a função check_fibonacci recebe um número n e verifica se ele é um
#termo da sequência fibonacci

def check_fibonacci(n: int) -> bool:
    
    for i in range(1, n+1):
        #Otmiza o número de iterações
        if fibonacci(i) > n:
            break
        if fibonacci(i) == n:
            return True
    return False


#Teste
number = int(input("Digite um número: "))
print(f"Resultado: " , check_fibonacci(number))