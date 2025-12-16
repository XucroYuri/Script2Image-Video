# AI画像・動画生成アプリ

[English](README.md) | [日本語](README_ja.md) | [中文](README_zh.md)

ReactフロントエンドとPythonバックエンドをベースにしたAI画像・動画生成アプリケーションです。JSON設定ファイルを解析し、高品質な画像や動画コンテンツを自動生成します。

## 🌟 特徴

- **🤖 AI駆動**: Google GeminiおよびVeo APIを統合し、高品質なビジュアルコンテンツを生成
- **📋 設定可能**: JSON設定ファイルで生成ルールを定義、柔軟な制御が可能
- **🎨 インテリジェント処理**: プロンプトを自動処理し、スタイルテンプレートや参照置換をサポート
- **⚡ 高効率**: バッチ処理と複数のシーンの並列生成をサポート
- **💻 クロスプラットフォーム**: Windows、macOS、Linuxでの展開をサポート
- **🌐 モダン**: React + FastAPI技術スタックを採用し、ユーザーフレンドリーなインターフェースを提供

## 🚀 クイックスタート

### 必要環境

- **Node.js**: ≥ 16.0.0
- **Python**: ≥ 3.9.0
- **OS**: Windows 10+/macOS 10.15+/Ubuntu 20.04+

### インストール手順

1. **リポジトリのクローン**
```bash
git clone https://github.com/XucroYuri/Script2Image-Video.git
cd ai-image-video-generator
```

2. **バックエンド依存関係のインストール**
```bash
cd backend
pip install -r requirements.txt
```

3. **フロントエンド依存関係のインストール**
```bash
cd ../frontend
npm install
```

4. **APIキーの設定**
```bash
# 環境変数テンプレートをコピー
cp .env.example .env

# .envファイルを編集し、APIキーを入力
GEMINI_API_KEY=your_gemini_api_key_here
VEO_API_KEY=your_veo_api_key_here
```

5. **サービスの起動**
```bash
# バックエンドの起動（backendディレクトリで）
uvicorn main:app --reload --port 8000

# フロントエンドの起動（frontendディレクトリで）
npm run dev
```

6. **アプリへのアクセス**
ブラウザで `http://localhost:5173` にアクセス

## 📖 使用ガイド

### 1. 設定ファイルの準備

以下のような形式のJSON設定ファイルを作成します：

```json
{
  "project_id": "project-001",
  "project_name": "私の初めてのAIプロジェクト",
  "scenes": [
    {
      "scene_id": "scene-001",
      "name": "オープニングシーン",
      "shots": [
        {
          "shot_id": "shot-001",
          "name": "ワイドショット",
          "order_index": 1,
          "nano_banana_pro_prompts": {
            "start": "美しい日の出の風景、[universal_style_block]",
            "middle": "太陽がゆっくりと昇り、空がグラデーションになる",
            "end": "日差しが大地に降り注ぎ、万物が蘇る"
          },
          "veo_3_1_prompt": "日の出の自然風景、柔らかな光の変化"
        }
      ]
    }
  ]
}
```

### 2. 設定ファイルのアップロード

- ホームページでアップロードエリアにJSONファイルをドラッグ＆ドロップ
- またはアップロードボタンをクリックしてファイルを選択
- システムが自動的に解析し、プロジェクトのプレビューを表示します

### 3. 生成パラメータの設定

- 画像生成パラメータの設定（オプション）
- 動画生成パラメータの設定（オプション）
- 生成効果のプレビュー

### 4. 生成開始

- 「生成開始」ボタンをクリック
- リアルタイムで生成の進捗を確認
- 詳細な生成ログを監視

### 5. 結果のダウンロード

- 生成完了後に結果を確認
- すべてのコンテンツの一括ダウンロードをサポート
- 特定のファイルを選択してダウンロード可能

## 🏗️ プロジェクト構造

```
App/
├── frontend/                    # Reactフロントエンド
│   ├── src/
│   │   ├── components/         # UIコンポーネント
│   │   ├── pages/             # ページコンポーネント
│   │   ├── services/          # APIサービス
│   │   ├── utils/             # ユーティリティ
│   │   └── types/             # TypeScript型定義
│   ├── public/
│   └── package.json
├── backend/                     # Pythonバックエンド
│   ├── app/
│   │   ├── api/               # APIルート
│   │   ├── core/              # コア設定
│   │   ├── models/            # データモデル
│   │   ├── services/          # ビジネスロジック
│   │   └── utils/             # ユーティリティ
│   ├── requirements.txt
│   └── main.py
├── input/                       # 入力ファイルディレクトリ
├── output/                      # 出力ファイルディレクトリ
├── logs/                        # ログファイルディレクトリ
├── docs/                        # ドキュメント
└── scripts/                     # デプロイスクリプト
```

## 🔧 設定説明

### 環境変数

| 変数名 | 説明 | デフォルト値 |
|--------|------|--------|
| `GEMINI_API_KEY` | Google Gemini APIキー | 必須 |
| `VEO_API_KEY` | Google Veo APIキー | 必須 |
| `MAX_CONCURRENT_TASKS` | 最大同時タスク数 | 5 |
| `MAX_FILE_SIZE` | 最大ファイルサイズ(MB) | 500 |
| `OUTPUT_DIR` | 出力ディレクトリパス | ./output |
| `LOG_LEVEL` | ログレベル | INFO |

