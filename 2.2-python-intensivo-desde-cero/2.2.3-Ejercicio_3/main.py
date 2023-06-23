inputNum = int(input("Ingresa un número: "))

def encontrar_numeros_primos(inputNum):
    primos = []
    for num in range(2, inputNum + 1):
        es_primo = True
        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    return primos


primos_encontrados = encontrar_numeros_primos(inputNum)
print(primos_encontrados)
