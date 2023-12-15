import pandas as pd
import os

# 검사할 컬럼 리스트 정의
columns_to_check = [
    "nmdept", "nmprogram", "nmgiat", "nmoutput", "nmsuboutput",
    "nmtipe_peng", "pagu_rev", "rupiah", "tahun", "kddept",
    "kdunit", "kdprogram", "kdgiat", "kdfungsi", "kdsfung",
    "kdoutput", "tipe_peng", "kdakun", "nmunit", "nmfungsi",
    "nmsfung", "nmakun", "type", "kdsatker", "kdlokasi",
    "kdkabkota", "iddekon", "kddekon", "kdsektor", "kdsdana",
    "nmlokasi", "nmkabkota", "nmdekon", "nmsatker", "nmsdana",
    "nmsektor", "pagu_diawal", "kdtipe_peng"
]

# 검사할 파일들이 있는 디렉토리
directory = '../data/csv/'

# 결과를 저장할 딕셔너리 초기화
results = {column: [] for column in columns_to_check}
results['filename'] = []

# 각 파일을 순회하면서 검사
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        try:
            # CSV 파일 읽기
            df = pd.read_csv(file_path)
            results['filename'].append(filename)

            # 각 컬럼에 대해 검사
            for column in columns_to_check:
                if column in df.columns:
                    # 데이터 유효성 검사
                    if not df[column].isnull().all():  # 유효한 데이터가 있으면
                        results[column].append(2)
                    else:  # 필드만 존재
                        results[column].append(1)
                else:  # 필드가 존재하지 않음
                    results[column].append(0)

        except Exception as e:
            print(f"{filename}: 파일을 읽는 중 오류가 발생했습니다. 오류: {e}")

# 결과를 DataFrame으로 변환하고 CSV 파일로 저장
result_df = pd.DataFrame(results)
result_df.set_index('filename', inplace=True)
result_df.to_csv('output_results.csv')
