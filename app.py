import streamlit as st
from search_google import google_search
from score_post import score_post
import pandas as pd

# 🔑 APIキー入力（安全に保管するならStreamlit Secretsが理想）
serpapi_key = c7cee1fdb1e4924a31958879d1f6d0971e4c157c4431d69dc275b06891535c7f
openai_key = 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

st.title("🔍 探客くん - 新規出店スカウター")

query = st.text_input("検索ワードを入力（例：美容室 大宮 open）")

if st.button("検索する"):
    with st.spinner("Google検索中..."):
        raw_results = google_search(query, serpapi_key)

    scored_results = []
    with st.spinner("GPTでスコア判定中..."):
        for r in raw_results:
            score = score_post(r["snippet"], openai_key)
            scored_results.append({
                "タイトル": r["title"],
                "抜粋": r["snippet"],
                "URL": r["link"],
                "新店らしさスコア": score
            })

    df = pd.DataFrame(scored_results).sort_values(by="新店らしさスコア", ascending=False)
    st.success("結果を表示します！")
    st.dataframe(df, use_container_width=True)
