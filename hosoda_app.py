import random
from google import genai
import streamlit as st

api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)
MODEL_NAME = "gemini-3.5-flash"

# --------------------
# ページ設定
# --------------------
st.set_page_config(
    page_title="細田守キャラクター診断",
    page_icon="🎬",
    layout="centered"
)

st.markdown("""
<style>

/* ===== 背景 ===== */
.stApp {
    background:
    linear-gradient(
        180deg,
        #7ec8ff 0%,
        #bde8ff 40%,
        #ffffff 100%
    );
}

/* ===== タイトル ===== */
.main-title {
    text-align: center;
    font-size: 4rem;
    font-weight: 900;
    color: white;

    text-shadow:
        3px 3px 0 #4aa3df,
        6px 6px 15px rgba(0,0,0,0.2);

    margin-bottom: 10px;
}

/* ===== サブタイトル ===== */
.subtitle {
    text-align: center;
    color: #1f4f82;
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 30px;
}

/* ===== ラジオボタン全体をカード化 ===== */
div[data-testid="stRadio"] {

    background: rgba(255,255,255,0.85);

    backdrop-filter: blur(12px);

    border-radius: 24px;

    padding: 20px;

    margin-bottom: 20px;

    box-shadow:
        0 8px 20px rgba(0,0,0,0.08);

    transition: all .3s ease;
}

div[data-testid="stRadio"]:hover {

    transform: translateY(-4px);

    box-shadow:
        0 14px 28px rgba(0,0,0,0.12);
}

/* ===== ラジオ文字 ===== */
.stRadio label {
    color: #203040 !important;
    font-weight: 600;
}

/* ===== ボタン ===== */
.stButton > button {

    width: 100%;
    height: 60px;

    border-radius: 40px;

    border: none;

    font-size: 22px;
    font-weight: bold;

    color: white;

    background:
    linear-gradient(
        90deg,
        #4facfe,
        #00f2fe
    );

    box-shadow:
        0 8px 20px rgba(79,172,254,0.4);

    transition: all .3s ease;
}

.stButton > button:hover {

    transform: scale(1.03);

    box-shadow:
        0 12px 25px rgba(79,172,254,0.5);
}

/* ===== 成功メッセージ ===== */
.stSuccess {

    border-radius: 20px;
}

/* ===== 情報ボックス ===== */
.stInfo {

    border-radius: 20px;
}

/* ===== 画像 ===== */
img {

    border-radius: 25px;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.15);
}

/* ===== 見出し ===== */
h1,h2,h3 {

    color: #1f4f82;
}

/* ===== 区切り線 ===== */
hr {

    border: none;

    height: 2px;

    background:
    linear-gradient(
        90deg,
        transparent,
        #4facfe,
        transparent
    );
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">
🎬 細田守キャラクター診断
</div>

<div class="subtitle">
質問に答えて、あなたにぴったりのキャラクターを見つけよう！
</div>
""", unsafe_allow_html=True)

# --------------------
# 質問
# --------------------

q1 = st.radio(
    "休日はどう過ごしたい？",
    ["友達と遊ぶ", "家族と過ごす", "新しいことに挑戦", "一人で好きなことをする"]
)

q2 = st.radio(
    "困難に直面したら？",
    ["仲間に相談する", "最後まで頑張る", "自分なりの方法で解決する", "じっくり考える"]
)

q3 = st.radio(
    "一番大切なものは？",
    ["友情", "家族", "成長", "夢"]
)

q4 = st.radio(
    "周りからよく言われる性格は？",
    ["明るい", "優しい", "努力家", "好奇心旺盛"]
)

q5 = st.radio(
    "好きな物語は？",
    ["仲間との協力", "家族愛", "成長物語", "不思議な冒険"]
)

q6 = st.radio(
    "友達から相談されたら？",
    ["一緒に考える", "優しく聞く", "励ます", "自由にやらせる"]
)

q7 = st.radio(
    "好きな場所は？",
    ["みんなが集まる場所", "自然の中", "修行できる場所", "不思議な場所"]
)

q8 = st.radio(
    "あなたの強みは？",
    ["協調性", "思いやり", "努力", "想像力"]
)

# --------------------
# 診断開始
# --------------------

