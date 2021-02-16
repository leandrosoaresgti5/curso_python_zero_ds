
# bibliotecas importadas
import pandas as pd

# print ('Hello, World DS')

# Funcao read_csv da biblioteca pandas que ler arquivos csv
dados = pd.read_csv('datasets\kc_house_data.csv')
df = pd.DataFrame(data=dados, dtype=None, index=None)
df = df.rename(columns={'date': 'data', 'price': 'preco', 'bedrooms': 'quartos', 'bathrooms': 'banheiros'})
# Mostra as 5 primeiras linhas do conjuto de dados
# print( data.head() )

# Motra o numero de colunas e linha do conjuto de dados
# print( dados.shape)

# Mostra na tela o nome das colunas do conjuto de dado
#print(dados.columns)

# Mostra o conjunto de dados ordenado pela coluna preço
# print( dados[['id', 'price']].sort_values( 'price') )

# Mostra o conjunto de dados ordenado pela coluna preço do maior para o menor
# print( dados[['id', 'price']].sort_values( 'price', ascending=False) )
# print( 'Casa com ', dados[['price']].max() , 'mais alto')

##Mostra o conjunto de dados ordenado pela coluna quartos do maior para o menor
# print( dados[['id', 'bedrooms']].sort_values( 'bedrooms', ascending=False) )
# print( 'Maior quantidade' ,df[['bedrooms']].max() )
#data_count = dados[['id']].count()
# 1. Quantas casas estão disponiveis para compra?
print('1. Quantas casas estão disponiveis para compra?')
print('R = Quantidade de casas disponiveis é ', df['id'].count(), '.\n', )

# 2. Quantos atributos as casas possuem ?
print('2. Quantos atributos as casas possuem ?')
print('R = As casas possuem ', df.shape[1], 'atributos.','.\n')

# 3. Quais são os atributos das casas?
print('3. Quais são os atributos das casas?')
print('R = Os atributos das casas são ', df.columns,'.\n')
print(df.query("id==1"))

# 4. Qual a casa mais cara (casa com o maior  de venda)?

print('4. Qual a casa mais cara (casa com o maior  de venda)?')
print('A casa mais cara (casa com o maior  de venda) é ', df[['id']].loc[(df['preco'] == df['preco'].max())],
      'com o valor de ', df['preco'].max(),'.\n')

# 5. Qual a casa com maior numero de quartos?
print('5. Qual a casa com maior numero de quartos?')
max_quartos = df['id'].loc[(df['quartos'] == df['quartos'].max())].to_numpy()
print('A com maior numero de quartos é ', max_quartos, 'com ', df['quartos'].max(), 'quartos.\n')

# 6. Qual a soma total de quartos do conjunto de dados?
print('6. Qual a soma total de quartos do conjunto de dados?')
print('R = A soma total de quartos do conjunto de dados é', df['quartos'].sum(),'.\n')

# 7.Quantas casas possuem 2 banheiros?
count_banheiros = df['banheiros'].value_counts()
total_2_banheiros = count_banheiros.loc[2.00]
print('7.Quantas casas possuem 2 banheiros?')
print('R= Total de casas que  possuem 2 banheiros é ', total_2_banheiros,'.\n')

# 8. Qual o preço medio de todas as casas do conjunto de dados?
print('8. Qual o preço medio de todas as casas do conjunto de dados?')
print('R= O preço medio de todas as casas do conjunto de dados é ', df['preco'].mean(),'.\n')

# 9. Qual o preço médio de  casas com 2 banheiros?
print('9. Qual o preço médio de  casas com 2 banheiros?')
print('R= O preço médio de  casas com 2 banheiros é', df['preco'].loc[(df['banheiros'] == 2.00)].mean(),'.\n')

# 10. Qual o preço minimo entre as casas com 3 quartos?
print('10. Qual o preço minimo entre as casas com 3 quartos?')
print('R= O preço minimo das  casas com 3 quartos é', df['preco'].loc[(df['quartos'] == 3)].min(),'.\n')

# 11. Quantas casas possuem mais de 300 metros quadrados?
print('11. Quantas casas possuem mais de 300 metros quadrados?')
print('R= A quantidade de casas que possuem mais de 300 metros quadrados é ', df['sqft_lot'].loc[(df['sqft_lot'] > 300)].count(),'casas.\n')

# 12. Quantas casas tem mas de 2 andares ?
print('12. Quantas casas tem mas de 2 andares ?')
print('R = A quantidade de  casas  mais de  2 andares  é ',df['floors'].loc[(df['floors'] > 2)].count(),'casas.\n')



# 13. Quantas casas tem vista para o mar?
print('13. Quantas casas tem vista para o mar?')
print('R = A quantidade de  casas  que tem vista para o mar  é ',df['waterfront'].loc[(df['waterfront'] >0)].count(),'casas.\n')
# 14. Das Casas com vista para o mar, quantas tem 3 quartos?
qtd_cs_vista_mar=df.loc[df['waterfront']>0]
print('14. Das Casas com vista para o mar, quantas tem 3 quartos?')
print('R= Das Casas com vista para o mar', qtd_cs_vista_mar['quartos'].loc[qtd_cs_vista_mar['quartos']==3].count(),'tem 3 quartos\n' )


# 15. Das Casas com mais de 300 quadrados de sala de estar quantos banheiros?
qtd_cs_sqft_living= df.loc[(df['sqft_living'] > 300)]
print('15. Das Casas com mais de 300 quadrados de sala de estar quantas  tem mais 2 banheiros?')
print('R = Das Casas com mais de 300 quadrados de sala de estar',qtd_cs_sqft_living['banheiros'].loc[qtd_cs_sqft_living['banheiros']>2].count(), 'tem mais de 2 banheiros')
