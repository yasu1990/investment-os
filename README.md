# investment-os

小型株の中から「10倍候補」を効率的に発見するための  
日次スクリーニングOS。

---

## 目的

- 将来10倍以上になる可能性のある銘柄を早期に見つける
- 高値掴みを避ける
- 毎日すべての銘柄を見ないための判断基準を作る

本プロジェクトは売買を自動化しない。  
人間が「見るべき銘柄」を数本に絞るためのOS。

---

## 基本思想

### daily OS（毎日回す）

以下を機械的に判定する。

- 今は安値圏か（price_position）
- 出来高に異変が出ているか（volume_ratio）
- 出来高が連続して増えているか（volume_trend）
- 過去に急騰実績があるか（historical_spike）

これらを統合して score（総合評価）を算出し、  
今日見るべき銘柄だけを抽出する。

---

### quarterly / event OS（別機能）

- 四季報（売上成長など）
- 業績・材料系の評価

※ 毎日回さない  
※ イベント発生時のみ実行する別機能として設計

---

## 使い方（daily）

### 1. ユニバースを読み込む

- python
- from core.universe.load_universe import load_universe
- from core.universe.market_cap_filter import filter_small_caps

### 2. 小型株に絞る（時価総額150億円以下）
- all_tickers = load_universe("data/universe_smallcaps.csv")
- small_caps = filter_small_caps(all_tickers)

### 3. daily report を生成する
- from core.report.daily_report import generate_daily_report

report = generate_daily_report(
    tickers=small_caps,
    top_n=20
)
- 出力カラムの意味
- カラム	意味
- ticker	銘柄コード
- company_name	会社名（参考情報）
- price_position	過去3年での価格位置（0=底, 10=天井）
- volume_ratio	当日出来高 ÷ 過去平均出来高
- volume_trend	出来高が連続増加しているか
- historical_spike	過去に急騰実績があるか
- score	総合評価（見る価値）
- 運用ルール（目安）

score >= 10
→ 必ず見る

score 6〜9
→ 余裕があれば見る

score < 6
→ 見ない

特に注目する条件：

price_position が低い

volume_trend = True

ディレクトリ構成
core/
  fetch/        価格データ取得
  features/     特徴量（価格・出来高など）
  universe/     銘柄集合・フィルタ
  report/       daily report
  scoring/      スコア計算
data/
  universe_smallcaps.csv

注意点・割り切り

売買判断は行わない

日本語銘柄名は完全自動取得しない（運用優先）

IPO・材料株は人間が最終判断する前提

ステータス

daily OS：実装済み

四季報 feature：別機能として後続実装予定


---
