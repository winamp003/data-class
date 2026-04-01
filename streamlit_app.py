import streamlit as st
import pandas as pd
import numpy as np

st.title("🎨 Streamlit 요소 샘플 페이지")
st.write("아래는 Streamlit에서 자주 사용하는 주요 요소들 예시입니다.")

st.header("1. 텍스트 및 레이아웃")
st.subheader("기본 텍스트")
st.write("`st.write`, `st.markdown`, `st.text` 등으로 표현합니다.")
st.markdown("**강조 텍스트**와 *이탤릭 텍스트*를 지원합니다.")

st.header("2. 입력 위젯")
col1, col2 = st.columns(2)
with col1:
    checked = st.checkbox("체크박스")
    selected = st.radio("라디오 선택", ["옵션 A", "옵션 B", "옵션 C"])

with col2:
    slider = st.slider("슬라이더", 0, 100, 25)
    text = st.text_input("텍스트 입력", "안녕하세요")

st.write("체크박스:", checked)
st.write("선택:", selected)
st.write("슬라이더:", slider)
st.write("입력 텍스트:", text)

st.header("3. 데이터 표시")

df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["A", "B", "C"]
)
st.dataframe(df)
st.table(df.head(5))

st.metric("기본 지표", 42, delta=3)

st.header("4. 시각화")
st.line_chart(df)
st.bar_chart(df)

st.header("5. 파일 업로드/다운로드")
up = st.file_uploader("CSV 파일 업로드", type=["csv"])
if up is not None:
    uploaded_df = pd.read_csv(up)
    st.write("업로드된 데이터", uploaded_df.head())
    st.download_button("다운로드 CSV", uploaded_df.to_csv(index=False), file_name="download.csv")

st.header("6. 미디어")
st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.svg", caption="Streamlit 로고")

st.header("7. 상태 관리")
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("카운트 증가"):
    st.session_state.count += 1
st.write("현재! 카운트:", st.session_state.count)

with st.expander("추가 도움말"):
    st.info("Streamlit 앱은 위에서 아래로 실행됩니다. 위젯 상태는 `st.session_state`와 캐시를 통해 유지됩니다.")

