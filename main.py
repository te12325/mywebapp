
import random
import streamlit as st

# 1. 페이지 기본 설정 및 커스텀 파스텔 CSS 적용
st.set_page_config(
    page_title="MBTI 몽글몽글 여행지 추천 ✈️",
    page_icon="🌸",
    layout="centered",
)

st.markdown(
    """
    <style>
    /* 전체 배경에 부드러운 파스텔 핑크/보라 그라데이션 적용 */
    .stApp {
        background: linear-gradient(135deg, #fff5f8 0%, #f3e8ff 100%);
    }
    
    /* 제목 스타일 */
    .main-title {
        color: #ff6b81;
        font-size: 2.3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        color: #7d5fff;
        font-size: 1.05rem;
        text-align: center;
        margin-bottom: 25px;
    }

    /* 결과 카드를 위한 귀여운 둥근 상자 */
    .result-card {
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0px 10px 20px rgba(255, 182, 193, 0.3);
        border: 2px solid #ffcca1;
        margin-top: 15px;
    }
    
    /* 버튼 스타일 커스텀 */
    div.stButton > button {
        background: linear-gradient(90deg, #ff758c 0%, #ff7eb3 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 24px;
        font-size: 1.1rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(255, 117, 140, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 117, 140, 0.6);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 2. MBTI 데이터베이스
mbti_data = {
    "ENFP": {
        "title": "🎉 흥미진진 호기심 대장",
        "spot": "발리, 인도네시아 🇮🇩",
        "desc": "매일 새로운 액티비티가 기다리는 발리! 자유로운 영혼에게 딱이에요.",
        "tips": ["스쿠버 다이빙 체험하기", "서핑 도전하기", "야시장 털기"],
    },
    "INFJ": {
        "title": "🌿 조용한 사색의 조력자",
        "spot": "교토, 일본 🇯🇵",
        "desc": "고즈넉한 대나무 숲과 오래된 사찰을 거닐며 마음에 평화를 찾아보세요.",
        "tips": ["아라시야마 대나무 숲 걷기", "전통 찻집 가기", "조용한 카메라인생샷"],
    },
    "INTP": {
        "title": "🔍 아이디어 파라다이스",
        "spot": "런던, 영국 🇬🇧",
        "desc": "박물관과 미술관이 가득한 도시! 지적 호기심을 마음껏 채워봐요.",
        "tips": ["대영박물관 둘러보기", "오래된 고서점 방문", "빅벤 야경 감상"],
    },
    "ENTJ": {
        "title": "👑 완벽한 플래너 비전가",
        "spot": "뉴욕, 미국 🇺🇸",
        "desc": "화려한 트렌드의 중심지! 빽빽한 일정표를 채우며 성취감을 느낄 수 있어요.",
        "tips": ["엠파이어 스테이트 전망대", "브로드웨이 뮤지컬", "센트럴파크 산책"],
    },
    "ESFP": {
        "title": "✨ 흥 부자 에너자이저",
        "spot": "바르셀로나, 스페인 🇪🇸",
        "desc": "열정적인 축제와 맛있는 타파스! 분위기에 취해 신나게 즐겨보세요.",
        "tips": ["사그라다 파밀리아 관람", "해변 비치 바 가기", "플라멩코 공연 보기"],
    },
    "ISTJ": {
        "title": "📐 신뢰 만점 원칙주의자",
        "spot": "취리히, 스위스 🇨🇭",
        "desc": "정확한 기차 시간표와 깨끗한 자연환경! 안심하고 계획대로 여행할 수 있어요.",
        "tips": ["산악열차 타고 융프라우 가기", "호수 유람선 타기", "치즈 퐁뒤 먹기"],
    },
}

# 기본 데이터에 없는 MBTI를 위한 공통 테마
default_recommendation = {
    "title": "🎈 어디로든 떠나고 싶은 탐험가",
    "spot": "제주도, 대한민국 🇰🇷",
    "desc": "푸른 바다와 맛있는 디저트가 기다리는 곳! 가볍게 떠나기 최고예요.",
    "tips": ["돌담길 따라 산책하기", "예쁜 카페 투어", "오름에 올라 노을 보기"],
}

# 3. 앱 화면 구성
st.markdown(
    '<div class="main-title">🌸 MBTI 떠나자! ✈️</div>', unsafe_allow_html=True
)
st.markdown(
    '<div class="sub-title">성향에 딱 맞는 찰떡 여행지를 찾아드려요! 💕</div>',
    unsafe_allow_html=True,
)

# 사이드바/메인 조합
col1, col2 = st.columns([1, 1])

with col1:
    mbti_list = [
        "ENFP",
        "INFJ",
        "INTP",
        "ENTJ",
        "ESFP",
        "ISTJ",
        "INFP",
        "ESTP",
        "ISFP",
        "INTJ",
        "ENTP",
        "ESTJ",
        "ISFJ",
        "ESFJ",
        "ISTP",
        "INFJ",
    ]
    selected_mbti = st.selectbox(
        "✨ MBTI를 선택해 주세요:", sorted(list(set(mbti_list)))
    )

with col2:
    style_option = st.radio(
        "🎀 어떤 느낌의 여행을 선호하나요?",
        ["힐링&휴식 🍃", "액티비티&모험 🏄‍♂️", "문화&맛집 🍕"],
    )

st.write("")
button_clicked = st.button("💖 내 맞춤 여행지 확인하기 💖")

if button_clicked:
    st.balloons()

    info = mbti_data.get(selected_mbti, default_recommendation)

    st.markdown(
        f"""
        <div class="result-card">
            <h3 style="color: #ff6b81; margin-top:0;">{selected_mbti}만을 위한 추천 ✨</h3>
            <h2 style="color: #4b6584;">📍 {info['spot']}</h2>
            <p style="font-size: 1.1rem; color: #57606f;"><b>{info['title']}</b></p>
            <p style="color: #2f3542;">{info['desc']}</p>
            <hr style="border: 0.5px dashed #ffb8b8;">
            <p style="font-weight: bold; color: #7d5fff;">🌟 추천 버킷리스트:</p>
            <ul>
                <li>{info['tips'][0]}</li>
                <li>{info['tips'][1]}</li>
                <li>{info['tips'][2]}</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.success(
        f"선택하신 '{style_option}' 취향까지 고려해서 완벽한 일정을 준비해보세요! 🎒"
    )
