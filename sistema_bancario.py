saldo_conta = 0

deposito = 0
saque = 0

limite = 500

numero_saques = 0
LIMITE_SAQUES = 3


extrato = f'''  
                       
          !!! Extrato !!! \n
-----------------------------------------\n
saldo da conta = R$ {saldo_conta:.2f}\n
'''
menu = f''' 
     ######   Menu ######
     #  (d) - Deposito  #
     #  (s) - Saque     #
     #  (e) - Extrato   #
     #  (q) - sair      #
                     '''


while True :
    opcao = input(menu)  
    if opcao == 'd':
        valor_deposito = float(input('digite o valor de deposito: R$ ' ))
        if valor_deposito > 0:
            saldo_conta += valor_deposito    
            extrato += f'Deposito de R$ {valor_deposito:.2f} \n'
            extrato = extrato.replace(f'saldo da conta = R$ {saldo_conta - valor_deposito:.2f}', f'saldo da conta = R$ {saldo_conta:.2f}')
        else:
            print('Depositos só valores positivos !!!!')
       
    elif opcao == 's':
        if numero_saques < LIMITE_SAQUES:
            saque = float(input('Digite o valor de saque : R$ '))
            if saque < 500 and saque <= saldo_conta:
                saldo_conta -= saque
                numero_saques += 1
                extrato += f'Saque de R$ {saque:.2f} \n'
                extrato = extrato.replace(f'saldo da conta = R$ {saldo_conta + saque:.2f}', f'saldo da conta = R$ {saldo_conta:.2f}')
            else:
                if saque > 500:
                    print('Não é possivel fazer Saque maior que R$500,00 !!!')
                else:
                    print('Não tem saldo suficiente para realizar o saque')
        else: 
            print('Operação não efetuada !!! Só pode ser realizado 3 saques por dia')
                
                                    
    elif opcao == 'e':
        print (extrato)
      
        
        
    elif opcao == 'q':
        break     
        
    else :
        print('Opção invalida, selecione uma opção novamente.')

