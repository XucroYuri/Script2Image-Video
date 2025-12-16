# AI Image & Video Generator

[English](README.md) | [日本語](README_ja.md) | [中文](README_zh.md)

An AI-powered image and video generation application based on React frontend and Python backend. It automatically generates high-quality visual content by parsing JSON configuration files.

## 🌟 Features

- **🤖 AI-Powered**: Integrated with Google Gemini and Veo APIs for high-quality content generation.
- **📋 Configurable**: Define generation rules via JSON configuration files, flexible and controllable.
- **🎨 Intelligent Processing**: Automatically processes prompts, supporting style templates and reference replacement.
- **⚡ Efficient**: Supports batch processing and parallel generation of multiple scenes.
- **💻 Cross-Platform**: Supports Windows, macOS, and Linux deployment.
- **🌐 Modern**: Built with React + FastAPI technology stack, offering a user-friendly interface.

## 🚀 Quick Start

### Requirements

- **Node.js**: ≥ 16.0.0
- **Python**: ≥ 3.9.0
- **OS**: Windows 10+/macOS 10.15+/Ubuntu 20.04+

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/XucroYuri/Script2Image-Video.git
cd ai-image-video-generator
```

2. **Install Backend Dependencies**
```bash
cd backend
pip install -r requirements.txt
```

3. **Install Frontend Dependencies**
```bash
cd ../frontend
npm install
```

4. **Configure API Keys**
```bash
# Copy env template
cp .env.example .env

# Edit .env and add your API keys
GEMINI_API_KEY=your_gemini_api_key_here
VEO_API_KEY=your_veo_api_key_here
```

5. **Start Services**
```bash
# Start Backend (in backend directory)
uvicorn main:app --reload --port 8000

# Start Frontend (in frontend directory)
npm run dev
```

6. **Access Application**
Open browser and visit `http://localhost:5173`

## 📖 Usage Guide

### 1. Prepare Configuration

Create a JSON configuration file like this:

```json
{
  "project_id": "project-001",
  "project_name": "My First AI Project",
  "scenes": [
    {
      "scene_id": "scene-001",
      "name": "Opening Scene",
      "shots": [
        {
          "shot_id": "shot-001",
          "name": "Wide Shot",
          "order_index": 1,
          "nano_banana_pro_prompts": {
            "start": "A beautiful sunrise scene, [universal_style_block]",
            "middle": "The sun rises slowly, sky turns gradient",
            "end": "Sunlight hits the ground, everything comes to life"
          },
          "veo_3_1_prompt": "Natural scenery at sunrise, soft light changes"
        }
      ]
    }
  ]
}
```

### 2. Upload Configuration

- Drag and drop JSON file to the upload area on the homepage.
- Or click the upload button to select a file.
- The system will automatically parse and display the project preview.

### 3. Configure Parameters

- Set image generation parameters (optional).
- Set video generation parameters (optional).
- Preview generation effects.

### 4. Start Generation

- Click the "Start Generation" button.
- View generation progress in real-time.
- Monitor detailed generation logs.

### 5. Download Results

- View results after generation is complete.
- Support batch download of all content.
- Selectively download specific files.

## 🏗️ Project Structure

```
App/
├── frontend/                    # React Frontend
│   ├── src/
│   │   ├── components/         # UI Components
│   │   ├── pages/             # Page Components
│   │   ├── services/          # API Services
│   │   ├── utils/             # Utilities
│   │   └── types/             # TypeScript Types
│   ├── public/
│   └── package.json
├── backend/                     # Python Backend
│   ├── app/
│   │   ├── api/               # API Routes
│   │   ├── core/              # Core Config
│   │   ├── models/            # Data Models
│   │   ├── services/          # Business Logic
│   │   └── utils/             # Utilities
│   ├── requirements.txt
│   └── main.py
├── input/                       # Input Directory
├── output/                      # Output Directory
├── logs/                        # Logs Directory
├── docs/                        # Documentation
└── scripts/                     # Deployment Scripts
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|--------|------|--------|
| `GEMINI_API_KEY` | Google Gemini API Key | Required |
| `VEO_API_KEY` | Google Veo API Key | Required |
| `MAX_CONCURRENT_TASKS` | Max concurrent tasks | 5 |
| `MAX_FILE_SIZE` | Max file size (MB) | 500 |
| `OUTPUT_DIR` | Output directory path | ./output |
| `LOG_LEVEL` | Log level | INFO |

### Config Example

`.env`:
```bash
# API Config
GEMINI_API_KEY=your_gemini_api_key_here
VEO_API_KEY=your_veo_api_key_here

