import sqlite3

#Criamos a conexão com o banco e guardamos na variavel 'banco
banco = sqlite3.connect('escola.db')


#Criamos a variavel  cursor e colocamos em uma variavel 
cursor = banco.cursor()

#Criando a tabela  pessoas com os campos necessários 
# cursor.execute("CREATE TABLE farmacia(id interger,nome text,dosagem VARCHAR(50),preço decima(10,2),fabricante VARCHAR(100),categoria VARCHAR(50),data_validade date)")


#Inserindo na tabela desejada os valores 
#cursor.execute("INSERT INTO empresa VALUES(6,'amoxilina','500mg',15,'anvisa','antibiótico',05/26)")

#enviando os dados 
banco.commit()

#printar a informação 
cursor.execute("SELECT nome,nota FROM alunos")
print(cursor.fetchall())