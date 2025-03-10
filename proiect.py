import pandas as pd
import matplotlib.pyplot as plt #am folosit libraria matplot pentru a vedea graficele desenate
from scipy.stats import pearsonr #libraria ce faciliteaza calculul indicelui pearson intre cele doua variabile

file_path = "steam_games.csv"
df = pd.read_csv(file_path) #citesc

# --- TEST INFO CSV ---
# print(df.head())
# print(df.info())
# --- TEST INFO CSV ---

df = df[['price', 'rating']] #selectez coloanele de interes

df = df.dropna() #drop liniilor care au valori nule

# scot jocurile gratuite (adica pret = 0); ce se afla in parantezele patrate este de fapt un filtru care se aplica pe coloana "price" si "transforma" respectiva coloana in booleans.
# astfel pastrez doar valorile pozitive
df = df[df['price'] > 0] 

descriptive_stats = df.describe() #df.describe() returneaza statistici cu privire la price si rating (se aplica doar la coloanele numerice)
print(descriptive_stats)

# bar charts
df['price'].hist(bins=30)
plt.title('Distributia Preturilor Jocurilor')
plt.xlabel('Pret')
plt.ylabel('Frecventa')
plt.show()

df['rating'].hist(bins=30)
plt.title('Distributia Rating-urilor Jocurilor')
plt.xlabel('Rating')
plt.ylabel('Frecventa')
plt.show()

# scatter plot pret versus rating
df.plot.scatter(x='price', y='rating', figsize=(8, 5), title='Corelatia dintre Pret si Rating')
plt.xlabel('Pret')
plt.ylabel('Rating')
plt.show()

# calculul corelatiei
correlation, p_value = pearsonr(df['price'], df['rating'])
print(f'Coeficientul de corelatie Pearson: {correlation:.2f}') # indicele pearson deoarece este metoda standard pentru a evalua corelatia intre doua variabile numerice - EXPLICA TEORIE
print(f'P-value: {p_value:.4f}')

# concluzii
if p_value < 0.05:
    print("Exista o corelatie semnificativa statistic intre pret si rating.")
    if correlation > 0:
        print("Jocurile mai scumpe tind sa aiba rating-uri mai mari.")
    else:
        print("Jocurile mai scumpe tind sa aiba rating-uri mai mici.")
else:
    print("Nu exista o corelatie semnificativa intre pret si rating.")
