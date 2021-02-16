# bibliotecas importadas
import pandas as pd
#print ('Hello, World DS')

#Funcao read_csv da biblioteca pandas que ler arquivos csv
dados = pd.read_csv('datasets\kc_house_data.csv')
df = pd.DataFrame(data=dados, dtype=None,index=None)
df = df.rename(columns={'date': 'data', 'price': 'preco', 'bedrooms': 'quartos', 'bathrooms': 'banheiros'})
# Mostra as 5 primeiras linhas do conjuto de dados
#print( data.head() )

#Motra o numero de colunas e linha do conjuto de dados
#print( dados.shape)

#Mostra na tela o nome das colunas do conjuto de dado
print( dados.columns )

#Mostra o conjunto de dados ordenado pela coluna preço
#print( dados[['id', 'price']].sort_values( 'price') )

#Mostra o conjunto de dados ordenado pela coluna preço do maior para o menor
#print( dados[['id', 'price']].sort_values( 'price', ascending=False) )
#print( 'Casa com ', dados[['price']].max() , 'mais alto')

##Mostra o conjunto de dados ordenado pela coluna quartos do maior para o menor
#print( dados[['id', 'bedrooms']].sort_values( 'bedrooms', ascending=False) )
#print( 'Maior quantidade' ,df[['bedrooms']].max() )

#1. Quantas casas estão disponiveis para compra?
data_count = dados[['id']].count()
print( '1. Quantas casas estão disponiveis para compra?' )
print( 'R = Quantidade de casas disponiveis é ', df['id'].count(),'.', )

#2. Quantos atributos as casas possuem ?
print('2. Quantos atributos as casas possuem ?')
print('R = As casas possuem ',df.shape[1], 'atributos.')

#3. Quais são os atributos das casas?
print( '3. Quais são os atributos das casas?')
print( 'R = Os atributos das casas são ',df.columns)

#4. Qual a casa mais cara (casa com o maior  de venda)?

print( '4. Qual a casa mais cara (casa com o maior  de venda)?')
print( 'A casa mais cara (casa com o maior  de venda) é ', df[['id']].loc[(df['preco']==df['preco'].max())],'com o valor de ' ,df['preco'].max())


#5. Qual a casa com maior numero de quartos?
max_quartos=df['id'].loc[(df['quartos']==df['quartos'].max())].to_numpy()
print( 'A com maior numero de quartos é ', max_quartos,'com ' ,df['quartos'].max(), 'quartos')

#6. Qual a soma total de quartos do conjunto de dados?
print( '6. Qual a soma total de quartos do conjunto de dados?' )
print( 'R = A soma total de quartos do conjunto de dados é' ,df['quartos'].sum() )

#7.Quantas casas possuem 2 banheiros?
count_banheiros= df['banheiros'].value_counts()
total_2_banheiros = count_banheiros.loc[2.00]
print( '7.Quantas casas possuem 2 banheiros?' )
print( 'R= Total de casas que  possuem 2 banheiros é ',total_2_banheiros)

#8. Qual o preço medio de todas as casas do conjunto de dados?
print('8. Qual o preço medio de todas as casas do conjunto de dados?')
print('R= O preço medio de todas as casas do conjunto de dados é ' , df['preco'].mean())

#9. Qual o preço médio de  casas com 2 banheiros?
print( '9. Qual o preço médio de  casas com 2 banheiros?')
print ('R= O preço médio de  casas com 2 banheiros é', df['preco'].loc[(df['banheiros']==2.00)].mean())

#10. Qual o preço minimo entre as casas com 3 quartos?
print('10. Qual o preço minimo entre as casas com 3 quartos?')
print ('R= O preço minimo das  casas com 3 quartos é', df['preco'].loc[(df['quartos']==3)].min())

#11. Quantas casas possuem mais de 300 metros quadrados?
print(df[['floors','sqft_living', 'sqft_lot', 'sqft_above','sqft_basement','sqft_living15', 'sqft_lot15']].head())
print(df[['floors','sqft_basement','sqft_living15', 'sqft_lot15']])

#12. Quantas casas tem mas de 2 andares ?


#13. Quantas casas tem vista para o mar?


#14. Das Casas com vista para o mar, quantas tem 3 quartos?
print

#14. Das Casas com mais de 300 quadrados de sala de estar quantos banheiros?