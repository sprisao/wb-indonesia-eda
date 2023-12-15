import os
import pandas as pd


def excel_to_csv(input_folder, output_folder):
    # Check if the input directory exists
    if not os.path.isdir(input_folder):
        raise FileNotFoundError(f"Input directory '{input_folder}' does not exist.")

    # Excel 파일 목록을 불러온다
    excel_files = [f for f in os.listdir(input_folder) if f.endswith(".xlsx")]

    # 불러온 파일을 하나씩 읽어들여서 데이터프레임으로 만든다
    for file in excel_files:
        file_path = os.path.join(input_folder, file)
        df = pd.read_excel(file_path)

        # Check if the output directory exists, if not create it
        if not os.path.isdir(output_folder):
            os.makedirs(output_folder)

        # 데이터프레임을 CSV 파일로 저장한다
        output_file = file.replace('.xlsx', '.csv')
        output_path = os.path.join(output_folder, output_file)
        df.to_csv(output_path, index=False)


input_folder = "../data/original"
output_folder = "../data/csv"

excel_to_csv(input_folder, output_folder)
