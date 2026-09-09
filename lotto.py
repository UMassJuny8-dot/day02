# random 모듈을 이용해서 1~45 중 중복 없는 번호 6개를 뽑고
# 자료구조 list(중복가능), set(중복불가) : set이용, 버튼을 누르면 5세트 한번에 생성
# datatime 으로 생성 시간도 함께 보여준다.

import streamlit as st
import random
from datetime import datetime

st.title("🎱로또 번호 자동 생성기🎊")
st.caption("버튼을 누르면 1~45 사이의 중복 없는 번호 6개짜리 세트를 5개 만듭니다.")

def lotto_one_set() -> list :
    """ 1~45 에서 중복없이 6개 뽑아 정렬된 리스트로 반환"""
    number = set[int]()
    while len(number) < 6:
        number.add(random.randint(1,45)) # 1 이상 45 이하 정수 하나 뽑기
    return sorted(number)

st.markdown("---")

st.button("🤞5세트 번호 생성하기🍀", key="lotto_generate_btn")
now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.write(f"생성 시각 : **{now_str}**")

for set_index in range(1,6):
    lotto_num = lotto_one_set()
    st.write(f"{set_index}세트 : ")









