class Cor:
    def __init__(self, nome: str, hexadecimal: str, conexao):
        conexao.run(
            'MERGE (:Cor {nome: $nome, hexadecimal: $hexadecimal})',
            parameters={'nome': nome, 'hexadecimal': hexadecimal}
        )
        self.conexao = conexao
        self.nome = nome
