# Biblioteca de funções pra trabalhar com SQLite

import sqlite3

# FUNÇÃO DE CRIAR TABELAS --------------------------------------------
def criarTabela(nomeDB, nomeTabela):
    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    query =f'''CREATE TABLE IF NOT EXISTS {nomeTabela} (
        "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "nome" TEXT NOT NULL,
        "sobrenome" TEXT NOT NULL,
        "email" TEXT NOT NULL
    );'''
    cursor.execute(query)
    conn.commit()
    conn.close()

# FUNÇÃO DE INSERIR DADOS --------------------------------------------
def inseriDados(nomeDB, nomeTabela, nome, sobrenome, email):
    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    query =f'''INSERT INTO {nomeTabela} (nome, sobrenome, email)
        VALUES ("{nome}", "{sobrenome}", "{email}");
    '''
    cursor.execute(query)
    conn.commit()
    conn.close()

# FUNÇÃO DE ATUALIZAR DADOS ------------------------------------------
def atualizarDados(nomeDB, nomeTabela, nome, sobrenome, email, id):

    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    if len(nome) != 0 and nome != '\r':

        query =f'''
            UPDATE {nomeTabela}
            SET nome = "{nome}"
            WHERE id = "{id}";
        '''
        cursor.execute(query)
        conn.commit()

    if len(sobrenome) != 0 and sobrenome != '\r':

        query =f'''
            UPDATE {nomeTabela}
            SET sobrenome = "{sobrenome}"
            WHERE id = "{id}";
        '''
        cursor.execute(query)
        conn.commit()

    if len(email) != 0 and email != '\r':

        query =f'''
            UPDATE {nomeTabela}
            SET email = "{email}"
            WHERE id = "{id}";
        '''
        cursor.execute(query)
        conn.commit()

    conn.close()

# FUNÇÃO PARA APAGAR DADOS ------------------------------------------
def apagarDado(nomeDB, nomeTabela, id):
    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    query =f'''DELETE FROM {nomeTabela} WHERE id = "{id}";'''

    cursor.execute(query)
    conn.commit()
    conn.close()

# FUNÇÃO PARA SELECIONAR TODOS OS DADOS -----------------------------
def selecionarTodosDados(nomeDB, nomeTabela):
    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    query =f'''SELECT * FROM "{nomeTabela}";'''

    cursor.execute(query)
    dados = cursor.fetchall()

    conn.commit()
    conn.close()

    return dados

# FUNÇÃO PARA SELECIONAR OS DADOS POR ID ----------------------------
def selecionarDadoPorId(nomeDB, nomeTabela, id):
    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    query =f'''SELECT * FROM "{nomeTabela}" WHERE id = "{id}";'''

    cursor.execute(query)
    dados = cursor.fetchall()

    conn.commit()
    conn.close()

    return dados

# FUNÇÃO PRINCIPAL DE TESTE-------------------------------------------
def main():
    nomeDB = "clientes.db"
    nomeTabela = "clientes"

    # criarTabela(nomeDB, nomeTabela)
    # inseriDados(nomeDB, nomeTabela, "Lara", "Silva", "lara@sp.br")
    # atualizarDados(nomeDB, nomeTabela, "Bia", "Castro", "bia@sp.br", 1)
    # apagarDado(nomeDB, nomeTabela, 1)
    todosRegistros = selecionarTodosDados(nomeDB, nomeTabela)
    print(todosRegistros)
    
    registroPorId = selecionarDadoPorId(nomeDB, nomeTabela, 2)
    print(registroPorId)

if __name__ == "__main__":
    main()