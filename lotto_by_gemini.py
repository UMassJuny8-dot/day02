import streamlit as st
import random
from datetime import datetime

st.title("🎱로또 번호 자동 생성기🎊")
st.caption("버튼을 누르면 1~45 사이의 중복 없는 번호 6개짜리 세트를 5개 만듭니다.")

def lotto_one_set() -> list :
    """ 1~45 에서 중복없이 6개 뽑아 정렬된 리스트로 반환"""
    number = set() 
    while len(number) < 6:
        number.add(random.randint(1,45))
    return sorted(number)

# 🎨 1. 번호 크기에 따라 로또 공 색상을 정해주는 함수
def get_color(num):
    if num <= 10:
        return "#fbc400" # 노란색
    elif num <= 20:
        return "#69c8f2" # 파란색
    elif num <= 30:
        return "#ff7272" # 빨간색
    elif num <= 40:
        return "#aaaaaa" # 회색
    else:
        return "#b0d840" # 초록색

# ⚽ 2. 동그란 공 모양을 그리는 HTML 코드를 만들어주는 함수
def make_ball_html(num):
    color = get_color(num)
    # CSS를 이용해 동그랗고 그림자가 있는 공 모양 디자인을 설정합니다.
    style = f"""
        display: inline-block;
        width: 40px;
        height: 40px;
        background-color: {color};
        border-radius: 50%; /* 완전한 동그라미로 만들기 */
        text-align: center;
        line-height: 40px;
        font-weight: bold;
        color: white; /* 글자색은 흰색 */
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5); /* 글자에 그림자 넣기 */
        margin-right: 8px;
        box-shadow: 2px 2px 4px rgba(0,0,0,0.2); /* 공 전체에 그림자 넣기 */
    """
    return f'<div style="{style}">{num}</div>'

st.markdown("---")

if st.button("🤞5세트 번호 생성하기🍀", key="lotto_generate_btn"):
    
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"생성 시각 : **{now_str}**")
    st.write("") 

    for set_index in range(1,6):
        lotto_num = lotto_one_set()
        
        # 3. 뽑힌 6개의 번호를 각각 HTML 공 모양으로 변환해서 하나로 합칩니다.
        html_balls = ""
        for num in lotto_num:
            html_balls += make_ball_html(num)
            
        # 4. st.markdown을 이용해 화면에 출력합니다.
        # 주의: unsafe_allow_html=True 를 꼭 써주어야 HTML 디자인이 적용됩니다!
        st.markdown(f"**{set_index}세트** &nbsp;&nbsp; {html_balls}", unsafe_allow_html=True)
        st.write("") # 세트와 세트 사이에 빈 줄을 넣어 간격을 줍니다.