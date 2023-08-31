import pandas as pd
import sqlite3
import seaborn as sns
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt


with sqlite3.connect('E:\Projekty\RPIS\projekt.db') as conn:
    dg = pd.read_sql('select * from games ', conn)
dg.head()
dg.isnull().sum()
len(dg)-len(dg.drop_duplicates())
dg.dropna(inplace=True)
dg['Year']=dg['Year'].astype(int)


# ax = plt.figure(figsize=(10, 6))
# sns.distplot(dg['Year'], color='green')
# plt.title('Liczba gier wydanych w poszczególnych latach')
# avg = dg['Global_Sales'].mean()
# median = dg['Global_Sales'].median()
# plt.show()
# print("Średnia: ", round(avg,2), "Mediana: ", median)


# ax1=plt.figure(figsize=(15,6))
# sns.barplot(x='Genre', y='NA_Sales', data=dg , palette='Paired')
# plt.ylabel("Sprzedaż")
# plt.title("Sprzedaż gatunków gier w Ameryce Północnej")
# plt.show()
#
#
# ax2=plt.figure(figsize=(15,6))
# sns.barplot(x='Genre', y='EU_Sales', data=dg , palette='hls')
# plt.ylabel("Sprzedaż")
# plt.title("Sprzedaż rodzajów gier w Europie")
# plt.show()
#
# ax3=plt.figure(figsize=(15,6))
# sns.barplot(x='Genre', y='JP_Sales', data=dg , palette='Paired')
# plt.ylabel("Sprzedaż")
# plt.title("Sprzedaż gatunków gier w Japonii")
# plt.show()
#
#
# plt.figure(figsize=(16, 5))
# sns.countplot(x="Year", data=dg, hue='Genre', order=dg.Year.value_counts().iloc[:5].index)
# plt.xticks(size=16, rotation=90)
# plt.title("TOP 5 wydanych gier według gatunku")
# plt.show()


# ax = plt.figure(figsize=(15,6))
# dg.groupby(['Year'])['Global_Sales'].sum().plot()
# plt.grid()
# plt.ylabel('Światowa sprzedaż')
# plt.title('Światowa sprzedaż gier na przestrzeni lat')
# plt.show()
#
ax = plt.figure(figsize=(15,6))
dg.groupby(['Platform'])['Global_Sales'].sum().plot().bar(15, 10)
plt.xticks(rotation=45)
plt.ylabel('Sprzedaż')
plt.title('Wykres sprzedaży gier na poszczególne platformy')
plt.show()
#
#
# max_year_dg = dg.groupby(['Year', 'Genre']).size().reset_index(name='count')
# max_year_id = max_year_dg.groupby(['Year'])['count'].transform(max) == max_year_dg['count']
# max_year_genre = max_year_dg[max_year_id].reset_index(drop=True)
# max_year_genre = max_year_genre.drop_duplicates(subset=["Year", "count"], keep = 'last').reset_index(drop = True)
# genre = max_year_genre['Genre'].values
#
# plt.figure(figsize=(15,8))
# plt.title("Który gatunek gier został wydany najwięcej razy w ciągu jednego roku")
# g = sns.barplot(x='Year', y='count', data = max_year_genre)
# id = 0
# for val in max_year_genre['count'].values:
#     g.text(id, val + 5, str(genre[id] + '----' + str(val)), color='#000', size=14, rotation=90, ha="center")
#     id += 1
#
# plt.xticks(rotation=90)
# plt.show()
#
#
# top_region = dg[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]
# top_region = top_region.sum().reset_index()
# top_region = top_region.rename(columns={"index": "region", 0: "sprzedaż"})
#
# labels = top_region['region']
# sizes = top_region['sprzedaż']
# plt.figure(figsize=(10, 8))
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
# plt.title("Zestawienie sprzedaży gier w regionach świata")
# plt.show()
#
