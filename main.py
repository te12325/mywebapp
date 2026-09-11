import re
import requests
import pandas as pd
import streamlit as st
import plotly.express as px

# 1. 페이지 설정
st.set_page_config(page_title="전국 고령화 지도", layout="wide")

# 2. 배경화면(하늘색 그라데이션 + 애니메이션 구름 + 카드 스타일) Custom CSS 적용
st.markdown("""
    <style>
    /* 전체 배경을 밝은 하늘색 그라데이션으로 설정 */
    .stApp {
        background: linear-gradient(180deg, #87CEEB 0%, #E0F6FF 100%);
        background-attachment: fixed;
        overflow-x: hidden;
    }

    /* 애니메이션 되는 구름 효과 */
    .stApp::before, .stApp::after {
        content: "";
        position: fixed;
        top: 8%;
        left: -100px;
        width: 200px;
        height: 60px;
        background: rgba(255, 255, 255, 0.7);
        border-radius: 200px;
        box-shadow: 0 8px 15px rgba(0,0,0,0.05);
        animation: moveClouds 35s linear infinite;
        z-index: 0;
        pointer-events: none;
    }
    .stApp::before {
        box-shadow: 40px -20px 0 10px rgba(255, 255, 255, 0.7), 90px -10px 0 20px rgba(255, 255, 255, 0.7);
    }
    .stApp::after {
        top: 25%;
        animation-duration: 50s;
        animation-delay: -15s;
        opacity: 0.5;
        transform: scale(1.3);
    }

    @keyframes moveClouds {
        0% { transform: translateX(-200px); }
        100% { transform: translateX(105vw); }
    }

    /* 제목 및 캡션 영역 스타일 */
    h1 {
        color: #1E3A8A !important;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.8);
        font-weight: 800;
    }
    .stCaption {
        color: #1E40AF !important;
        font-size: 1.05rem !important;
        font-weight: 600;
    }

    /* Plotly 차트 배경을 반투명 흰색 카드로 감싸기 */
    [data-testid="stPlotlyChart"] {
        background-color: rgba(255, 255, 255, 0.65);
        backdrop-filter: blur(8px);
        border-radius: 20px;
        padding: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border: 1px solid rgba(255, 255, 255, 0.8);
    }

    /* 데이터프레임 카드 및 헤더 스타일 */
    .stSubheader h3 {
        color: #1E3A8A !important;
        font-weight: 700;
        margin-bottom: 10px;
    }
    [data-testid="stDataFrame"] {
        background-color: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(8px);
        border-radius: 15px;
        padding: 10px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.06);
        border: 1px solid rgba(255, 255, 255, 0.8);
    }
    </style>
""", unsafe_allow_html=True)

# 메인 타이틀
st.title("🗺️ 전국 고령화 지도")
st.caption("시군구별 65세 이상 인구 비율 (행정안전부 주민등록 인구)")

POP_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/population_yearly.csv.gz"
GEO_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/boundaries/sigungu_kr.geojson"

@st.cache_data(show_spinner="인구 데이터를 불러오는 중입니다...")
def load_population():
    return pd.read_csv(POP_URL, dtype={"코드": str})

@st.cache_data(show_spinner="지도 경계를 불러오는 중입니다...")
def load_geojson():
    return requests.get(GEO_URL, timeout=30).json()

df = load_population()
geojson = load_geojson()

# 1. 가장 최신 연도만 사용
latest_year = int(df["연도"].max())
df = df[df["연도"] == latest_year].copy()

# 2. '계_'로 시작하는 나이 열만
total_cols = [c for c in df.columns if c.startswith("계_")]

def age_of(col):
    m = re.match(r"계_(\d+)세", col)
    return int(m.group(1)) if m else None

# 3. 그중 65세 이상 열만
elderly_cols = [c for c in total_cols if age_of(c) is not None and age_of(c) >= 65]

# 4. 동 단위로 전체 인구·고령 인구 계산
df["전체인구"] = df[total_cols].sum(axis=1)
df["고령인구"] = df[elderly_cols].sum(axis=1)

# 5. 시군구별로 묶어 비율 계산
df["시군구코드"] = df["코드"].str[:5]
grouped = df.groupby("시군구코드")[["전체인구", "고령인구"]].sum().reset_index()
grouped["고령화율"] = (grouped["고령인구"] / grouped["전체인구"] * 100).round(2)

names = pd.DataFrame([
    {
        "시군구코드": str(f["properties"]["코드"]),
        "시군구": f["properties"]["시군구"],
        "시도": f["properties"]["시도"],
    }
    for f in geojson["features"]
])
merged = grouped.merge(names, on="시군구코드", how="left")

# 6. 5단계 색 구간
BINS = [0, 19, 23, 28, 38, 100]
LABELS = ["19% 미만", "19~23%", "23~28%", "28~38%", "38% 이상"]
COLORS = {
    "19% 미만": "#fee6ce",
    "19~23%": "#fdc086",
    "23~28%": "#f79646",
    "28~38%": "#e8590c",
    "38% 이상": "#a63603",
}
merged["단계"] = pd.cut(merged["고령화율"], bins=BINS, labels=LABELS, right=False)

# 7. 단계구분도 그리기 (배경 투명화 처리 추가)
fig = px.choropleth(
    merged,
    geojson=geojson,
    locations="시군구코드",
    featureidkey="properties.코드",
    color="단계",
    category_orders={"단계": LABELS},
    color_discrete_map=COLORS,
    hover_name="시군구",
    hover_data={"고령화율": True, "시도": True, "시군구코드": False, "단계": False},
    labels={"고령화율": "65세 이상 비율(%)"},
)
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),
    height=700,
    legend_title_text=f"65세 이상 비율 ({latest_year}년)",
    paper_bgcolor="rgba(0,0,0,0)", # 그래프 배경을 투명하게 설정
    plot_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig, width="stretch")

# 8. 지도 아래 순위 표 두 개
c1, c2 = st.columns(2)
cols = ["시도", "시군구", "고령화율"]
with c1:
    st.subheader("🔴 고령화율 높은 곳 10")
    st.dataframe(merged.nlargest(10, "고령화율")[cols].reset_index(drop=True), use_container_width=True)
with c2:
    st.subheader("🟢 고령화율 낮은 곳 10")
    st.dataframe(merged.nsmallest(10, "고령화율")[cols].reset_index(drop=True), use_container_width=True)
