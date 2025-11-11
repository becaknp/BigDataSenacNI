def celsius_para_fahrenheit(temp_c):
    return (temp_c*9/5) + 32

def fahrenheit_para_celsius(temp_f):
    return (temp_f-32) *5/9

def conversao():
    print("Escolhe um opção:")
    print("1  -  Celsius -> fahrenheit")
    print("2  -  Fahrenheit -> Celsius")

    escolha = input("opção: ")

    if escolha == 1:
        temp = float(input("Digite a temperatura em Celsius: "))
        resultado = celsius_para_fahrenheit
        print(celsius_para_fahrenheit)
    else:
        print (fahrenheit_para_celsius)

   

# print(f"Resultado da Conversão: {conversao}")
