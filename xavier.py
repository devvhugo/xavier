print("_________________________________")
print("Olá! Bem Vindo ao Prof. Xavier")
nome = input("Qual seu nome? " )
game = 0
while(game == 0):
	
	print(f"{nome} pense em um número")
	r1 = input ("Pensou? s/n ")
	print("_________________________________")
	if r1 == "s":
		print("Soma ele por 2")
		r2 = input("somou? s/n ")
		print("_________________________________")
		if r2 == "s":
			print("Soma mais 8, e subtraia pelo número que pensou no início")
			print(f"Pronto para a reposta {nome}?")
			input("Aperte Enter")
			print("_________________________________")
			print("A responsta é: 10")
			r3 = input("Quer continuar jogando? s/n ")
			print("_________________________________")
			if r3 == "n":
				print(f"Obrigado por jogar {nome}!")
				game = 1
		else:
			print("Nem sabe brincar! rsrs")	
			r4 = input("Quer continuar jogando? s/n ")
			if r4 == "n":
				game = 1
	else:
		print(f"Brincamos depois então {nome}. :-)")	
		game = 1
else:
	print("Volte sempre! ;-)")
