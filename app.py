import streamlit as st
import pandas as pd

# --- モック投稿データ ---
mock_posts = [
    {
        "username": "@beauty_salon_omiya",
        "date": "2025-07-01",
        "text": "【新店舗OPEN】7月7日から新しくオープンします！ご予約受付中🌿"
    },
    {
        "username": "@hairplace_kawaguchi",
        "date": "2025-06-28",
        "text": "リニューアル完了しました！今まで以上の空間でお迎えします✨"
    },
    {
        "username": "@salon_diary",
        "date": "2025-07-01",
        "text": "週末のご予約、まだ少し空きがあります♪当日予約もOK！"
    }
]

# --- 投稿スコアリングロジック ---
def mock_score_post(text):
    if "オープン" in text or "OPEN" in text:
        return 90
    elif "リニューアル" in text:
        return 75
    else:
        return 30

# --- Streamlit UI ---
st.title("🧭 探客くん - 新店発見ツール（プロトタイプ）")

# 入力欄
st.subheader("🔍 キーワードを入力してください（例：美容室 大宮 open）")
keywords = st.text_input("キーワード（半角スペース区切り）", "")

# 検索ボタン
if st.button("検索する"):
    # 結果生成
    results = []
    for post in mock_posts:
        score = mock_score_post(post["text"])
        results.append({
            "ユーザー名": post["username"],
            "投稿日": post["date"],
            "投稿内容": post["text"],
            "新店らしさスコア": f"{score} %"
        })
    
    df = pd.DataFrame(results)
    st.success("検索が完了しました！")
    st.dataframe(df, use_container_width=True)
