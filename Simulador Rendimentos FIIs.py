#Calculadora de Rendimentos em FII's

count = 1
rendimentosMensal = 0.0
rendimentosTotal = 0.0
rendimentos = 0.0
quantCotasAdicionais=0

#Obtenção de dados
print("Digite a quantidade inicial de cotas")
quantCotas = int(input())

print("Digite a quantidade de cotas compradas mensalmente:")
quantCotasMensais = int(input())

print("Digite o valor pago por cota")
valorCota= float(input())

print("Digite a quantidade de períodos")
periodos= int(input())

print("Digite o DY médio do FII")
valorRentabilidade = float(input())

while (count < (periodos+1)):  #Executar o cálculo
   x = 0  # Resetar o contador de cotas adicionais

   rendimentosMensal = valorCota * valorRentabilidade * quantCotas
   rendimentosTotal = rendimentosTotal +rendimentosMensal
   rendimentos = rendimentos + rendimentosMensal

   print("O rendimento do mês", count, "é: R$",rendimentosMensal)
   print("O total de rendimentos disponível é: R$", rendimentos)
   print("A quantidade de cotas atual é:", quantCotas)

   while rendimentos > valorCota:
      rendimentos = rendimentos - valorCota
      quantCotas = quantCotas + 1
      quantCotasAdicionais= quantCotasAdicionais+1
      x = x+1
   if x!=0:
      print("Foram compradas", x,"cotas com os rendimentos!")

   #Atualizar contadores
   quantCotas = quantCotas + quantCotasMensais
   count = count + 1

   print("")


#Imprimir informações adicionais
print("O total de rendimentos disponível é: R$", round(rendimentos, 2))
print("O total de rendimentos acumulado é: R$",round(rendimentosTotal, 2))
print("A quantidade total de cotas é:", quantCotas,"unidades.")
print("O total investido em", periodos,"meses, comprando", quantCotasMensais, "cotas mensais, por R$", valorCota,"é: R$", (valorCota * periodos * quantCotasMensais), ", gerando um lucro de ", round(((rendimentos + (quantCotasAdicionais * valorCota))/(valorCota * periodos * quantCotasMensais))*100,1), "%")
print("O total de patrimônio acumulado é:R$", round(quantCotas*valorCota+rendimentos,2))
print("A renda passiva mensal é: R$", round(quantCotas*valorRentabilidade*valorCota,2))
