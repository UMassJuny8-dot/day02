# 1. 필요한 도구 상자(레고 블록)들을 가져옵니다!
import streamlit as st # 웹사이트를 예쁘게 만들어주는 마술 지팡이예요. (앞으로 줄여서 st라고 부를게요)
import pandas as pd    # 엑셀처럼 표를 쉽게 다루게 해주는 마법사입니다. (줄여서 pd라고 부를게요)
import os              # 컴퓨터 안의 폴더와 파일 위치를 요리조리 찾아주는 탐험가예요.

# 2. 읽어올 데이터 파일이 어디 있는지 주소를 적어줍니다.
# "지금 이 코드가 있는 곳에서 뒤로 한 칸 가서(..), common 폴더 안에 있는 raw_trade_data.csv 파일을 찾아줘!" 라는 뜻이에요.
CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "common", "raw_trade_data.csv")
# CSV_PATH = os.path.join(os.path.dirname(__file__), "raw_trade_data.csv") # 만약 코드가 파일과 같은 폴더 안에 있다면 이 줄을 씁니다.

# 3. 환율 샘플 데이터 만들기
# 딕셔너리(사전)라는 방법으로 이름표와 그 안의 내용물을 짝지어 줍니다.
exchange_data = {
    "통화" : ["USD", "EUR", "JPY(100엔)", "CNY"],           # 돈의 종류
    "환율(KRW)" :  ["1390.5", "1503.2", "930.8", "191.3"], # 우리나라 돈으로 얼마인지
    "전일대비" : ["+5.2", "-3.1", "+1.0", "-0.4"]          # 어제보다 올랐는지 내렸는지
}
# 위에서 만든 데이터를 판다스(pd)를 이용해 보기 좋은 '표(DataFrame)'로 변신시킵니다!
df_exchange = pd.DataFrame(exchange_data)

# ---------------------------------------------------------
# 여기서부터는 마술 지팡이(st)를 휘둘러서 화면을 꾸미는 부분이에요!
# ---------------------------------------------------------

# 4. 화면에 제목과 글씨 쓰기
st.title("💱 오늘의 환율 대시보드 💱") # 가장 큰 제목을 쾅! 달아줍니다.
st.caption("아래 데이터는 실제 환율이 아닌 실습용 샌플 데이터입니다.") # 제목 아래에 작고 연한 글씨로 설명을 달아줍니다.

st.header("1) 환율 표 보기") # 중간 크기의 소제목이에요.

# 5. 화면에 표 보여주기
st.write("▶ st.dataframe 상호작용 가능한 표") # 일반 글씨 쓰기
# st.dataframe은 마우스로 칸을 늘리거나 줄일 수 있고, 순서도 정렬할 수 있는 '살아있는 표'예요.
# use_container_width=True 는 화면 넓이에 맞게 표를 고무줄처럼 꽉 채워달라는 뜻입니다.
st.dataframe(df_exchange, use_container_width=True)

st.write("▶ st.table 정적인 표")
# st.table은 사진을 찰칵! 찍은 것처럼 움직이지 않고 딱 고정된 표를 보여줍니다.
st.table(df_exchange)

st.markdown("---") # 화면에 가로로 쭉~ 얇은 선을 그어줍니다. (구분선)

# 6. 멋진 카드 모양으로 숫자 보여주기
st.subheader("2) 주요 환율 카드 (st.metric)") # 약간 작은 소제목이에요.

# 화면을 3개의 칸(열)으로 나눕니다.
col1, col2, col3 = st.columns(3)

# 첫 번째 칸(col1)에 점수판(metric)을 그립니다.
with col1:
    # st.metric(라벨=이름, value=현재값, delta=어제보다 얼마나 변했는지)
    st.metric(label="USD/KRW", value="1,000.0", delta="+5.0")
# 두 번째 칸(col2)에 점수판을 그립니다.
with col2:
    st.metric(label="EUR/KRW", value="1,000.0", delta="-5.0")
# 세 번째 칸(col3)에 점수판을 그립니다.
with col3:
    st.metric(label="JPY/KRW", value="1,000.0", delta="+5.0")

st.markdown("---") # 다시 가로선 긋기

# 7. 무역 데이터 불러와서 보여주기
st.header("3) 보너스: 무역 원본 데이터 미리보기")
st.write("공용 데이터 파일 raw_trade_data.csv를 읽어온 상위 5행입니다.")

# 판다스(pd)에게 아까 2번에서 찾은 주소(CSV_PATH)에 가서 파일을 읽어오라고 시킵니다.
# encoding="utf-8" 은 한글이 깨지지 않고 예쁘게 잘 나오게 해주는 암호 같은 거예요!
df_trade_raw = pd.read_csv(CSV_PATH, encoding="utf-8")

# 읽어온 무역 데이터 표에서 위에서부터 딱 5줄(head(5))만 화면에 꽉 차게 보여줍니다.
st.dataframe(df_trade_raw.head(5), use_container_width=True)