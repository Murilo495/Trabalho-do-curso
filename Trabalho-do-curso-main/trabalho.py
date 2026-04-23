
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

#Questão 6= do jeito que eu queria!!
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
    
#Questão 6= do jeito solicitado pelo professor.
ir1 = int(input("Digite o ano de nascimento do irmão 1: "))
ir2 = int(input("Digite o ano de nascimento do irmão 2: "))
ir3 = int(input("Digite o ano de nascimento do irmão 3: "))

if ir1 == ir2 == ir3:
    print ("Os irmãos são trigêmeos")
elif ir1 == ir2 or ir1 == ir3 or ir2 == ir3:
    print ("Dois irmãos são gêmeos.")
else:
    print ("Nenhum dos irmãos é gêmeo.")

if ir1 < ir2 and ir1 < ir3:
    if ir2 < ir3:
        print (f"Em ordem crescente, os anos de nascimento dos irmãos são: {ir1}, {ir2}, {ir3}")
    else:
        print (f"Em ordem crescente, os anos de nascimento dos irmãos são: {ir1}, {ir3}, {ir2}")
elif ir2 < ir1 and ir2 < ir3:
    if ir1 < ir3:
        print (f"Em ordem crescente, os anos de nascimento dos irmãos são: {ir2}, {ir1}, {ir3}")
    else:
        print (f"Em ordem crescente, os anos de nascimento dos irmãos são: {ir2}, {ir3}, {ir1}")
else:
    if ir1 < ir2:
        print (f"Em ordem crescente, os anos de nascimento dos irmãos são: {ir3}, {ir1}, {ir2}")
    else:
        print (f"Em ordem crescente, os anos de nascimento dos irmãos são: {ir3}, {ir2}, {ir1}")


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

#Questão 11=
valor = float(input("Qual o valor da compra: ")) # Pergunta o valor da compra e guarda o resultado
categoria = input("Qual a sua categoria? a) comum b) vip c) funcionario: ") # Pergunta a categoria 
vip = valor * 10 / 100 # Calcula o desconto do vip de acordo com o valor total da compra
funcionario = valor * 20 / 100 # Calcula o desconto do funcionario de acordo com o valor total da compra

if categoria == "vip": # Se a categoria foi igual a "vip"
    total = valor-vip # Variavel total faz a operação valor - vip, valor da compra menos o desconto

elif categoria == "funcionario": # Se a categoria foi igual a "funcionario"
    total = valor-funcionario # Variavel total faz a operação valor - funcionario, valor da compra menos o desconto

else: # Aqui é para o comum
    total = valor # Mantém o valor total da compra, por que o cliente comum não tem desconto

print("Valor total da compra: ", total) # Faz o print do valor total da compra, já calculando o desconto, de acordo com a categoria

#Questão 12= 
ano = int(input("Digite o ano com 4 números: ")) 

if ano % 4 == 0: 
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("O ano é Bissexto")
else:
    print("o ano é comum")

#Questão 13=
ataque = int(input("Digite o valor do Ataque do jogador: "))
defesa = int(input("Digite a Defesa do monstro: "))
dado = int(input("Digite o resultado do dado de 20 faces (1 a 20): "))

if dado == 20:
    print ("Acerto crítico")
    dano = ataque * 2 
    print (f"O dano causado é: {dano}")
elif dado == 1:
    print ("Falha crítica")
    dano = 0
    print (f"O dano causado é: {dano}")
else:
    dano = (ataque + dado) - defesa
    if dano < 0:
        dano = 0
    print (f"O dano causado é: {dano}")

#Questão 14=
usuario = input("Digite o nome de usuário: ")
senha = int(input("Digite a senha: "))

if usuario == "admin" and senha == 1234:
    print ("Acesso liberado")
elif usuario == "admin" and senha != 1234:
    print ("Senha incorreta")
else:
    usuario != "admin" and senha == 1234
    print ("Usuário não encontrado no sistema")

#Questão 15=

#Questão 16=
cor = input("Digite a cor do semáforo (vermelho, amarelo ou verde): ")
velocidade = float(input("Digite a velocidade do veículo em km/h: "))

if cor == "vermelho":
    if velocidade > 0:
        print ("Multa Gravíssima por avanço.")
    else:
        print ("Condução segura.")
elif cor == "amarelo":
    if velocidade > 60:
        print ("Multa por excesso de velocidade no amarelo.")
    else:
        print ("Condução segura.")

elif cor == "verde":
    if velocidade > 80:
        print ("Multa por excesso de velocidade.")
    else:
        print ("Condução segura.")

#Questão 17=
bruto = float(input("Diga seu salario bruto: "))

if bruto <= 2000:
    salario = bruto
    imposto = 0
elif 2000<= bruto <=4000:
  salario = bruto - (bruto * 10/100)
  imposto = bruto * 10/100
else:
  salario = bruto - (bruto * 20/100)
  imposto = bruto * 20/100
print(f"Salário líquido: {salario}")
print(f"Imposto: {imposto}")

#Questão 18=
dias = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))

if mes < 1 or mes > 12:
    print ("Data inválida")
elif mes == 2:
    if dias < 1 or dias > 28:
        print("Data inválida")
    else:
        print ("Data válida")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dias < 1 or dias > 30:
        print ("Data inválida")
    else:
        print ("Data válida")
else:
    if dias < 1 or dias > 31:
        print ("Data inválida")
    else:
        print ("Data válida")

#Questão 19=
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
faltas = int(input("Digite o número de faltas: "))
media = (nota1 + nota2) / 2

if media >= 7 and faltas <= 10:
    print ("Aprovado")

elif media < 7 and faltas <= 10:
    print ("Exame final")
elif faltas > 10:
    print ("Reprovado por faltas")

#Questão 20=









