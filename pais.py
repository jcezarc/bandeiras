class Pais:
    def __init__(self, sigla: str, nome: str, conexao):
        conexao.run(
            'MERGE (:Pais {sigla: $sigla, nome: $nome})',
            parameters={'sigla': sigla, 'nome': nome}
        )
        self.sigla = sigla
        self.conexao = conexao

    def bandeira(self, cores: list):
        comando = '''
        MATCH(p:Pais)WHERE p.sigla=$sigla
        MATCH(c:Cor)WHERE c.nome=$nome
        CREATE (p)-[: bandeira]->(c)'''
        for cor in cores:
            params = {'sigla': self.sigla, 'nome': cor.nome}
            self.conexao.run(
                comando,
                parameters=params      
            )
