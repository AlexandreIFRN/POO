#Lista (list)
# 👉 É uma coleção mutável (pode mudar).
# 👉 Aceita elementos repetidos.
# 👉 Mantém a ordem em que os itens foram adicionados.

# frutas = ["maçã", "banana", 'uva']

# for i in range(len(frutas)):
#     print(frutas[i])

# for fruta in frutas:
#     print(fruta)


# for i, fruta in enumerate(frutas):
#     print(i, fruta)



# Tupla (tuple)

# 👉 Igual a lista, mas é imutável (não pode mudar).
# 👉 Boa para dados que não devem ser alterados.
# 👉 Também mantém a ordem.
# cores = ("vermelho", "verde", "azul")

# for cor in cores:
#     print(cor)


# Dicionário (dict)

# 👉 É uma coleção de pares chave: valor.
# 👉 Não permite chaves duplicadas.
# 👉 Muito usado para representar objetos/entidades.

# aluno = {

#     "matricula": "20250001",
#     "nome": "Alexandre",
#     "curso": "TSI",
#     "periodo": "2"
# }

# print(aluno,"Alexandre")


# Conjunto (set)

# 👉 É uma coleção de valores únicos (não aceita repetição).
# 👉 Não garante ordem.
# 👉 Bom para operações matemáticas: união, interseção, diferença.



a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("Conjunto a:", a)
print("Conjunto b:", b)
print("a união b:", a | b)
print("a interseção b:", a & b)
print("Diferença a menos b:", a - b)
print("Difereça b menos a", sorted(b - a))

