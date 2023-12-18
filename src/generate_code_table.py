import pandas as pd

df = pd.read_csv('../data/csv/cleaned/cleaned_merged.csv')

# for tahun 2011 - 2022 : create df which takes kddept as index and nmdept as column

df_2011_2022 = df[(df['tahun'] >= 2011) & (df['tahun'] <= 2022)]
df_2011_2022 = df_2011_2022[['kddept', 'nmdept', 'tahun']]
df_2011_2022 = df_2011_2022.drop_duplicates()
df_2011_2022 = df_2011_2022.set_index('kddept')
df_2011_2022 = df_2011_2022.sort_index()

nan_kddept = df_2011_2022[df_2011_2022.index.isna()]

nan_kddept.to_csv('../data/csv/code_mapping/kddept/NaN/nan_kddept.csv')
