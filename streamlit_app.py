import streamlit as st
from PIL import Image

st.set_page_config(page_title="김요한 자기소개", layout="wide")

st.markdown("# 👋 안녕하세요, 김요한입니다")
st.markdown("### 서울공업고등학교 전기교과 교사 | 교육과 자격증을 연결하는 전문가")

with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        img = Image.open("20240424_221209.jpg")
        rotated = img.rotate(-90, expand=True)
        st.image(rotated, width=180, caption="김요한의 반려견 김호빵!")
    with col2:
        st.write("### 핵심 역량")
        st.write("- **자격증 교육** 설계 및 운영 (전기기능사, 전기기사, 전기기능장)")
        st.write("- **신재생에너지 융합 수업** 개발 및 학생 맞춤 교육")
        st.write("- **공학 실습 중심 교육**과 실제 발전소 사례 기반 지도")

st.write("---")

st.subheader("🎯 주요 프로젝트")
st.image("https://images.unsplash.com/photo-1466611653911-95081537e5b7?w=150&h=100&fit=crop")
with st.expander("신재생에너지 발전소 만들기"):
    st.write("직접 설계하고 교육과정에 포함된 모형 발전소 제작 프로젝트")
    st.write("- 에너지 효율 분석과 시뮬레이션을 통해 학생 이해도 향상")

with st.expander("신재생에너지 융합수업"):
    st.write("전기, 환경, 정보 기술을 통합한 프로젝트 기반 수업 개발")
    st.write("- 팀별 실습, 발표, 평가 체계로 학생 참여도 증진")

st.write("---")

st.subheader("🛠️ 기술 스택 및 자격증")
st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=150&h=100&fit=crop")
st.write("- 전기기능사\n- 전기기사\n- 전기기능장")
st.progress(100)

st.write("---")

st.subheader("📌 개인 정보")
col1, col2 = st.columns(2)
with col1:
    st.image("https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=100&h=100&fit=crop")
    st.write("- 취미: 운동")
with col2:
    st.image("https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=100&h=100&fit=crop")
    st.write("- 취미: 커피")
st.write("- 성향: 프로페셔널하고 교육 중심적 접근")

st.write("---")

st.subheader("📬 연락 및 추가 정보")
st.image("https://images.unsplash.com/photo-1538485399081-7191377e8241?w=150&h=100&fit=crop",)
st.write("- 위치: 서울특별시 동작구 대방동\n- 관심 분야: 신재생에너지 교육, 자격증 연계 실무교육")

with st.expander("소개 메시지"):
    st.info("학생들이 공학적 사고를 갖추고 자격증 취득을 통해 전문 기술인이 될 수 있도록 돕는 것이 목표입니다.")

