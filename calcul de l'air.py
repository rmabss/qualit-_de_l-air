import numpy as np
import pandas as pd

# Charger les données à partir du fichier dataset.csv
df = pd.read_csv("donnée_nettoyée.csv")

# Fonction de calcul de l'AQI
def calculate_AQI(NO, NO2, PM10, PM25, CO2):
    # Fonctions de calcul des sous-indices pour chaque polluant
    def calculate_NO_subindex(NO):
        if NO <= 50:
            return NO * 50 / 50
        elif NO <= 100:
            return 50 + (NO - 50) * 50 / 50
        elif NO <= 150:
            return 100 + (NO - 100) * 100 / 50
        elif NO <= 200:
            return 200 + (NO - 150) * 100 / 50
        elif NO <= 300:
            return 300 + (NO - 200) * 100 / 100
        elif NO > 300:
            return 400 + (NO - 300) * 100 / 100
        else:
            return 0

    def calculate_NO2_subindex(NO2):
        if NO2 <= 50:
            return NO2 * 50 / 50
        elif NO2 <= 100:
            return 50 + (NO2 - 50) * 50 / 50
        elif NO2 <= 150:
            return 100 + (NO2 - 100) * 100 / 50
        elif NO2 <= 200:
            return 200 + (NO2 - 150) * 100 / 50
        elif NO2 <= 300:
            return 300 + (NO2 - 200) * 100 / 100
        elif NO2 > 300:
            return 400 + (NO2 - 300) * 100 / 100
        else:
            return 0

    def calculate_PM10_subindex(PM10):
        if PM10 <= 50:
            return PM10 * 50 / 50
        elif PM10 <= 100:
            return 50 + (PM10 - 50) * 50 / 50
        elif PM10 <= 250:
            return 100 + (PM10 - 100) * 100 / 150
        elif PM10 <= 350:
            return 200 + (PM10 - 250)
        elif PM10 <= 430:
            return 300 + (PM10 - 350) * 100 / 80
        elif PM10 > 430:
            return 400 + (PM10 - 430) * 100 / 80
        else:
            return 0

    def calculate_PM25_subindex(PM25):
        if PM25 <= 30:
            return PM25 * 50 / 30
        elif PM25 <= 60:
            return 50 + (PM25 - 30) * 50 / 30
        elif PM25 <= 90:
            return 100 + (PM25 - 60) * 100 / 30
        elif PM25 <= 120:
            return 200 + (PM25 - 90) * 100 / 30
        elif PM25 <= 250:
            return 300 + (PM25 - 120) * 100 / 130
        elif PM25 > 250:
            return 400 + (PM25 - 250) * 100 / 130
        else:
            return 0

    def calculate_CO2_subindex(CO2):
        if CO2 <= 50:
            return CO2 * 50 / 50
        elif CO2 <= 100:
            return 50 + (CO2 - 50) * 50 / 50
        elif CO2 <= 150:
            return 100 + (CO2 - 100) * 100 / 50
        elif CO2 <= 200:
            return 200 + (CO2 - 150) * 100 / 50
        elif CO2 <= 300:
            return 300 + (CO2 - 200) * 100 / 100
        elif CO2 > 300:
            return 400 + (CO2 - 300) * 100 / 100
        else:
            return 0

    # Calcul des sous-indices pour chaque polluant
    NO_subindex = calculate_NO_subindex(NO)
    NO2_subindex = calculate_NO2_subindex(NO2)
    PM10_subindex = calculate_PM10_subindex(PM10)
    PM25_subindex = calculate_PM25_subindex(PM25)
    CO2_subindex = calculate_CO2_subindex(CO2)

    # Calcul de l'AQI
    AQI = max(NO_subindex, NO2_subindex, PM10_subindex, PM25_subindex, CO2_subindex)

    return AQI

# Appliquer la fonction de calcul de l'AQI à chaque ligne du DataFrame
df["AQI"] = df.apply(lambda row: calculate_AQI(row["NO"], row["NO2"], row["PM10"], row["PM2.5"], row["CO2"]), axis=1)

# Afficher les premières lignes du DataFrame avec l'AQI calculé
print(df.head())

# Sauvegarder le DataFrame avec l'AQI calculé dans le fichier calcul.csv
df.to_csv("calcul.csv", index=False)