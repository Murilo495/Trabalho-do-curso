
#Questão 1=
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

if nota1 == nota2 == nota3:
    print (" Todas as notas são iguais.")
elif nota1 == nota2 and nota1 > nota3:
    print (" As duas maiores notas são iguais.")
elif nota1 == nota3 and nota1 > nota2:
    print (" As duas maiores notas são iguais.")
elif nota2 == nota3 and nota2 > nota1: 
    print (" As duas maiores notas são iguais.")
elif nota1 > nota2 and nota1 > nota3:
    print (" A maior nota é a primeira: ", nota1)
elif nota2 > nota1 and nota2 > nota3:
    print (" A maior nota é a segunda: ", nota2)
elif nota3 > nota1 and nota3 > nota2:
    print (" A maior nota é a terceira: ", nota3)

#Questão 2=
saldo = float(input("Digite o saldo da conta: "))
saque = float(input("Digite o valor do saque: "))

if saque > 0:
   saldo =saldo - saque

   if saldo > 0:
       print ("positivo")
   elif saldo < 0:
       print ("negativo (Entrou no cheque especial)")
   else:
       print ("zero")
else:
   print ("Erro: O valor do saque deve ser maior que zero")

#Questão 3=
print (" Rede social do bem ")
perfil = input("Digite o perfil do usuário: ").upper()
if perfil == "A":
    print ("Bem-vindo, admin! Você tem acesso total ao sistema.")
elif perfil == "M":
    print ("Bem-vindo, moderador! Você pode gerenciar conteúdo e usuários.")
elif perfil == "U":
    print ("Bem-vindo, usuário! Você pode acessar o conteúdo e interagir com outros usuários.")
else:
    print ("Perfil invalido")

#Questão 4=
jogador1 = float(input("Qual a pontuação do jogador 1? "))
jogador2 = float(input("Qual a pontuação do jogador 2? "))
jogador3 = float(input("Qual a pontuação do jogador 3? "))

if jogador1 > jogador2 and jogador1 > jogador3:
    print ("O jogador 1 é o vencedor com a pontuação de", jogador1)
elif jogador2 > jogador1 and jogador2 > jogador3:
    print ("O jogador 2 é o vencedor com a pontuação de", jogador2)
elif jogador3 > jogador1 and jogador3 > jogador2:
    print ("O jogador 3 é o vencedor com a pontuação de", jogador3)
elif jogador1 == jogador2 and jogador1 > jogador3:
    print ("O jogador 1 e o jogador 2 são os vencedores com a pontuação de", jogador1)
elif jogador1 == jogador3 and jogador1 > jogador2:
    print ("O jogador 1 e o jogador 3 são os vencedores com a pontuação de", jogador1)
elif jogador2 == jogador3 and jogador2 > jogador1:
    print ("O jogador 2 e o jogador 3 são os vencedores com a pontuação de", jogador2)
else:
    print ("Todos os jogadores empataram com a pontuação de", jogador1)

#Questão 5=
produto1 = float(input("Digite o preço do produto 1: "))
produto2 = float(input("Digite o preço do produto 2: "))           
produto3 = float(input("Digite o preço do produto 3: "))

if produto1 >= produto2 and produto1 >= produto3:
    mais_caro = produto1
elif produto2 >= produto1 and produto2 >= produto3:
    mais_caro = produto2
else:
    mais_caro = produto3

if produto1 <= produto2 and produto1 <= produto3:
   mais_barato = produto1
elif produto2 <= produto1 and produto2 <= produto3:
   mais_barato = produto2
else:  
    mais_barato = produto3

diferença = mais_caro - mais_barato

print (f"O produto mais caro custa R$ {mais_caro:.2f}")
print (f"O produto mais barato custa R$ {mais_barato:.2f}")
print (f"A diferença de preço é de R$ {diferença:.2f}")   

