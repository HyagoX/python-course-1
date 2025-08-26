# Exercicio com Args(Que retorna Tuplas) e Kwargs(Que retorna uma chave com um valor), utilizando como exemplo o arquivo 'args_kwargs.py'

def gerar_relatorio_compra(dataCompra, *produtos, **cliente):
    lista_produtos = '\n'.join(produtos)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in cliente.items()])
    mensagem = f'{dataCompra} \n {lista_produtos} \n\n {meta_dados}'
    print(mensagem)

gerar_relatorio_compra(
    'Domingo, 24 de Agosto de 2025',
    'Macaxeira',
    'Cafe',
    'Leite',
    'Uva',
    'Maca',
    nome='Hyago',
    idade='17',
    endereco='Manoel Dias, 644'
    
)