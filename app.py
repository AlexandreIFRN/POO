
"""
    # Faça um programa em Python composto por funções que implemente o cenário descrito a seguir. 

    # Cenário (história do usuário)
    # Como Diretor Acadêmico do IFRN eu preciso de um programa para matricular estudantes em uma turma. Deve ser possível, além de inserir o estudante na turma, obter a lista de todos os matriculados, obter um aluno dada a sua matrícula e verificar se um estudante já está matriculado. 

    # Estudante: matricula, nome, curso, período(1, 2, 3...)

    # Testes:
    # 1. Adicione pelo menos 3 estudantes na turma;
    # 2. liste todos os estudantes;
    # 3 busque (e obtenha) um estudante dada a sua matrícula.

"""

# ----------------------------
# Funções
# ----------------------------
def criar_turma():
    """Cria e retorna uma turma vazia (lista de dicionários)."""
    return []


def esta_matriculado(turma, matricula):
    """Retorna True se a matrícula já estiver na turma."""
    for estudante in turma:
        if estudante["matricula"] == matricula:
            return True
    return False


def adicionar_estudante(turma, matricula, nome, curso, periodo):
    """
    Adiciona um estudante à turma.
    Retorna True se adicionou; False se já existia.
    """
    if esta_matriculado(turma, matricula):
        return False
    turma.append({
        "matricula": matricula,
        "nome": nome,
        "curso": curso,
        "periodo": periodo
    })
    return True


def listar_estudantes(turma):
    """Lista todos os estudantes da turma."""
    for estudante in turma:
        print(f'{estudante["matricula"]} - {estudante["nome"]} | {estudante["curso"]} | {estudante["periodo"]}º período')


def obter_estudante_por_matricula(turma, matricula):
    """Retorna o dicionário do estudante pela matrícula ou None."""
    for estudante in turma:
        if estudante["matricula"] == matricula:
            return estudante
    return None


# ----------------------------
#          Testes
# ----------------------------
if __name__ == "__main__":
    turma = criar_turma()

    # 1) Adicionar pelo menos 3 estudantes
    adicionar_estudante(turma, "20250001", "Ana Souza de Fulano", "TSI", 1)
    adicionar_estudante(turma, "20250002", "Bruno Almeida de Sicrano", "TSI", 2)
    adicionar_estudante(turma, "20250003", "Carla Ribeiro dos Anzóis", "Redes", 3)
    adicionar_estudante(turma, "20250004", "José Manoel Cabral", "Redes", 2)

    # 2) Listar todos
    print("=== Lista de Estudantes ===")
    listar_estudantes(turma)

    # 3) Buscar um estudante pela matrícula
    print("\n=== Busca por matrícula 20250004 ===")
    aluno = obter_estudante_por_matricula(turma, "20250004")
    if aluno:
        print(f'Encontrado: {aluno["nome"]}, {aluno["curso"]}, {aluno["periodo"]}º período')
    else:
        print("Matrícula não encontrada.")
