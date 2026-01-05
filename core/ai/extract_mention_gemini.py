import os
import json
import google.generativeai as genai

# Colabでは事前に環境変数をセットしておく
# os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY"

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "models/gemini-2.5-flash"


def extract_stock_mention(text: str) -> dict:
    """
    日本語テキストから銘柄言及を抽出する（Gemini使用）
    """

    prompt = f"""
以下の文章から、日本株の銘柄について言及している場合は情報を抽出してください。

文章:
{text}

出力は必ずJSONのみ。

出力形式:
{{
  "ticker": null または "1234.T",
  "company_name": "会社名（日本語）",
  "sentiment_score": -1.0〜1.0
}}

ルール:
- 銘柄コードが不明な場合 ticker は null
- ポジティブなら正、ネガティブなら負
"""

    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)

    try:
        return json.loads(response.text)
    except Exception:
        return {
            "ticker": None,
            "company_name": None,
            "sentiment_score": 0.0
        }
