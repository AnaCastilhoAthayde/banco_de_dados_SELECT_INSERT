import sqlite3

#Criamos a conexão com o banco e guardamos na variavel 'banco
banco = sqlite3.connect('ricardaofather.db')


#Criamos a variavel  cursor e colocamos em uma variavel 
cursor = banco.cursor()

# UPDATE 
cursor.execute("UPDATE funcionarios  SET cargo = 'Analista' WHERE id = 26")


#Inserindo na tabela desejada os valores 
#cursor.execute("INSERT INTO empresa VALUES(6,'amoxilina','500mg',15,'anvisa','antibiótico',05/26)")

#enviando os dados 
banco.commit()

#printar a informação 
#cursor.execute("SELECT salario FROM funcionarios")
#print(cursor.fetchall())    