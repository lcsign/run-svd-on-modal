 

---

# 🎬 SVD 图像生成视频工具

**run-svd-on-modal** 是一个基于 **Stable Video Diffusion (SVD)** 模型的云端推理项目，结合 **Modal** 云算力平台，让你只需一张静态图像，就能快速生成自然流畅的视频。  
无需本地 GPU、无需复杂环境配置，甚至不需要写一行代码。

---

- **一键生成视频**：本地上传图片，自动生成视频和逐帧图像序列  
- **云端 GPU 推理**：利用 Modal 云算力，高效完成视频生成  
- **可调参数**：帧数、推理步数、FPS 等均可自定义  
- **多格式输出**：生成 `.mp4` 视频和 `.png` 帧图像  
- **零命令行门槛**：配套批处理脚本，双击即可运行  

---

## 📦 环境准备

### 必备条件
1. **Python 3.10+**  
2. **Modal 账号**（已安装 CLI 工具）  
3. **Hugging Face 账号**（并接受 SVD 模型协议）  
4. **Hugging Face Token**（具备模型访问权限）  

---

## ⚙ 安装与配置

### 1️⃣ 注册并配置 Modal
- 打开 [Modal 官网](https://modal.com) 注册账号  
- 安装 CLI 工具：
```bash
pip install modal
```
- 登录授权：
```bash
modal token set
```

### 2️⃣ 克隆仓库
```bash
git clone git@github.com:lcsign/run-svd-on-modal.git
cd run-svd-on-modal
```

### 3️⃣ 安装依赖（建议虚拟环境）
```bash
python -m venv .venv
# Windows PowerShell
. .\.venv\Scripts\Activate.ps1
# macOS / Linux
# source .venv/bin/activate

pip install -r requirements.txt
```

### 4️⃣ 准备输入图像
- 将要生成视频的图片放到：
```
assets/input.png
```
- 建议分辨率：`1024×576`  
- 文件名必须为 `input.png`

---

## 🚀 使用方法

### 一键运行（推荐）
在项目根目录双击：
```
start.bat
```
脚本会自动：
1. 上传图片到 Modal Volume  
2. 远程运行推理脚本  
3. 下载生成的视频和帧图像到 `output/` 目录  

---

## 📂 输出结果
- `output/input.mp4`：生成的视频文件  
- `output/frames/`：逐帧图像序列  

---

## 🔧 高级用法（命令行）
如果你想自定义参数，可以直接运行：
```bash
modal run modal_app.py::infer \
  --input_path assets/input.png \
  --frames 25 \
  --steps 30 \
  --fps 12
```
可选参数：
| 参数       | 说明             | 默认值 |
|------------|------------------|--------|
| `--frames` | 视频帧数         | 25     |
| `--steps`  | 推理步数         | 30     |
| `--fps`    | 每秒帧数         | 12     |

---

## 🔍 常见问题

**1. 第一次运行很慢**  
- 因为需要下载模型权重，可使用 Modal Volume 缓存，加快后续运行  

**2. GitHub 推送被拦截**  
- 原因：硬编码了 Token  
- 解决：用 `.env` 管理，并清理提交历史中的敏感信息  

**3. 视频生成效果不理想**  
- 尝试调整帧数、步数、FPS  
- 使用更清晰、主体突出的输入图像  

---

## 📁 项目结构建议
```
run-svd-on-modal/
├─ modal_app.py         # Modal 推理入口
├─ src/svd_runner/      # 推理逻辑与工具函数
├─ assets/input.png     # 输入图片
├─ output/              # 输出视频与帧图像
├─ requirements.txt
├─ .env.example
├─ .gitignore
└─ start.bat
```
太棒了！你这个更新听起来非常工程化，尤其是“套娃式多层封装”——这说明你把逻辑模块化得很彻底，利于维护和扩展。下面是我为你生成的一段 `README.md` 更新内容，你可以直接复制粘贴进去，也可以让我帮你进一步润色或扩展：

---

```markdown
## 🔄 更新说明（Update Log）

### 2025-08-14
- ✨ 新增 Gradio UI：支持图形界面上传文件、查看推理结果
- 🧩 引入多层封装架构：
  - 核心推理逻辑与参数解析分离
  - UI 层与后端逻辑解耦，支持快速替换或扩展
  - 支持本地与云端（Modal）部署的统一接口调用
- 🛠️ 优化模块结构：
  - 所有功能封装为独立模块，便于调试与复用
  - 参数传递支持嵌套配置，提升灵活性

## 🚀 使用方式（Usage）

### 启动 Gradio UI
```bash
python app.py
```

### 本地命令行推理
```bash
python run.py --input ./data --output ./results
```

### 云端部署（Modal）
```bash
modal deploy --name svd_runner
```

## 📦 依赖环境（Requirements）
- Python 3.10+
- Gradio
- Modal
- ffmpeg
```

---



---


