import mysql.connector 
from mysql.connector import Error

def connect_to_db():
    try:
        # Conectar ao banco de dados
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'pytestes'
        )
        return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados mysql: {e}")
        return None

def create_contact(nome, telefone):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute('''
            INSERT INTO Agenda (nome, telefone)
            VALUES (%s, %s);
            ''', (nome, telefone))
            # Recuperando id gerado 
            contact_id = cursor.lastrowid
            conn.commit()
            print(f"Contato adicionado com ID: {contact_id}")
            
        except Error as e:
            print(f"Erro ao adicionar contato: {e}")
        finally:
            cursor.close()
            conn.close()
            
def read_contacts():
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute('''
            SELECT id, nome, telefone FROM Agenda;''')
            contacts = cursor.fetchall()
            for contact in contacts:
                print(f"ID: {contact[0]}, NOME: {contact[1]}, TELEFONE: {contact[2]}")
                
        except Error as e:
            print(f"Erro ao ler contatos")
        finally:
            cursor.close()
            conn.close()

def update_contact(contact_id, novo_nome, novo_telefone):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute('''
            UPDATE Agenda
            SET nome = %s, telefone = %s
            WHERE id = %s;
            ''', (novo_nome, novo_telefone, contact_id))
            conn.commit()
            print("Contato atualizado com sucesso.")
        except Error as e:
            print(f"Erro ao atualizar contato: {e}")
        finally:
            cursor.close()
            conn.close()
            
def delete_contact(contact_id):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute('''
            DELETE FROM Agenda
            WHERE id = %s
            ''', (contact_id,))
            conn.commit()
            print("Contato deletado com sucesso.")
        except Error as e:
            print(f"Erro ao deletar contato: {e}")
        finally:
            cursor.close()
            conn.close()

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar novo contato")
        print("2. Mostrar todos os contatos")
        print("3. Atualizar um contato")
        print("4. Deletar um contato")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")
        
        match choice:
            case "1":
                nome = input("Digite o nome: ")
                telefone = input("Digite o telefone: ")
                create_contact(nome, telefone)
            case "2":
                read_contacts()
            case "3":
                contact_id = int(input("Digite o ID do contato para atualizar: "))
                novo_nome = input("Digite o novo nome: ")
                novo_telefone = input ("Digite o novo telefone: ")
                update_contact(contact_id, novo_nome, novo_telefone)
            case "4":
                contact_id = int(input("Digite o ID do contato para deletar: "))
                delete_contact(contact_id)
            case "5":
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
        