import pandas as pd
import re

df = pd.read_csv('../data/csv/cleaned/cleaned_merged.csv')

# 'tahun' 필드의 값이 2020, 2021, 2022인 행만 선택
df_selected = df.loc[(df['tahun'] >= 2020) & (df['tahun'] <= 2022)].copy()

# 'kddept' 열의 값으로 숫자 3자리 사용
df_selected.loc[:, 'kddept'] = df_selected['nmdept'].apply(lambda x: re.search(r'^\d{3}', str(x)).group() if re.search(r'^\d{3}', str(x)) else None)

# 'nmdept' 열의 값에서 숫자 3자리와 빈칸 제거 후, 문자열의 시작과 끝의 공백 제거
df_selected.loc[:, 'nmdept'] = df_selected['nmdept'].apply(lambda x: re.sub(r'^\d{3}\s', '', str(x)).strip())

# 수정된 df_selected를 df에 반영한다

# 'tahun' 필드의 값이 2020, 2021, 2022인 행을 선택하는 불리언 인덱스 생성
index = (df['tahun'] >= 2020) & (df['tahun'] <= 2022)

# 원본 DataFrame의 해당 부분을 df_selected로 대체
df.loc[index, :] = df_selected

df.to_csv('../data/csv/cleaned/nmdept_cleaned_merged.csv', index=False)
