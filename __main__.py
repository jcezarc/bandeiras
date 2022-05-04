from py2neo import Graph
from cor import Cor
from pais import Pais

def main():
    user, password = 'neo4j', '1234'
    neo4j = Graph(
        'neo4j://localhost:7687',
        auth=(user, password)
    )
    Brasil = Pais('BR', 'Brasil', neo4j)
    verde, amarelo, azul, branco = [
        Cor('Verde', '#00FF00', neo4j),
        Cor('Amarelo', '#FFFF00', neo4j),
        Cor('Azul', '#0000FF', neo4j),
        Cor('Branco', '#FFFFFF', neo4j)
    ]
    Brasil.bandeira([
        verde, amarelo, azul, branco
    ])
    vermelho = Cor('Vermelho', '#FF0000', neo4j)
    Pais('EUA', 'Estados Unidos', neo4j).bandeira([vermelho, azul, branco])
    Pais('ITA', 'Italia', neo4j).bandeira([verde, vermelho, branco])
    Pais('POR', 'Portugal', neo4j).bandeira([verde, vermelho])
    Pais('FRA', 'França', neo4j).bandeira([azul, branco, vermelho])
    Pais('JPN', 'Japão', neo4j).bandeira([branco, vermelho])
    Pais('MEX', 'México', neo4j).bandeira([verde, vermelho, branco])
    Pais('ARG', 'Argentina', neo4j).bandeira([azul, branco])
    Pais('CAN', 'Canadá', neo4j).bandeira([vermelho, branco])
    Pais('VEN', 'Venezuela', neo4j).bandeira([azul, vermelho, amarelo])
    Pais('COL', 'Colômbia', neo4j).bandeira([azul, vermelho, amarelo])


print('--- Gravando dados ---')
main()
print('**** SUCESSO!!! ****')