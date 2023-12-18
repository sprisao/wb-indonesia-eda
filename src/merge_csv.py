import pandas as pd

from glob import glob
import os


# 빈 데이터 프레임 생성
merged_df = pd.DataFrame()

for file in glob('../data/csv/original/*.csv'):
    df = pd.read_csv(file)
    merged_df = pd.concat([merged_df, df])

merged_df.to_csv('../data/csv/merged/merged.csv', index=False)


