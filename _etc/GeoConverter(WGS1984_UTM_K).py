# GeoConverter (좌표계 변환기)
from pyproj import Proj, transform
import numpy as np
import pandas  as pd
import os

"""
# UTM-K 의 한국 SRID는  ‘5178′ 혹은 ‘5179’입니다.
# epsg : 5186 -> KT / 4326 -> WGS84

(1) 개인 경로 설정하기 및 파일 로드
(2) Dataframe에서 기준좌표계 x, y 지정 (WGS - 위경도 / UTM-K - X,Y ... 등)
(3) 좌표계 등록 epsg (원래 좌표계 -> 바꾸고자 하는 좌표계)
(4) 좌표 변환 transform(기존좌표계, 바꿀좌표계, 좌표x, 좌표y)
(5) 변환 좌표들 새로운 열로 추가 및 csv 파일 저장

"""

# (1) 개인 경로 설정 및 파일 읽기
path = "C:/Users/urse/Documents/카카오톡 받은 파일/"
file_name = 'filename.csv'  # 파일 이름 지정

os.chdir(path)
data = pd.read_csv(path + file_name, engine='python')

# (2) Dataframe에서 기준좌표계 x, y 지정 (WGS - 위경도 / UTM-K - X,Y ... 등)
# df_xy = data[['위도','경도']]
df_xy = data[['lat', 'lon']]

# (3) 좌표계 등록 epsg (원래 좌표계 -> 바꾸고자 하는 좌표계)
# WGS1984 - 경도/위도, GPS사용 전지구 좌표
proj_WGS84 = Proj(init='epsg:4326')

# proj_UTMK (Bassel) 도로명주소 지도 사용 중
proj_UTMK_5186 = Proj(init='epsg:5186')  # kt 유동인구 데이터

# (4) 좌표 변환 transform(기존좌표계, 바꿀좌표계, 좌표x, 좌표y)
# WBS84 -> UTM-K 좌표
ls1, ls2 = [], []
for i in range(len(df_xy)):
    x1, y1 = df_xy['lon'][i], df_xy['lat'][i]  # x1 = 경도, y1 = 위도.
    # 127.xxx / 37.xxx -> 194800 , 546400

    x2, y2 = transform(proj_WGS84, proj_UTMK_5186, x1, y1)
    ls1.append(x2)  # 경도변환좌표들 담음
    ls2.append(y2)  # 위도변환좌표들 담음

# (5) 변환 좌표들 새로운 열로 추가 및 csv 파일 저장
series1 = pd.Series(ls1)  # 경도변환좌표들 담음
series2 = pd.Series(ls2)  # 위도변환좌표들 담음
data['UTM-K_위도변환'] = series2
data['UTM-K_경도변환'] = series1

data.to_csv(file_name + '(UTM_K).csv', encoding='euc_kr', index=False)  # index_False 는 to_csv시 index 안집어넣음.
print('완료')