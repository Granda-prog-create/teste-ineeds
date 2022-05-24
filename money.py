#Nome do banco
print('=' * 30)
print('{:^30}'.format('Bem vindo ao Banco Virtual'))
print('=' * 30)

#Inserir valor 
valor = int(input('Qual valor você quer sacar? R$ '))
total = valor

#cédulas
ced = 200
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced +=1
    else:
        if totalced >0:
         print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 2:
             ced = 2
        if total == 0:
            break   
print('=' *30)
print('{:^30}'.format('Obrigado por usar o Banco Virtual! Tenha um excelente dia!'))
print('=' * 30)
        
                
                
                  
              
               