# AI图像视频生成应用

一个基于React前端和Python后端的AI图像视频生成应用，通过解析JSON配置文件，自动生成高质量的图像和视频内容。

## 🌟 项目特色

- **🤖 AI驱动**: 集成Google Gemini和Veo API，生成高质量视觉内容
- **📋 配置化**: 通过JSON配置文件定义生成规则，灵活可控
- **🎨 智能处理**: 自动处理提示词，支持样式模板和引用替换
- **⚡ 高效生成**: 支持批量处理，并行生成多个场景内容
- **💻 跨平台**: 支持Windows、macOS、Linux多平台部署
- **🌐 现代化**: 采用React + FastAPI技术栈，界面友好

## 🚀 快速开始

### 环境要求

- **Node.js**: ≥ 16.0.0
- **Python**: ≥ 3.9.0
- **操作系统**: Windows 10+/macOS 10.15+/Ubuntu 20.04+

### 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/your-username/ai-image-video-generator.git
cd ai-image-video-generator
```

2. **安装后端依赖**
```bash
cd backend
pip install -r requirements.txt
```

3. **安装前端依赖**
```bash
cd ../frontend
npm install
```

4. **配置API密钥**
```bash
# 复制环境变量模板
cp .env.example .env

# 编辑.env文件，填入你的API密钥
GEMINI_API_KEY=your_gemini_api_key_here
VEO_API_KEY=your_veo_api_key_here
```

5. **启动服务**
```bash
# 启动后端服务（在backend目录）
uvicorn main:app --reload --port 8000

# 启动前端服务（在frontend目录）
npm run dev
```

6. **访问应用**
打开浏览器访问 `http://localhost:5173`

## 📖 使用说明

### 1. 准备配置文件

创建JSON配置文件，格式如下：

```json
{
  "project_id": "project-001",
  "project_name": "我的第一个AI项目",
  "scenes": [
    {
      "scene_id": "scene-001",
      "name": "开场场景",
      "shots": [
        {
          "shot_id": "shot-001",
          "name": "远景镜头",
          "order_index": 1,
          "nano_banana_pro_prompts": {
            "start": "一个美丽的日出场景，[universal_style_block]",
            "middle": "太阳缓缓升起，天空呈现渐变色",
            "end": "阳光洒向大地，万物复苏"
          },
          "veo_3_1_prompt": "日出时分的自然风光，柔和的光线变化"
        }
      ]
    }
  ]
}
```

### 2. 上传配置文件

- 在主页拖拽JSON文件到上传区域
- 或点击上传按钮选择文件
- 系统会自动解析并显示项目预览

### 3. 配置生成参数

- 设置图像生成参数（可选）
- 设置视频生成参数（可选）
- 预览生成效果

### 4. 开始生成

- 点击"开始生成"按钮
- 实时查看生成进度
- 监控详细的生成日志

### 5. 下载结果

- 生成完成后查看结果
- 支持批量下载所有内容
- 可选择性下载特定文件

## 🏗️ 项目结构

```
App/
├── frontend/                    # React前端项目
│   ├── src/
│   │   ├── components/         # UI组件
│   │   ├── pages/             # 页面组件
│   │   ├── services/          # API服务
│   │   ├── utils/             # 工具函数
│   │   └── types/             # TypeScript类型定义
│   ├── public/
│   └── package.json
├── backend/                     # Python后端项目
│   ├── app/
│   │   ├── api/               # API路由
│   │   ├── core/              # 核心配置
│   │   ├── models/            # 数据模型
│   │   ├── services/          # 业务逻辑
│   │   └── utils/             # 工具函数
│   ├── requirements.txt
│   └── main.py
├── input/                       # 输入文件目录
├── output/                      # 输出文件目录
├── logs/                        # 日志文件目录
├── docs/                        # 项目文档
└── scripts/                     # 部署脚本
```

## 🔧 配置说明

### 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `GEMINI_API_KEY` | Google Gemini API密钥 | 必填 |
| `VEO_API_KEY` | Google Veo API密钥 | 必填 |
| `MAX_CONCURRENT_TASKS` | 最大并发任务数 | 5 |
| `MAX_FILE_SIZE` | 最大文件大小(MB) | 500 |
| `OUTPUT_DIR` | 输出目录路径 | ./output |
| `LOG_LEVEL` | 日志级别 | INFO |

### 配置文件示例

`.env`:
```bash
# API配置
GEMINI_API_KEY=your_gemini_api_key_here
VEO_API_KEY=your_veo_api_key_here

# 系统配置
MAX_CONCURRENT_TASKS=10
MAX_FILE_SIZE=500
OUTPUT_DIR=./output
LOG_LEVEL=INFO

# 高级配置
GEMINI_MODEL=models/gemini-3-pro-image-preview
VEO_MODEL=models/veo-2.0-generate-001
DEFAULT_IMAGE_QUALITY=high
DEFAULT_VIDEO_DURATION=5
```

## 🎯 核心功能

### 图像生成
- 支持start/middle/end三帧图像生成
- 自动处理提示词中的占位符
- 支持引用替换功能
- 高质量图像输出

### 视频生成
- 基于图像序列生成视频
- 支持纯文本生成视频
- 可调节视频参数（时长、分辨率等）
- 多种输出格式支持

### 智能处理
- JSON文件自动解析
- 提示词预处理
- 批量任务管理
- 错误重试机制

### 用户界面
- 拖拽上传文件
- 实时进度显示
- 可视化参数配置
- 响应式设计

## 📊 开发进度

- ✅ 项目架构设计
- ✅ 技术文档编写
- 🔄 后端核心功能开发
- ⏳ 前端界面开发
- ⏳ API集成测试
- ⏳ 用户界面优化
- ⏳ 性能优化
- ⏳ 文档完善
- ⏳ 开源发布准备

## 🤝 贡献指南

我们欢迎社区贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与项目开发。

### 开发环境设置

1. Fork项目仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建Pull Request

## 📝 文档

- [开发计划](docs/development_plan.md) - 详细的开发计划和里程碑
- [技术架构](docs/technical_architecture.md) - 系统架构和技术细节
- [产品需求](docs/product_requirements.md) - 功能需求和UI设计
- [API文档](docs/api_reference.md) - API接口文档
- [用户指南](docs/user_guide.md) - 详细使用教程

## 🐛 问题反馈

如果您在使用过程中遇到问题，请通过以下方式反馈：

- 📧 发送邮件至: support@example.com
- 💬 加入我们的 [Discord社区](https://discord.gg/example)
- 🐙 在 [GitHub Issues](https://github.com/your-username/ai-image-video-generator/issues) 提交问题
- 📖 查看 [FAQ文档](docs/faq.md)

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- [Google AI](https://ai.google/) - 提供Gemini和Veo API
- [React](https://reactjs.org/) - 前端框架
- [FastAPI](https://fastapi.tiangolo.com/) - 后端框架
- [Vite](https://vitejs.dev/) - 构建工具
- [Tailwind CSS](https://tailwindcss.com/) - 样式框架

## 📞 联系我们

- 💼 项目主页: [https://github.com/your-username/ai-image-video-generator](https://github.com/your-username/ai-image-video-generator)
- 📧 邮箱: contact@example.com
- 🐦 Twitter: [@AIContentGen](https://twitter.com/AIContentGen)
- 💼 LinkedIn: [AI Content Generator](https://linkedin.com/company/ai-content-generator)

---

⭐ 如果这个项目对您有帮助，请给我们一个星标！

**Made with ❤️ by the AI Image Video Generator Team**