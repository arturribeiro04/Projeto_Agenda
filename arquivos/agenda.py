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

        print("NOME: ", contato)
        print("TELEFONE: ", AGENDA[contato]['telefone'])
        print("ENDEREÇO: ", AGENDA[contato]['endereco'])
        print("E-MAIL: ", AGENDA[contato]['email'])
        print("-" * 120)

def buscar_contato(contato):
   
    print("NOME: ", contato)
    print("TELEFONE: ", AGENDA[contato]['telefone'])
    print("ENDEREÇO: ", AGENDA[contato]['endereco'])
    print("E-MAIL: ", AGENDA[contato]['email'])
    print("-" * 120)


print("-" * 20 + "MOSTRAR TODOS OS CONTATOS" + "-" * 20)

mostrar_contatos()
buscar_contato('maria')