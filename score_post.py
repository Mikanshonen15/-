import openai

def score_post(snippet, openai_api_key):
    prompt = f"""
以下は美容室に関する投稿の抜粋です。この文章が「美容室の新規オープン」または「リニューアル情報」である可能性を、0〜100%で評価してください。

---
投稿内容:「{snippet}」
---
あなたの評価（数値のみ）:
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            api_key=openai_api_key  # 明示的にAPIキー指定
        )

        score_text = response["choices"][0]["message"]["content"].strip()
        # スコアとして使えるように数値変換
        score = int("".join(filter(str.isdigit, score_text)))
        return min(score, 100)  # 100を上限に
    except Exception as e:
        print(f"Error scoring post: {e}")
        return 0
