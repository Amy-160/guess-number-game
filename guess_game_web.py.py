import streamlit as st
import random

# 初始化 session state
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.result = ""

st.title("🎯 猜數字遊戲")
st.write("我想了一個 1 到 100 的數字，來猜猜看吧！")

# 輸入數字
guess = st.number_input("請輸入你的猜測：", min_value=1, max_value=100, step=1)

if st.button("猜！"):
    st.session_state.attempts += 1
    if guess < st.session_state.answer:
        st.session_state.result = "太小了！再試一次。"
    elif guess > st.session_state.answer:
        st.session_state.result = "太大了！再試一次。"
    else:
        st.session_state.result = f"🎉 恭喜你猜對了！答案是 {st.session_state.answer}，你總共猜了 {st.session_state.attempts} 次。"

# 顯示結果
st.write(st.session_state.result)

# 重新開始
if st.button("重新開始"):
    st.session_state.answer = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.result = ""
