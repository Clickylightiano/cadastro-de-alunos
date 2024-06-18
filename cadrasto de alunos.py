class Aluno:
    def __init__(self, nome, matricula, curso, data_nascimento):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.data_nascimento = data_nascimento

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, nova_matricula):
        self.matricula = nova_matricula

    def get_curso(self):
        return self.curso

    def set_curso(self, novo_curso):
        self.curso = novo_curso

    def get_data_nascimento(self):
        return self.data_nascimento

    def set_data_nascimento(self, nova_data_nascimento):
        self.data_nascimento = nova_data_nascimento

    def to_string(self):
        return f"Nome: {self.nome}\nMatrícula: {self.matricula}\nCurso: {self.curso}\nData de Nascimento: {self.data_nascimento}"

class SistemaCadastroAlunos:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def buscar_aluno_por_nome(self, nome):
        for aluno in self.alunos:
            if aluno.get_nome().lower() == nome.lower():
                return aluno
        return None

    def buscar_aluno_por_matricula(self, matricula):
        for aluno in self.alunos:
            if aluno.get_matricula() == matricula:
                return aluno