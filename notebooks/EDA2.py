import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.concat([pd.read_csv('/Users/ViegasMP/SGD/projeto 3/data/ssbana1998_6.txt', sep='\t'),
                pd.read_csv('/Users/ViegasMP/SGD/projeto 3/data/ssbana1999_6.txt', sep='\t')])

'''quantidade_mes_mundo_total'''

plt.rcParams["figure.figsize"] = [10, 7]
#segmentar
somas = df.groupby(['monthnuminyear', 'c_region', 'month']).sum()
somas.reset_index(inplace=True)
#plot
g = sns.catplot(x='c_region', y='l_quantity', data=somas, hue='month', kind="bar")
plt.title('Quantidade de produtos encomendados por mês')
plt.show()

'''quantidade_shipmode_mundo_total'''

#segmentar
somas = df.groupby(['l_shipmode', 'c_region']).sum()
somas.reset_index(inplace=True)
#plot
g = sns.catplot(x='c_region', y='l_quantity', data=somas, hue='l_shipmode', kind="bar")
plt.title('Modo de Shipping')
plt.show()


'''quantidade_regioes_mundo_total'''

#segmentar
somas = df.groupby(['c_region'])["l_quantity"].sum()
#plot
plt.axis('equal')
plt.pie(somas, labels=somas.index, autopct='%1.1f%%')
plt.title('Receitas por Região do Cliente')
plt.show()



'''quantidade_nacoes_mundo'''

plt.rcParams["figure.figsize"] = [15, 7]
fig, axs = plt.subplots(2, 3, constrained_layout=True)
# segmentar AFRICA
df1 = df[df['c_region'] == 'AFRICA']
somas = df1.groupby(['c_nation'])["l_quantity"].sum()
# plot AFRICA
axs[0, 0].axis('equal')
axs[0, 0].pie(somas, labels=somas.index, autopct='%1.1f%%')
axs[0, 0].title.set_text('Receitas por Nação dos Clientes da Africa')

# segmentar AMERICA
df2 = df[df['c_region'] == 'AMERICA']
somas = df2.groupby(['c_nation'])["l_quantity"].sum()
# plot AMERICA
axs[0, 1].axis('equal')
axs[0, 1].pie(somas, labels=somas.index, autopct='%1.1f%%')
axs[0, 1].title.set_text('Receitas por Nação dos Clientes da America')

fig.delaxes(axs[1, 2])

# segmentar ASIA
df3 = df[df['c_region'] == 'ASIA']
somas = df3.groupby(['c_nation'])["l_quantity"].sum()
# plot ASIA
axs[0, 2].axis('equal')
axs[0, 2].pie(somas, labels=somas.index, autopct='%1.1f%%')
axs[0, 2].title.set_text('Receitas por Nação dos Clientes da Asia')

# segmentar EUROPE
df4 = df[df['c_region'] == 'EUROPE']
somas = df4.groupby(['c_nation'])["l_quantity"].sum()
# plot EUROPE
axs[1, 0].axis('equal')
axs[1, 0].pie(somas, labels=somas.index, autopct='%1.1f%%')
axs[1, 0].title.set_text('Receitas por Nação dos Clientes da Europa')

# segmentar MIDDLE EAST
df5 = df[df['c_region'] == 'MIDDLE EAST']
somas = df5.groupby(['c_nation'])["l_quantity"].sum()
# plot MIDDLE EAST
axs[1, 1].axis('equal')
axs[1, 1].pie(somas, labels=somas.index, autopct='%1.1f%%')
axs[1, 1].title.set_text('Receitas por Nação dos Clientes do Oriente Medio')

plt.show()

print(df.describe().transpose())

''' Hypothesis 
df1 = pd.read_csv('/Users/ViegasMP/SGD/projeto 3/data/ssbana1998_6.txt', sep='\t')
df2 = pd.read_csv('/Users/ViegasMP/SGD/projeto 3/data/ssbana1999_6.txt', sep='\t')
year1 = df1.groupby(['c_nation'])["l_ordertotalprice"].sum()
year2 = df2.groupby(['c_nation'])["l_ordertotalprice"].sum()
print(year1)

print("year2 data :-\n")
print(year2)
year1_mean = np.mean(year1)
year2_mean = np.mean(year2)
print("year1 mean value:", year1_mean)
print("year2 mean value:", year2_mean)
year1_std = np.std(year1)
year2_std = np.std(year2)
print("year1 std value:", year1_std)
print("year2 std value:", year2_std)
ttest, pval = ttest_ind(year1, year2)
print("p-value", pval)
if pval < 0.05:
    print("we reject null hypothesis")
else:
    print("we accept null hypothesis")
    '''

