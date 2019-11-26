import requests


def buscar_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    response_data = response.json()
    return response_data

def main():
    print('####################')
    print('### Consulta CEP ###')
    print('####################')
    print()

    cep = input('Digite o CEP para a consulta: ')
    if len(cep) != 8:
        exit('Quantidade de digitos invalidos!')

    address_data = buscar_cep(cep)
    if 'erro' not in address_data:
        info_cep = """
        ==> CEP ENCONTRADO <==
        CEP: {cep}
        Logradouro: {logradouro}
        Complemento: {complemento}
        Bairro: {bairro}
        Cidade: {localidade}
        Estado: {uf}
        """
        print(info_cep.format(**address_data))

    else:
        print('{}: CEP invalido'.format(cep))

    print("-----------------------------------------------")
    option = int(input('Deseja realizar uma nova consulta?\n1.Sim\n2.Não\n==> '))
    print("-----------------------------------------------\n")
    if option == 1:
        main()
    else:
        print('Saindo')

if __name__ == "__main__":
    main()
