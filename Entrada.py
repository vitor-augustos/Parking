from datetime import datetime
from Veiculo import Veiculo

lista = []

p: str = ''

while p != '1':

    print('Digite a opção desejada')
    print('[\033[0;32m1\033[m] ENCERRAR PROGRAMA')
    print('[\033[0;32m2\033[m] ENTRAR NOVO VEÍCULO')
    print('[\033[0;32m3\033[m] SAIR VEÍCULO')
    print('[\033[0;32m4\033[m] LISTAR VEÍCULOS ESTACIONADOS')

    p = input('')
    data = datetime.today()

    if p == '1':
        exit()

    if p == '2':
        placa: str = input('Digite a placa do veículo: ')

        print('-------------------------------------------------')
        print(f'Horário de entrada: {data} \nplaca {placa}')
        print('-------------------------------------------------')

        veiculo_object = Veiculo(placa, data)

        lista.append(veiculo_object)
    #  array de objetos

    if p == '3':
        print('Volte sempre.\n')

    if p == '4':
        print('-------------------------------------------------')
        print('       *** VEICULOS ESTACIONADOS ***')
        print('-------------------------------------------------')
        num: int = 1
        for v in lista:
            print(f'{num} {v.placa}: {v.hrentrada}')
            print('-------------------------------------------------')
            num+=1
        print(f'Total de veiculos estacionados = {len(lista)}')