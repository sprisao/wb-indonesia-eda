import pandas as pd

# 2020부터 2022까지의 연도에 대해 반복
for year in range(2020, 2023):
    # 연도를 문자열로 변환
    str_year = str(year)

    # 해당 연도의 파일을 읽어옴
    df = pd.read_csv(f'../data/csv/Real_{str_year}.csv')

    # df에 tahun column 추가 하여 전체 행에 해당 연도 값 넣기
    df['tahun'] = year

    # 수정된 df를 csv 파일로 덮어쓰기
    df.to_csv(f'../data/csv/Real_{str_year}.csv', index=False)