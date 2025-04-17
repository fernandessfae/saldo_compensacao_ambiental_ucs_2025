import pandas as pd
import os

pd.set_option('display.float_format', '{:.2f}'.format)

df_ucs_biome_info: pd.DataFrame = pd.read_excel(
    'data/dadosgeoestatisticos_ucs_27fev2025.xlsx', engine='openpyxl',
    skiprows=2, nrows=341)

print(df_ucs_biome_info.columns)
print()

# Remove unnecessary columns
df_ucs_biome_info.drop(
    columns=['Unnamed: 0',
             'Nome da Unidade de Conservação',
             'Núcleo de Gestão Integrada',
             'Atos legais (Criação ou redefinição)',
             'UF de Abrangência',
             'Bioma para fins de Compensação de Reserva Legal'
             ], inplace=True)

# Roname the column that will be used to merge with the other dataframe
df_ucs_biome_info.rename(
    columns={'Código CNUC (MMA)': 'CÓDIGO CNUC',
             'Bioma* (IBGE 1:250mil). Para as UCs que ocorrem em mais de um bioma, é considerado apenas o bioma que abrange 50% ou mais de seu território': 'Bioma Total/Marjoritário',}, inplace=True)

# Get the last 4 characters of the CÓDIGO CNUC column
df_ucs_biome_info['CÓDIGO CNUC'] = df_ucs_biome_info['CÓDIGO CNUC'].str[-4:]

# Dataframe view after update
print(df_ucs_biome_info.head())
print()

df_ucs_environment_compensation: pd.DataFrame = pd.read_excel(
    'data/relatorio-siscomp_pagamento_saldo-disponivel.xlsx',
    engine='openpyxl')

print(df_ucs_environment_compensation.tail())
print()

print(df_ucs_environment_compensation.columns)
print()

# Remove rows without 'CÓDIGO CNUC'
df_ucs_environment_compensation.dropna(
    subset=['CÓDIGO CNUC'], inplace=True)

# Convert the column 'CÓDIGO CNUC' to string and remove the decimal part
df_ucs_environment_compensation['CÓDIGO CNUC'] = \
    df_ucs_environment_compensation['CÓDIGO CNUC'].astype(
        str).str.replace(r'\.0$', '', regex=True)

# Check if rows with 'CÓDIGO CNUC' with length less than 4
len_numbers_mask = df_ucs_environment_compensation['CÓDIGO CNUC'].str.len() < 4

#Fill the 'CÓDIGO CNUC' column with the last 4 characters
df_ucs_environment_compensation['CÓDIGO CNUC'] = \
    df_ucs_environment_compensation['CÓDIGO CNUC'].mask(
          len_numbers_mask, df_ucs_environment_compensation[
                'CÓDIGO CNUC'].str.zfill(4))

# Merge the two dataframes on the 'CÓDIGO CNUC' column
df_ucs_environment_compensation_biome: pd.DataFrame = \
    df_ucs_environment_compensation.merge(
        df_ucs_biome_info[['CÓDIGO CNUC', 'Gerência Regional',
                           'Bioma Total/Marjoritário','Área (em hectares)**']],
        on='CÓDIGO CNUC',
        how='left')

print(df_ucs_environment_compensation_biome.tail())
print()

# Add data folder if it doesn't exist
if not os.path.exists('data'):
        os.makedirs('data')

# Download the file with the new dataframe
if not os.path.exists('data/recurso_compensacao_ambiental_ucs_2025.xlsx'):
    df_ucs_environment_compensation_biome.to_excel(
    'data/recurso_compensacao_ambiental_ucs_2025.xlsx',
    index=False)
