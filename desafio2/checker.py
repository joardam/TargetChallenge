#Verifica se a string possui a letra "a" maiúscula ou minúscula 
# e informa a quantidade de vezes que ocorre

verify_a= lambda s: s.lower().count("a")

#Teste
string = input("Digite uma string: ")
print(f"Resultado: " , verify_a(string))

