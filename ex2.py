class aluno:
    def __init__(self, nome,nota1,nota2,media):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = media
    def mediaAluno (self):
        print(f"A media do aluno {self.nome} é {self.media}")

nome = input("Digite o nome do aluno:")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
media = (nota1+nota2) / 2
aluno1 = aluno(nome,nota1,nota2,media)


aluno1.mediaAluno()

        