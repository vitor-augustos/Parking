from datetime import datetime

from Veiculo import Veiculo

lista = []

p = ''

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
        print('Horário de entrada: {} \nplaca {}\n'.format(data, placa))

        veiculo_object = Veiculo(placa, data)

        lista.append(veiculo_object)
    #  array de objetos

    if p == '3':
        print('Volte sempre.\n')

    if p == '4':
        for v in lista:
            print(f'{v.placa}: {v.hrentrada}')
#        print('{}\n'.format(lista))
