class Carros: #Aqui estamos criando uma class ( molde ) para ajudar na criação do nosso objeto
    def __init__(self, Modelo, Ano): #Criando um método para a nossa classe
       
        self.Modelo = Modelo #atributo time
        self.Ano = Ano #atributo CPF
                
 
#Criando nosso primeiro objeto, e passando como argumentos os atributos pessoais 
Carro1 = Carros("Fiat", "2020")

#Exibir no Vars
print (vars(Carro1))

class Produto: #Aqui estamos criando uma class ( molde ) para ajudar na criação do nosso objeto
    def __init__(self, Valor, Cor, Nome): #Criando um método para a nossa classe
       
        self.Valor = Valor #atributo time
        self.Cor = Cor #atributo CPF
        self.Nome = Nome    
    def apresentacao (self):
        print (f"O {self.Nome} é tem o valor {self.Valor}, e a cor {self.Cor}")


#Criando nosso primeiro objeto
Nome = input ("Digite o nome do produto: ")
Valor = int(input ("Digite o valor do produto: "))                
Cor = input ("Digite a cor: ")
Garrafa = Produto (Valor, Cor, Nome)

#Chamar método
Garrafa.apresentacao()

Nome = input ("Digite o nome do Produto: ")
Valor = int(input("Digite o valor do produto: "))
Cor = input ( "Digite a cor: ")
Mouse = Produto ( Valor, Cor, Nome)

Mouse.apresentacao()

class Aluno:
    def __init__ (self, nome, nota, nota1,media):
        self.nome = nome
        self.nota = nota
        self.nota1 = nota1
        self.media = media
    def mediaAluno(self):
        print (f"O Aluno {self.nome}, teve a média {self.media}.")

nome = input ("Digite o nome:")
nota1 = int(input("Digite sua nota:"))
nota2 = int(input ("Digite sua nota:"))
media = (nota1 + nota2) / 2
Aluno1 = Aluno(nome,nota1,nota2,media)

Aluno1.mediaAluno()