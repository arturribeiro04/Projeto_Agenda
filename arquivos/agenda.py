AGENDA = {}

AGENDA['guilherme'] = {

    'telefone' : '91122-3344',
    'email' : 'guilherme@email.com.br',
    'endereco' : 'Rua do Guilherme, 23',

}

AGENDA['maria'] = {

    'telefone' : '92233-4455',
    'email' : 'maria@email.com.br',
    'endereco' : 'Avenida da Maria, 1023',

}

def mostrar_contatos():

    for contato in AGENDA:

        buscar_contato(contato)

def buscar_contato(contato):
   
    print("NOME: ", contato)
    print("TELEFONE: ", AGENDA[contato]['telefone'])
    print("ENDEREÇO: ", AGENDA[contato]['endereco'])
    print("E-MAIL: ", AGENDA[contato]['email'])
    print("-" * 120)

def adicionar_contato(contato,telefone,endereco,email):

    AGENDA[contato] = {

        'telefone' : telefone,
        'email' : email,
        'endereco' : endereco,

    }

print("-" * 20 + "ADICIONAR UM CONTATO" + "-" * 20)

adicionar_contato('Renato','93344-6677','Estrada do Renato','renato@email.com.br')

print("-" * 20 + "MOSTRAR TODOS OS CONTATOS" + "-" * 20)

mostrar_contatos()

print("-" * 20 + "MOSTRAR UM CONTATO" + "-" * 20)

buscar_contato('maria')