if st.button("診断する 🎬"):

    scores = {
        "健二": 0,
        "花": 0,
        "九太": 0,
        "すず": 0,
        "くんちゃん": 0
    }

    # Q1
    if q1 == "友達と遊ぶ":
        scores["健二"] += 1
    elif q1 == "家族と過ごす":
        scores["花"] += 2
    elif q1 == "新しいことに挑戦":
        scores["九太"] += 2
    else:
        scores["くんちゃん"] += 2

    # Q2
    if q2 == "仲間に相談する":
        scores["健二"] += 2
    elif q2 == "最後まで頑張る":
        scores["九太"] += 2
    elif q2 == "自分なりの方法で解決する":
        scores["すず"] += 2
    else:
        scores["くんちゃん"] += 2

    # Q3
    if q3 == "友情":
        scores["健二"] += 2
    elif q3 == "家族":
        scores["花"] += 2
    elif q3 == "成長":
        scores["九太"] += 2
    else:
        scores["すず"] += 2

    # Q4
    if q4 == "明るい":
        scores["健二"] += 1
    elif q4 == "優しい":
        scores["花"] += 2
    elif q4 == "努力家":
        scores["九太"] += 2
    else:
        scores["くんちゃん"] += 2

    # Q5
    if q5 == "仲間との協力":
        scores["健二"] += 2
    elif q5 == "家族愛":
        scores["花"] += 2
    elif q5 == "成長物語":
        scores["九太"] += 2
    else:
        scores["くんちゃん"] += 2

    # Q6
    if q6 == "一緒に考える":
        scores["健二"] += 2
    elif q6 == "優しく聞く":
        scores["花"] += 2
    elif q6 == "励ます":
        scores["九太"] += 2
    else:
        scores["すず"] += 2

    # Q7
    if q7 == "みんなが集まる場所":
        scores["健二"] += 2
    elif q7 == "自然の中":
        scores["花"] += 2
    elif q7 == "修行できる場所":
        scores["九太"] += 2
    else:
        scores["くんちゃん"] += 2

    # Q8
    if q8 == "協調性":
        scores["健二"] += 2
    elif q8 == "思いやり":
        scores["花"] += 2
    elif q8 == "努力":
        scores["九太"] += 2
    else:
        scores["すず"] += 2

    # 同点対策
    max_score = max(scores.values())

    candidates = [
        name for name, score in scores.items()
        if score == max_score
    ]

    result = random.choice(candidates)

    st.divider()
    st.header("🎉 診断結果")

    if result == "健二":

        st.balloons()
        st.image("kenji.jpg", use_container_width=True)

        st.success("あなたは『健二タイプ』です！")

        st.subheader("🌟 性格診断")
        st.write("""
        ・協調性が高い
        ・仲間を大切にする
        ・責任感がある
        ・困った人を助ける
        """)

        st.subheader("🎬 おすすめ映画")
        st.write("サマーウォーズ")

    elif result == "花":

        st.snow()
        st.image("hana.jpg", use_container_width=True)

        st.success("あなたは『花タイプ』です！")

        st.subheader("🌟 性格診断")
        st.write("""
        ・思いやりがある
        ・優しい
        ・家族想い
        ・面倒見が良い
        """)

        st.subheader("🎬 おすすめ映画")
        st.write("おおかみこどもの雨と雪")

    elif result == "九太":

        st.image("kyuta.jpg", use_container_width=True)

        st.success("あなたは『九太タイプ』です！")

        st.subheader("🌟 性格診断")
        st.write("""
        ・努力家
        ・負けず嫌い
        ・行動力がある
        ・挑戦を楽しめる
        """)

        st.subheader("🎬 おすすめ映画")
        st.write("バケモノの子")

    elif result == "すず":

        st.balloons()
        st.image("suzu.jpg", use_container_width=True)

        st.success("あなたは『すずタイプ』です！")

        st.subheader("🌟 性格診断")
        st.write("""
        ・感受性豊か
        ・夢を大切にする
        ・表現力がある
        ・自分らしさを持っている
        """)

        st.subheader("🎬 おすすめ映画")
        st.write("竜とそばかすの姫")

    else:

        st.image("kunchan.jpg", use_container_width=True)

        st.success("あなたは『くんちゃんタイプ』です！")

        st.subheader("🌟 性格診断")
        st.write("""
        ・好奇心旺盛
        ・想像力豊か
        ・新しいことが好き
        ・自由な発想を持つ
        """)

        st.subheader("🎬 おすすめ映画")
        st.write("未来のミライ")

    
    st.divider()

    st.subheader("💡 ワンポイントアドバイス")

    advice = {
        "健二": "周りとのつながりを大切にするとさらに成長できます。",
        "花": "時には自分自身のことも大切にしましょう。",
        "九太": "継続する力があなたの最大の武器です。",
        "すず": "自分らしさを信じることで魅力が輝きます。",
        "くんちゃん": "好奇心を大切にすると新しい発見が待っています。"
    }

    st.info(advice[result])

