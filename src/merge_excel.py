import os
import pandas as pd


def merge_excel_to_csv(input_folder, output_folder, output_file):
    # Excel 파일 목록을 불러온다
    excel_files = [f for f in os.listdir(input_folder) if f.endswith(".xlsx")]

    # 불러온 파일을 하나씩 읽어들여서 데이터프레임으로 만든다
    dataframes = []
    for file in excel_files:
        file_path = os.path.join(input_folder, file)
        df = pd.read_excel(file_path)
        dataframes.append(df)


    # 데이터프레임을 하나로 합친다
    merged_df = pd.concat(dataframes)

    # 합친 데이터프레임을 CSV 파일로 저장한다
    output_path = os.path.join(output_folder, output_file)
    merged_df.to_csv(output_path, index=False)


input_folder = "data/origin"
output_folder = "data/csv"
output_file = "merged.csv"

merge_excel_to_csv(input_folder, output_folder, output_file)
