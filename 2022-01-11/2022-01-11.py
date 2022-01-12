import pandas as pd

# df = pd.DataFrame(
#     {
#         "Name": [
#             "Braund, Mr. Owen Harris",
#             "Allen, Mr. William Henry",
#             "Bonnell, Miss. Elizabeth",
#         ],
#         "Age": [22, 35, 58],
#         "Sex": ["male", "male", "female"],
#     }
# )

# print(df["Age"])
# print(df["Sex"])

# homes = pd.Series(["London", "NewYork", "paris"], name="Home")
# print(homes)

# # 추가
# df["Home"] = homes
# print(df)

# # 삭제
# df = df.drop(["Sex"], axis=1)
# print(df)

# print(df["Age"].max())
# print(df["Age"].min())
# print(df["Age"].mean())

# print( df.describe() )

# 판다스에서 문자를 처리하는 방식 != csv파일의 문자 처리 방식
# ecoding 맞춰야 함
df = pd.read_csv("test-data.csv", encoding="cp949")
print(df.describe())
print(df["분양가격(제곱미터)"])

# 가격 통계 내고 싶으면 문자 > 숫자 

prices = pd.to_numeric(df["분양가격(제곱미터)"], errors="coerce")
df["분양가격(제곱미터)"] = prices

print(prices.max())
print(prices.min())

df["분양가격(제곱미터)"] = prices 

# 전용면적(제곱미터) => 컬럼명
# 60 ~ 85
# 85 ~ 102

# str.replace() => 특정 문자 치환 함수
sizes = df["규모구분"].str.replace("전용면적", "")
sizes = sizes.str.replace("제곱미터초과", " ~")
sizes = sizes.str.replace("제곱미터이하", "")

df["전용면적(제곱미터)"] = sizes
df = df.drop(["규모구분"], axis=1)
print(df)



df["분양가격(평)"] = df["분양가격(제곱미터)"] * 3.3
df = df.drop(["분양가격(제곱미터)"], axis=1)
print(df)


# 필터링 
is_daejon = df["지역명"] == "대전" # 지역명이 대전인 것만 필터링

df_daejon = df[is_daejon] # 필터링 결과를 데이터프레임에 적용시키면 필터 결과만 얻을 수 있다.
avg_price_in_daejon = df[is_daejon]["분양가격(평)"].mean() # 대전 평균분양가격

# 대전에서 평균 이상인 분양가격만 출력
is_avg_over = df_daejon["분양가격(평)"] > avg_price_in_daejon 
print(df_daejon[is_avg_over])


# 그룹화 - 모든 행을 다 분석하기는 힘들 수 있기 때문에 원하는 컬럼을 기준으로 그룹화 해서 그룹별로 집계할 수 있다.
# 집계함수 -> sum(), mean(), max(), min()
# ex) 각 지역별 평균분양가격, 연도별 평균분양가격, 각 지역의 연도별 평균 분양 가격 등

# 전국 평균
print(df["분양가격(평)"].mean())

# 지역별 평균분양가격
print(   df.groupby(["지역명"])["분양가격(평)"].mean()  ) 

# 연도별 평균분양가격
print(   df.groupby(["연도"])["분양가격(평)"].mean()  )

# 전용면적별 평균분양가격
print(   df.groupby(["전용면적(제곱미터)"])["분양가격(평)"].mean()  )

# 각 지역의 연도별 평균 분양 가격
print(   df.groupby(["지역명", "연도"])["분양가격(평)"].mean()  )
# 지역별로 각 연도별 평균 결과 출력 가로로
new_df = df.groupby(["지역명", "연도"])["분양가격(평)"].mean()
print(new_df.unstack())
# 행과 열의 Name 바꾸기
print(new_df.unstack().T)
