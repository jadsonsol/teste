#A instrução "continue" interrompe a execução de um único ciclo de um laço de repetição.
#A instrução "break" interrompe todos os ciclos de um laço de repetição.
print("Antes")
print()
print("inicio")
print("inicio2")
i = 0
while(i<10):
    i += 1
    if(i%2==0):
        continue
    if(i>5):
        break
    print(i)
else:
    print("else")
print("fim")
print()
