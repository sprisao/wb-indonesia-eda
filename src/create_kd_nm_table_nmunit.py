import pandas as pd

df = pd.read_csv('../data/csv/cleaned/2_nmfungsi_cleaned_merged.csv')

unique_nmunit = df.groupby('kdunit')['nmunit'].unique().apply(list)

# Convert the Series to a DataFrame
unique_nmunit_df = unique_nmunit.to_frame()

# Reset the index
unique_nmunit_df_reset = unique_nmunit_df.reset_index()

# Create a new column 'idx' that represents the index of each 'nmunit' in its list for each 'kdunit'
unique_nmunit_df_reset['idx'] = unique_nmunit_df_reset.groupby('kdunit').cumcount()

# Pivot the DataFrame
pivot_df = unique_nmunit_df_reset.pivot(index='kdunit', columns='idx', values='nmunit')

# Reset the index of the pivot table and save it to an Excel file
pivot_df.reset_index().to_excel('../data/excel/unique_nmunit_pivot.xlsx', index=False)