# Só pra deixar claro que te odeio professor kkkkk fiquei meia eternidade até entender e fazer essa questão

#Questão 6=
irmaos = [
    int(input("Digite o ano de nascimento do irmão 1: ")),
    int(input("Digite o ano de nascimento do irmão 2: ")),
    int(input("Digite o ano de nascimento do irmão 3: "))
]

irmaos.sort()

print (f"Em ordem crescente, os anos de nascimento dos irmãos são: {irmaos[0]}, {irmaos[1]}, {irmaos[2]}")

if irmaos[0] == irmaos[1] == irmaos[2]:
    print ("Os irmãos são trigêmeos")
elif irmaos[0] == irmaos[1] or irmaos[0] == irmaos[2] or irmaos[1] == irmaos[2]:
    print ("Dois irmãos são gêmeos.")
else:
    print ("Nenhum dos irmãos é gêmeo.")

    # Tive que fazer assim, nenhuma maneira estava dando certo então aprendi com o youtube outra maneira de fazer e essa é bem mais eficiente.

#Questão 7=
reta1 = int(input("Digite o comprimento da reta 1: "))
reta2 = int(input("Digite o comprimento da reta 2: "))
reta3 = int(input("Digite o comprimento da reta 3: "))

if reta1 == reta2 > reta3:
    print ("As retas 1 e 2 formam um triângulo isósceles.") 
elif reta1 == reta3 > reta2:
    print ("As retas 1 e 3 formam um triângulo isósceles.")
elif reta2 == reta3 > reta1:
    print ("As retas 2 e 3 formam um triângulo isósceles.")
elif reta1 == reta2 == reta3:
    print ("As retas 1, 2 e 3 formam um triângulo equilátero.")
elif reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print ("As retas 1, 2 e 3 formam um triângulo escaleno.")
else:
    print ("As retas 1, 2 e 3 não formam um triângulo.")

#quebrei um pouco de cabeça pra entender sobre triângulo e não sobre fazer o código kkkkkkkkkk

#Questão 8=
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print ("O número é par.")
else:
    print ("O número é ímpar.")

if numero % 5 == 0:
    print ("O número é múltiplo de 5.")
else:
    print ("O número não é múltiplo de 5.")

#achei bem traquila essa questão.

#Questão 9=
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operação = input("Digite a operação desejada (+, -, *, /): ")

if operação == "+":
    resultado = n1 + n2
    print (f"O resultado da adição é: {resultado}")
elif operação == "-":
    resultado = n1 - n2
    print (f"O resultado da subtração é: {resultado}")  
elif operação == "*":
    resultado = n1 * n2
    print (f"O resultado da multiplicação é: {resultado}")  
elif operação == "/":
    if n2 == 0:
        print ("Erro: Divisão por zero")
    else:
        resultado = n1 / n2

    if resultado == int(resultado):
        if resultado % 2 == 0:
            print (f"O resultado: {resultado} é par.")
        else:
            print (f"O resultado: {resultado} é ímpar.")
    else:
        print (f"O resultado é: {resultado}")
else:
    print ("Operação inválida. Por favor, escolha entre +, -, * ou /.")

#Aqui me quebrasse em ta lokoooooo, mais de 30 minutos pra conseguir entender, claude foi um pai agora kkkkk

#Questão 10=
distancia = float(input("Digite a distância em metros: "))
operração = input("Digite a operação desejada 1 para cm, 2 para mm e 3 para km: ")
if operração == "1":
    resultado = distancia * 100
    print (f"A distância em centímetros é: {resultado} cm")
elif operração == "2":
    resultado = distancia * 1000
    print (f"A distância em milímetros é: {resultado} mm")
elif operração == "3":
    resultado = distancia / 1000
    print (f"A distância em quilômetros é: {resultado} km")
else:
    print ("Opção de conversão invalida")

# achei bem tranquila essa, nada de mais.

# Daqui pra frente é o xipotinhoo