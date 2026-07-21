from google import genai
import streamlit as st

api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)
MODEL_NAME = "gemini-3.5-flash"

# prompt = "こんにちは"

# response = client.models.generate_content(
#     model=MODEL_NAME,
#     concept=prompt,
# )
# st.write(response.text)


# # ページ設定
# st.set_page_config(
#     page_title="細田守キャラクター診断",
#     page_icon="🎬",
#     layout="centered"
# )

# st.title("🎬 細田守キャラクター診断")
# st.write("質問に答えて、あなたにぴったりのキャラクターと映画を見つけよう！")

# # ===== 質問 =====

# q1 = st.radio(
#     "休日はどう過ごしたい？",
#     ["友達と遊ぶ", "家族と過ごす", "新しいことに挑戦", "一人で好きなことをする"]
# )

# q2 = st.radio(
#     "困難に直面したら？",
#     ["仲間に相談する", "最後まで頑張る", "自分なりの方法で解決する", "じっくり考える"]
# )

# q3 = st.radio(
#     "一番大切なものは？",
#     ["友情", "家族", "成長", "夢"]
# )

# q4 = st.radio(
#     "周りからよく言われる性格は？",
#     ["明るい", "優しい", "努力家", "好奇心旺盛"]
# )

# q5 = st.radio(
#     "好きな物語は？",
#     ["仲間との協力", "家族愛", "成長物語", "不思議な冒険"]
# )

# # ===== 診断 =====

# if st.button("診断する 🎬"):

#     scores = {
#         "健二": 0,
#         "花": 0,
#         "九太": 0,
#         "すず": 0,
#         "くんちゃん": 0
#     }

#     # Q1
#     if q1 == "友達と遊ぶ":
#         scores["健二"] += 2
#     elif q1 == "家族と過ごす":
#         scores["花"] += 2
#     elif q1 == "新しいことに挑戦":
#         scores["九太"] += 2
#     else:
#         scores["くんちゃん"] += 2

#     # Q2
#     if q2 == "仲間に相談する":
#         scores["健二"] += 2
#     elif q2 == "最後まで頑張る":
#         scores["九太"] += 2
#     elif q2 == "自分なりの方法で解決する":
#         scores["すず"] += 2
#     else:
#         scores["くんちゃん"] += 2

#     # Q3
#     if q3 == "友情":
#         scores["健二"] += 2
#     elif q3 == "家族":
#         scores["花"] += 2
#     elif q3 == "成長":
#         scores["九太"] += 2
#     else:
#         scores["すず"] += 2

#     # Q4
#     if q4 == "明るい":
#         scores["健二"] += 2
#     elif q4 == "優しい":
#         scores["花"] += 2
#     elif q4 == "努力家":
#         scores["九太"] += 2
#     else:
#         scores["くんちゃん"] += 2

#     # Q5
#     if q5 == "仲間との協力":
#         scores["健二"] += 2
#     elif q5 == "家族愛":
#         scores["花"] += 2
#     elif q5 == "成長物語":
#         scores["九太"] += 2
#     else:
#         scores["くんちゃん"] += 2

#     result = max(scores, key=scores.get)

#     st.divider()
#     st.header("🎉 診断結果")

#     # ===== 健二 =====
#     if result == "健二":

#         st.balloons()

#         st.success("あなたは『健二タイプ』です！")

#         st.subheader("🌟 あなたの性格")
#         st.write("""
#         ・協調性がある  
#         ・仲間を大切にする  
#         ・困ったときに頼られる  
#         ・責任感が強い
#         """)

#         st.subheader("🎬 おすすめ映画")
#         st.write("サマーウォーズ")

#         st.info("""
#         あなたは周囲とのつながりを大切にするタイプです。
#         『サマーウォーズ』の世界観と相性抜群！
#         """)

#     # ===== 花 =====
#     elif result == "花":

#         st.snow()

#         st.success("あなたは『花タイプ』です！")

#         st.subheader("🌟 あなたの性格")
#         st.write("""
#         ・思いやりがある  
#         ・優しい  
#         ・家族想い  
#         ・面倒見が良い
#         """)

#         st.subheader("🎬 おすすめ映画")
#         st.write("おおかみこどもの雨と雪")

#         st.info("""
#         あなたは人を支えることに喜びを感じるタイプ。
#         温かい家族の物語に心を動かされるでしょう。
#         """)

#     # ===== 九太 =====
#     elif result == "九太":

#         st.success("あなたは『九太タイプ』です！")

#         st.subheader("🌟 あなたの性格")
#         st.write("""
#         ・努力家  
#         ・負けず嫌い  
#         ・チャレンジ精神がある  
#         ・成長意欲が高い
#         """)

#         st.subheader("🎬 おすすめ映画")
#         st.write("バケモノの子")

#         st.info("""
#         壁にぶつかっても前へ進む力があります。
#         成長物語との相性がとても高いタイプです。
#         """)

#     # ===== すず =====
#     elif result == "すず":

#         st.balloons()

#         st.success("あなたは『すずタイプ』です！")

#         st.subheader("🌟 あなたの性格")
#         st.write("""
#         ・感受性が豊か  
#         ・夢を大切にする  
#         ・自分らしさを追求する  
#         ・芸術的センスがある
#         """)

#         st.subheader("🎬 おすすめ映画")
#         st.write("竜とそばかすの姫")

#         st.info("""
#         あなたは自分の気持ちを大切にするタイプ。
#         音楽や感動的なストーリーと相性抜群です。
#         """)

#     # ===== くんちゃん =====
#     else:

#         st.success("あなたは『くんちゃんタイプ』です！")

#         st.subheader("🌟 あなたの性格")
#         st.write("""
#         ・好奇心旺盛  
#         ・自由な発想を持つ  
#         ・新しいことが好き  
#         ・想像力が豊か
#         """)

#         st.subheader("🎬 おすすめ映画")
#         st.write("未来のミライ")

#         st.info("""
#         あなたはワクワクする体験が好きなタイプ。
#         不思議な世界観を楽しめるでしょう。
#         """)

#     st.divider()

#     st.subheader("💡 ワンポイントアドバイス")

#     if result == "健二":
#         st.write("周囲を頼る力も、あなたの大切な才能です。")
#     elif result == "花":
#         st.write("時には自分自身を優先することも大切です。")
#     elif result == "九太":
#         st.write("焦らず一歩ずつ進むことで大きく成長できます。")
#     elif result == "すず":
#         st.write("自分らしさを大切にすると魅力がさらに輝きます。")
#     else:
#         st.write("好奇心を忘れずに新しいことへ挑戦してみましょう。")


import random
import streamlit as st

# --------------------
# ページ設定
# --------------------
st.set_page_config(
    page_title="細田守キャラクター診断",
    page_icon="🎬",
    layout="centered"
)

st.markdown(
    """
    <h1 style='text-align:center;'>
    🎬 細田守キャラクター診断
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("質問に答えて、あなたにぴったりのキャラクターを見つけよう！")

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
        scores["健二"] += 2
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
        scores["健二"] += 2
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
        st.image("images/kenji.jpg", use_container_width=True)

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
        st.image("images/hana.jpg", use_container_width=True)

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

        st.image("images/kyuta.jpg", use_container_width=True)

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
        st.image("images/suzu.jpg", use_container_width=True)

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

        st.image("images/mirai.jpg", use_container_width=True)

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