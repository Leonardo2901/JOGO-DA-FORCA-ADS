import os, random, time
clear = lambda: os.system('cls')
Enforcou = False
Acertou = False
numero_tentativas = 0
Acertos = 0

l = 0 # Usado no 'for' na linha 183
cont = 0
c = [] # Contador de letras digitadas, usado no pede_chute e como p1 da def placar
quantidade = []
qnt = []
dicas = [] # Se errar 3 vezes aparece uma dica
palavras = []
repetiu = 0
chutet = 0 # Transforma o chute em string pra ver se tem apenas letras

################################### VISUAL #######################################

def mensagem_abertura():
	print(" ==================================================")
	print("|                  JOGO DA FORCA                   |")
	print(" ==================================================")

def grupo():
	print("|         LER AVISO NA PASTA, ANTES DE RODAR      |") 
	print("|                     BEM-VINDO                   |")
	print(" ==================================================")


def placar(p1, p2):
	mensagem_abertura()
	if numero_tentativas == 0:
		print("              |----- ")
		print("              |    | ")
		print("              |     ")
		print("              |    ")
		print("              |     ")
		print("              |     ")
		print("              |")
	if numero_tentativas == 1:
		print("              |----- ")
		print("              |    | ")
		print("              |    O ")
		print("              |     ")
		print("              |     ")
		print("              |     ")
		print("              |")
	if numero_tentativas == 2:
		print("              |----- ")
		print("              |    | ")
		print("              |    O ")
		print("              |    | ")
		print("              |    | ")
		print("              |     ")
		print("              |")
	if numero_tentativas == 3:
		print("              |----- ")
		print("              |    | ")
		print("              |    O ")
		print("              |   /| ")
		print("              |    | ")
		print("              |     ")
		print("              |")
	if numero_tentativas == 4:
		print("              |----- ")
		print("              |    | ")
		print("              |    O ")
		print("              |   /|\\ ")
		print("              |    | ")
		print("              |     ")
		print("              |")
	if numero_tentativas == 5:
		print("              |----- ")
		print("              |    | ")
		print("              |    O ")
		print("              |   /|\\")
		print("              |    | ")
		print("              |   /  ")
		print("              |")
	if numero_tentativas == 6:
		print("              |----- ")
		print("              |    | ")
		print("              |    O ")
		print("              |   /|\\")
		print("              |    | ")
		print("              |   / \\ ")
		print("              |")

	lu = "".join(p1) #letras usadas
	junta = "".join(p2)
	print("                           "+str(junta)+"")
	print("\n  Letras Usadas pelo Apedeuta: "+str(lu)+"                       ")
	print(" --------------------------------------------------")

##################################### DICAS #########################################

def dica():
	if numero_tentativas < 3:
		print(f"               DICA: Países, não tem mais dicas   ")
		print(" --------------------------------------------------")
	if numero_tentativas >= 3:
		ajuda = dica_secreta
		print(f"             DICA: {ajuda}                  ")
		print(" --------------------------------------------------")

################################ CARREGA LISTA TXT ##################################

def carrega_palavra_secreta():
	global palavra_secreta, dica_secreta
	dicas = []
	palavras = []
	arquivo = open("palavras_secretas.txt", "r")
	texto = arquivo.read()
	lista = texto.split('\n')
	ls = "".join(lista).upper() #lista string
	lista2 = ls.split(';')
	for i in range (len(lista2)):
		if i % 2 == 0:
			palavras.append(lista2[i])
		elif i % 2 == 1:
			dicas.append(lista2[i])
	maxx = len(palavras) - 1
	numero_aleatorio = random.randint(0, maxx)
	palavra_secreta = palavras[numero_aleatorio]
	dica_secreta = dicas[numero_aleatorio]
	arquivo.close()

################################# QUANTIDADE DE LETRAS ###############################

def inicializa_letras_acertadas():
	global letras
	letras = list(palavra_secreta)
	i = 0
	global quantidade
	while i < len(letras):
		quantidade.append('_')
		i = i + 1

####################################### PERGUNTA ######################################

def pede_chute():
	global chute, c, repetiu, chutet
	chute = input("  Chute uma letra: ").upper()
	chutet = chute.isalpha()
	if chutet == True:
		if chute[0] in c:
			repetiu = 1
		else:
			c.append(chute[0])

###################################### SE ACERTAR #####################################

def chute_correto():
	global Acertos, qnt
	qnt[l] = chute[0]
	Acertos = Acertos + 1

####################################### INICIA ########################################

comeca = 'S'
mensagem_abertura()
grupo()
time.sleep(4)
while comeca == 'S':
	carrega_palavra_secreta()
	inicializa_letras_acertadas()
	letras_acertadas = letras[:]
	qnt = quantidade[:]

	while Enforcou == False and Acertou == False:
		cont = 0
		clear()
		placar(c, qnt)
		dica()
		pede_chute()
		if chutet == True:
			if repetiu == 0:
				for l in range(len(letras_acertadas)):
					if chute[0] == letras_acertadas[l]:
						chute_correto()
						cont = cont + 1
				if cont == 0:
					numero_tentativas = numero_tentativas + 1
					print("  Errou :(")
					time.sleep(1)
				else:
					print("  Acertou :)")
					time.sleep(1)
			else:
				print("  Voce ja chutou essa letra, chute outra!")
				repetiu = 0
				time.sleep(1)
		else:
			print(" Apenas Letra, não usamos números!")
			time.sleep(1)
		clear()
		placar(c, qnt)
		dica()
		if Acertos == len(qnt):
			time.sleep(1)
			Acertou = True
		if numero_tentativas == 6:
			time.sleep(1)
			Enforcou = True

	if Acertou == True:
		print(" Finalmente em, depois de tantos chutes. O APEDEUTA GANHOU!")
	if Enforcou == True:
		p = "".join(palavra_secreta)
		print(f"  PERDEU\n  A PALAVRA ERA {p}")
	pergunta = input('\n  DESEJA JOGAR NOVAMENTE? [S/N]: ').upper()
	if pergunta[0] == 'S':
		clear()
		Enforcou = False
		Acertou = False
		numero_tentativas = 0
		Acertos = 0
		l = 0
		cont = 0
		repetiu = 0
		del quantidade[:]
		del qnt[:]
		del c[:]
		del dicas[:]
		del palavras[:]
		continue
	else:
		clear()
		mensagem_abertura()
		grupo()
		break

input("\n\t\tOBRIGADO POR JOGAR, DE O SEU MELHOR NA PROXIMA...")