### 設定例

`.env`:
```bash
# API設定
GEMINI_API_KEY=your_gemini_api_key_here
VEO_API_KEY=your_veo_api_key_here

# システム設定
MAX_CONCURRENT_TASKS=10
MAX_FILE_SIZE=500
OUTPUT_DIR=./output
LOG_LEVEL=INFO

# 高度な設定
GEMINI_MODEL=models/gemini-3-pro-image-preview
VEO_MODEL=models/veo-2.0-generate-001
DEFAULT_IMAGE_QUALITY=high
DEFAULT_VIDEO_DURATION=5
```

## 🎯 コア機能

### 画像生成
- start/middle/endの3フレーム画像生成をサポート
- プロンプト内のプレースホルダーを自動処理
- 参照置換機能をサポート
- 高品質な画像出力

### 動画生成
- 画像シーケンスに基づく動画生成
- テキストから動画への生成をサポート
- 動画パラメータの調整が可能（長さ、解像度など）
- 複数の出力フォーマットをサポート

### インテリジェント処理
- JSONファイルの自動解析
- プロンプトの前処理
- バッチタスク管理
- エラー再試行メカニズム

### ユーザーインターフェース
- ドラッグ＆ドロップによるファイルアップロード
- リアルタイム進捗表示
- 視覚的なパラメータ設定
- レスポンシブデザイン

## 📊 ロードマップ

- ✅ プロジェクトアーキテクチャ設計
- ✅ 技術ドキュメント作成
- 🔄 バックエンドコア機能開発
- ⏳ フロントエンドインターフェース開発
- ⏳ API統合テスト
- ⏳ UI最適化
- ⏳ パフォーマンス最適化
- ⏳ ドキュメントの改善
- ⏳ オープンソース公開準備

## 🤝 貢献ガイド

コミュニティからの貢献を歓迎します！プロジェクト開発への参加方法については [CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。

### 開発環境のセットアップ

1. リポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## 📝 ドキュメント

- [開発計画](docs/development_plan.md) - 詳細な開発計画とマイルストーン
- [技術アーキテクチャ](docs/technical_architecture.md) - システムアーキテクチャと技術詳細
- [製品要件](docs/product_requirements.md) - 機能要件とUIデザイン
- [APIリファレンス](docs/api_reference.md) - APIインターフェースドキュメント
- [ユーザーガイド](docs/user_guide.md) - 詳細な使用チュートリアル

## 🐛 問題報告

使用中に問題が発生した場合は、以下の方法で報告してください：

- 📧 メール送信: support@example.com
- 💬 [Discordコミュニティ](https://discord.gg/example)に参加
- 🐙 [GitHub Issues](https://github.com/XucroYuri/Script2Image-Video/issues) で問題を提出
- 📖 [FAQドキュメント](docs/faq.md)を確認

## 📄 ライセンス

本プロジェクトは MIT ライセンスの下で公開されています - 詳細は [LICENSE](LICENSE) ファイルをご覧ください。

## 🙏 謝辞

- [Google AI](https://ai.google/) - GeminiおよびVeo APIの提供
- [React](https://reactjs.org/) - フロントエンドフレームワーク
- [FastAPI](https://fastapi.tiangolo.com/) - バックエンドフレームワーク
- [Vite](https://vitejs.dev/) - ビルドツール
- [Tailwind CSS](https://tailwindcss.com/) - スタイルフレームワーク

## 📞 お問い合わせ

- 💼 プロジェクトホームページ: [https://github.com/XucroYuri/Script2Image-Video](https://github.com/XucroYuri/Script2Image-Video)

---

⭐ このプロジェクトが役立った場合は、スターをお願いします！

**Made with ❤️ by the AI Image Video Generator Team**

---

## 📜 特別声明

**本プロジェクトのデモ脚本（`input/Visual_Development_Prompts_Nano_Veo.json` に配置）は、真実の歴史史料に厳格に基づき創作・演出されたものです：**

- **日本軍兵士の手紙2通**: 侵華日軍南京大屠殺遇難同胞紀念館で開催された2025年新収集文物史料発表会で展示された手紙を取材源としています。これら2通の手紙は、加害者自身の視点から、南京大虐殺期間中の日本軍の暴行を赤裸々に暴いています。
- **『同善堂による遺体埋葬に関する国防部戦犯裁判軍事法廷の調査調書』**: 1947年1月25日付、整理番号593/870、中国第二歴史公文書館所蔵。

**歴史を銘記し、平和を大切にする：**

私たちは、南京大虐殺で惨殺された30万人の同胞に深い哀悼の意を表します。歴史の改竄は許されず、真実を抹殺することはできません。私たちは、侵略戦争を美化し、軍国主義を復活させようとするいかなる行為にも断固として反対します。

日本側が長年にわたり南京大虐殺の史実を認めず、歴史教科書を公然と改竄し、真摯な謝罪を拒否していること、さらに最近の平和憲法改正の試み、「専守防衛」の原則を破り、周辺国への軍事介入に再び言及し、侵略と拡張を再現しようとする現状に対して、私たちは強い不満と厳重な非難、そして高度な警戒を表明します。

前事不忘、後事之師（過去を忘れず、未来の教訓とする）。歴史を直視してこそ、未来に向かうことができます。
