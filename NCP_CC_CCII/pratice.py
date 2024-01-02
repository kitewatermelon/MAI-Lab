import pandas as pd
import os

file_path = []
dir_path = "NCP_CC_CCII\\NCP"
for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_path.append(os.path.join(root, file))



# 파일 경로
lesion_clices_path = 'NCP_CC_CCII\lesions_slices.csv'
praticelist_path = 'praticelist.csv'

# 문자열 변경 함수
def transform_string(input_string):
    return input_string.replace('NCP_CC_CCII\\NCP\\', 'NCP/').replace('\\', '/')

# lesion_clices.csv 파일 읽기
lesion_df = pd.read_csv(lesion_clices_path)

# 변환된 문자열을 저장할 리스트
transformed_strings = []

# 문자열 변경 및 새 리스트에 추가
for index, row in lesion_df.iterrows():
    original_string = row['imgpath']
    transformed_string = transform_string(original_string)
    transformed_strings.append(transformed_string)

# praticelist.csv 파일에 저장할 데이터프레임 생성
praticelist_df = pd.DataFrame({'imgpath': transformed_strings})

# 변환된 데이터프레임을 praticelist.csv 파일에 저장
praticelist_df.to_csv(praticelist_path, index=False)
