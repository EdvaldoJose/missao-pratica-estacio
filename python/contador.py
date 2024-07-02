def conta_numero_pares(n):
    p = 0
    for num in range(n+1):
        if num % 2 == 0:
            p += 1
    return p


print("Numeros pares [0 2 4 6 8 10] :",
      conta_numero_pares(10))