# System Config
MAX_CONCURRENT_TASKS=10
MAX_FILE_SIZE=500
OUTPUT_DIR=./output
LOG_LEVEL=INFO

# Advanced Config
GEMINI_MODEL=models/gemini-3-pro-image-preview
VEO_MODEL=models/veo-2.0-generate-001
DEFAULT_IMAGE_QUALITY=high
DEFAULT_VIDEO_DURATION=5
```

## 🎯 Core Functions

### Image Generation
- Supports start/middle/end frame generation.
- Automatically processes placeholders in prompts.
- Supports reference replacement.
- High-quality image output.

### Video Generation
- Generates video based on image sequences.
- Supports text-to-video generation.
- Adjustable video parameters (duration, resolution, etc.).
- Multiple output format support.

### Intelligent Processing
- Automatic JSON parsing.
- Prompt preprocessing.
- Batch task management.
- Error retry mechanism.

### User Interface
- Drag-and-drop file upload.
- Real-time progress display.
- Visual parameter configuration.
- Responsive design.

## 📊 Roadmap

- ✅ Project Architecture Design
- ✅ Technical Documentation
- 🔄 Backend Core Development
- ⏳ Frontend Interface Development
- ⏳ API Integration Testing
- ⏳ UI Optimization
- ⏳ Performance Optimization
- ⏳ Documentation Polish
- ⏳ Open Source Preparation

## 🤝 Contributing

We welcome community contributions! Please check [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add some amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Create Pull Request

## 📝 Documentation

- [Development Plan](docs/development_plan.md)
- [Technical Architecture](docs/technical_architecture.md)
- [Product Requirements](docs/product_requirements.md)
- [API Reference](docs/api_reference.md)
- [User Guide](docs/user_guide.md)

## 🐛 Issues

If you encounter any problems, please report them via:

- 📧 Email: support@example.com
- 💬 [Discord Community](https://discord.gg/example)
- 🐙 [GitHub Issues](https://github.com/XucroYuri/Script2Image-Video/issues)
- 📖 [FAQ](docs/faq.md)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Google AI](https://ai.google/) - Gemini and Veo APIs
- [React](https://reactjs.org/) - Frontend Framework
- [FastAPI](https://fastapi.tiangolo.com/) - Backend Framework
- [Vite](https://vitejs.dev/) - Build Tool
- [Tailwind CSS](https://tailwindcss.com/) - CSS Framework

## 📞 Contact

- 💼 Homepage: [https://github.com/XucroYuri/Script2Image-Video](https://github.com/XucroYuri/Script2Image-Video)

---

⭐ Star us on GitHub if this project helps you!

**Made with ❤️ by the AI Image Video Generator Team**

---

## 📜 Special Declaration

**The demo script in this project (located in `input/Visual_Development_Prompts_Nano_Veo.json`) is a creative work strictly based on authentic historical records:**

- **2 Historical Letters from Japanese Soldiers**: Derived from letters displayed at the 2025 New Cultural Relics and Historical Materials Release Conference held by the Memorial Hall of the Victims in Nanjing Massacre by Japanese Invaders. These two letters nakedly reveal the atrocities committed by the Japanese army during the Nanjing Massacre from the perspective of the perpetrators themselves.
- **"Investigation Record of the Military Tribunal for the Trial of War Criminals of the Ministry of National Defense regarding the Burying of Bodies by Tongshantang"**: Dated January 25, 1947, File No. 593/870, currently held by the Second Historical Archives of China.

**Remember History, Cherish Peace:**

We deeply mourn the 300,000 compatriots who were brutally slaughtered in the Nanjing Massacre. History cannot be tampered with, and the truth cannot be erased. We firmly oppose any actions that glorify wars of aggression or attempt to revive militarism.

We express strong dissatisfaction, severe condemnation, and high vigilance regarding the Japanese side's long-standing refusal to acknowledge the facts of the Nanjing Massacre, their blatant tampering with history textbooks, their refusal to offer a sincere apology, as well as recent attempts to revise the Peace Constitution, break through the principle of "exclusively defense-oriented policy," and renew talk of military intervention in neighboring countries in a vain attempt to repeat aggression and expansion.

Past experience, if not forgotten, is a guide for the future. Only by facing history squarely can we look forward to the future.
