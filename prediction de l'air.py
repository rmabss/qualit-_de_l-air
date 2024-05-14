import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Charger les données à partir du fichier supervisé.csv
df = pd.read_csv("calcul.csv")

# Convertir la colonne "DATE/HEURE" en un format de date/heure approprié
df["DATE/HEURE"] = pd.to_datetime(df["DATE/HEURE"])

# Supprimer la colonne "DATE/HEURE" d'origine
df.drop(columns=["DATE/HEURE"], inplace=True)

# Vérifier les informations sur le DataFrame
print(df.info())

# Vérifier les valeurs manquantes
print(df.isnull().sum())

# Séparer les caractéristiques (X) et la variable cible (y)
X = df.drop(columns=["AQI"])
y = df["AQI"]

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialiser et entraîner le modèle de régression linéaire
model = LinearRegression()
model.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# Évaluer les performances du modèle
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Erreur quadratique moyenne (MSE) :", mse)
print("Coefficient de détermination (R^2) :", r2)

# Créer une figure et un axe pour le graphique
fig, ax = plt.subplots()

# Tracer les prédictions (y_pred) par rapport aux valeurs réelles (y_test)
ax.scatter(y_test, y_pred, c=y_pred, cmap='RdYlGn')
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
ax.set_xlabel('Valeurs réelles de l\'AQI')
ax.set_ylabel('Prédictions de l\'AQI')

# Ajouter une légende de couleur pour la criticité de la qualité de l'air
cbar = plt.colorbar(ax.scatter([], [], c=[], cmap='RdYlGn'))
cbar.set_label('Criticité de la qualité de l\'air')

plt.title('Prédictions de l\'AQI par rapport aux valeurs réelles')
plt.show()