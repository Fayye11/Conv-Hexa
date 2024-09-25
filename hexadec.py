def hexadecimal(value):
	if value < 10:
		return str(value)
	
	else:
		hex = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
		return hex.get(value, str(value))
		

# Solicitar que o usuário insira um número
numdeci = input("Insira um número: ")
numdeci = int(numdeci)

# Solicitar que o usuário insira o divisor
divisorhexa = input("Insira o divisor desejado (16 para hexa): ")
divisorhexa = int(divisorhexa)

restos = []

while numdeci != 0:
    # Calcular o quociente e o resto da divisão
    quociente = numdeci // divisorhexa
    resto = numdeci % divisorhexa

    # Exibir os resultados
    print(f"O quociente da divisão de {numdeci} e {divisorhexa} é: {quociente}")
    print(f"O resto da divisão de {numdeci} e {divisorhexa} é: {hexadecimal(resto)}")
    
    restos.append(hexadecimal(resto))

    # Atualizar o número para o quociente anterior para a próxima iteração
    numdeci = quociente

print("Não é possivel mais dividir o numero, você chegou no limite!!")


restos.reverse()

restos_string = "".join(restos)

print("A conversão de decimal para Hexadecimal é: ", restos_string)
