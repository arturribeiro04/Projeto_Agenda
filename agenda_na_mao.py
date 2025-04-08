print("\n-----------------------------------------------------------------\n")
AGENDA_SIMPLES = {

    "João" : {

        "Tel" : "99999-0001",
        "Email": "joao@email.com.br",
        "Endereco": "Rua do João",
    },

    "Maria" : {

        "Tel" : "99999-0002",
        "Email": "maria@email.com.br",
        "Endereco": "Estrada da Maria",
    },

    "José" : {

        "Tel" : "99999-0003",
        "Email": "jose@email.com.br",
        "Endereco": "Avenida do José",
    },

    "Ana" : {

        "Tel" : "99999-0004",
        "Email": "ana@email.com.br",
        "Endereco": "Travessa da Ana",
    },
    
}

print("\n--- ACESSAR O CONTATO DA MARIA ---")
print(AGENDA_SIMPLES['Maria'])

print("\n--- ACESSAR O ENDEREÇO DA ANA ---")
print(AGENDA_SIMPLES['Ana']['Endereco'])

print("\n--- ALTERAR O TELEFONE DO JOSÉ ---")
AGENDA_SIMPLES['José']['Tel'] = "90000-0003"
print(AGENDA_SIMPLES['José']['Tel'])

print("\n--- ADICIONAR AS INFOS DA RENATA ---")

AGENDA_SIMPLES["Renata"] = {

    "Tel" : "91234-5678",
    "Email": "renata@email.com.br",
    "Endereco": "Rodovia da Renata",

}

print(AGENDA_SIMPLES['Renata'])

print("\n--- MOSTRAR A AGENDA ---")

for contato in AGENDA_SIMPLES:

    print(contato)

print("\n--- REMOVER A ANA DA AGENDA ---")

AGENDA_SIMPLES.pop("Ana")

for contato in AGENDA_SIMPLES:

    print(contato)
    
print("\n-----------------------------------------------------------------\n")