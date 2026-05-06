# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:02:20 2026

@author: kteva
"""

import streamlit as st
import random
import time

st.set_page_config(page_title="線上擲筊系統", page_icon="🏮")

st.title("🏮 擲筊")
st.write("請在心中默念你的問題與姓名、生日、地址，隨後按下按鈕。")

if 'result' not in st.session_state:
    st.session_state.result = "準備好請擲筊"

if st.button('【 開始擲筊 】', use_container_width=True):
    with st.status("正在向神明請示中...", expanded=True) as status:
        st.write("誠心祈求...")
        time.sleep(1)
        st.write("筊杯落地...")
        time.sleep(1)
        
       
        cup_a = random.choice(['平', '凸'])
        cup_b = random.choice(['平', '凸'])
        
        if cup_a != cup_b:
            st.session_state.result = "🌟【 聖筊 】🌟\n\n神明應允，萬事大吉！"
        elif cup_a == '平':
            st.session_state.result = "😄【 笑筊 】😄\n\n神明笑而不答，請再說清楚一點。"
        else:
            st.session_state.result = "❌【 陰筊 】❌\n\n神明不應允，建議換個方式思考。"
        
        status.update(label="擲筊完成！", state="complete", expanded=False)

st.divider()
st.subheader("神示結果：")
st.info(st.session_state.result)

st.caption("※ 本程式僅供參考，心誠則靈。")
