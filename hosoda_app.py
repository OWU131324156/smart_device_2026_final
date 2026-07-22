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

/* 全体背景 */
.stApp {
    background: linear-gradient(135deg, #f0fff8 0%, #e8f7ff 100%);
}

/* タイトル */
.main-title {
    text-align: center;
    color: #2e8b57;
    font-size: 3rem;
    font-weight: bold;
    margin-bottom: 10px;
}

/* 説明文 */
.subtitle {
    text-align: center;
    color: #5f9ea0;
    font-size: 1.1rem;
    margin-bottom: 30px;
}

/* 質問カード */
.question-card {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    border-left: 6px solid #7fd8be;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

/* ボタン */
.stButton > button {
    background: linear-gradient(90deg,#7fd8be,#87cefa);
    color: white;
    border: none;
    border-radius: 30px;
    height: 50px;
    width: 100%;
    font-size: 20px;
    font-weight: bold;
}

.stButton > button:hover {
    background: linear-gradient(90deg,#6bc9ad,#73c3f5);
    transform: scale(1.02);
}

/* ラジオボタンの文字 */
.stRadio label {
    color: #2f4f4f !important;
    font-weight: 500;
}

/* 結果表示 */
.result-box {
    background: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.1);
}

.question-card {
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(8px);

    padding: 15px;
    border-radius: 20px;

    box-shadow:
        0 8px 20px rgba(0,0,0,0.08),
        0 2px 6px rgba(0,0,0,0.05);

    margin-bottom: 10px;

    transition: all 0.3s ease;
}

.question-card:hover {
    transform: translateY(-3px);
    box-shadow:
        0 12px 28px rgba(0,0,0,0.12),
        0 4px 10px rgba(0,0,0,0.08);
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

