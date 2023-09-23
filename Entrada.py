from datetime import datetime
from Veiculo import Veiculo

lista = []

p: str = ''
custoPorSegundo = 0.05

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
        print(f'Horário de entrada: \033[0;32m{data.strftime("%H:%M:%S")}\033[m \nplaca [\033[0;32m{placa}\033[m]')
        print('-------------------------------------------------')

        veiculo_object = Veiculo(placa, data)

        lista.append(veiculo_object)
    #  array de objetos

    if p == '3':
        placaSaida: str = input('Digite a placa do veículo: ')
        veiculoEstacionado = {}
        for veiculo in lista:
            if veiculo.placa == placaSaida:
               veiculoEstacionado = veiculo
        if veiculoEstacionado == {}:
            print(f'Veículo não encontrado pela placa: \033[0;32m{placaSaida}\033[m\n')
        else:
            lista.remove(veiculoEstacionado)

            permanencia = data - veiculoEstacionado.hrentrada
            valor = permanencia.seconds * custoPorSegundo

            print(f'Permanêcia: \033[0;32m{permanencia.seconds}\033[m segundos')
            print(f'Custo: \033[0;32m' "%.2f" %valor,"\033[m")

    if p == '4':
        print('-------------------------------------------------')
        print('       *** VEICULOS ESTACIONADOS ***')
        print('-------------------------------------------------')
        num: int = 1
        for v in lista:
            print(f'[\033[0;32m{num}\033[m] {v.placa}: \033[0;32m{v.hrentrada.strftime("%H:%M:%S")}\033[m')
            print('-------------------------------------------------')
            num+=1
        print(f'Total de veiculos estacionados = [\033[0;32m{len(lista)}\033[m]\n')