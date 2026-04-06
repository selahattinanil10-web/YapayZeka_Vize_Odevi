import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

results = pd.read_csv('results.csv')

print("--- Veri Seti İlk 5 Satır ---")
print(results.head())

print("\n--- Özelliklerin Açıklanması ---")


print("\n--- Eksik Veri Sayıları ---")
missing_values = results.isnull().sum()
print(missing_values)


results.dropna(inplace=True)

print("\nMaksimum Ev Sahibi Skoru:", results['home_score'].max())
print("Maksimum Deplasman Skoru:", results['away_score'].max())

def determine_result(row):
    if row['home_score'] > row['away_score']:
        return 1  # Ev Sahibi Kazandı
    elif row['home_score'] < row['away_score']:
        return 2  # Deplasman Kazandı
    else:
        return 0  # Berabere

results['result'] = results.apply(determine_result, axis=1)

df = results[['home_team', 'away_team', 'home_score', 'away_score', 'tournament', 'result']]

plt.figure(figsize=(10,6))
sns.countplot(x='result', data=df, palette='magma')
plt.title('Maç Sonucu Dağılımı (1: Ev Sahibi, 0: Beraberlik, 2: Deplasman)')
plt.xlabel('Maç Sonucu')
plt.ylabel('Toplam Maç Sayısı')
plt.show()

plt.figure(figsize=(10,4))
sns.boxplot(x=df['home_score'])
plt.title('Ev Sahibi Skorları Aykırı Değer Analizi (Boxplot)')
plt.show()

plt.figure(figsize=(10,4))
sns.boxplot(x=df['away_score'])
plt.title('Deplasman Skorları Aykırı Değer Analizi (Boxplot)')
plt.show()