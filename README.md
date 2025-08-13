SVD 图像生成视频工具 是一个基于 Stable Video Diffusion 模型的本地自动化流程，结合 Modal 云端推理平台，用户只需准备一张图像并运行脚本，即可生成自然动作的视频，无需编写代码或配置模型。

✨ 项目功能
支持本地上传图像并自动生成视频

可自定义推理参数（帧数、步数、FPS）

使用 Modal 云端 GPU 进行高效推理

输出包括 .mp4 视频和 .png 帧图像序列

一键运行，无需命令行操作

🧑‍💻 使用教程
1️⃣ 注册并配置 Modal 账户
打开 https://modal.com 注册账户

安装 Modal 命令行工具：

bash
pip install modal
登录授权：

bash
modal token set
2️⃣ 克隆项目仓库
bash
git clone https://github.com/lcsign/run-svd-on-modal.git
cd run-svd-on-modal
3️⃣ 安装依赖库（推荐使用虚拟环境）
bash
pip install -r requirements.txt
4️⃣ 准备输入图像
将你要生成的视频图像放入项目目录下的：

assets/input.png
注意：图像将自动上传到 Modal 云端进行推理，请确保文件名为 input.png，分辨率建议为 1024×576。

5️⃣ 一键运行生成脚本
在项目根目录下双击运行：

start.bat
该脚本将自动执行以下操作：

上传图像到 Modal Volume

远程运行推理脚本

下载生成的视频和帧图像到本地 output/ 目录

📦 输出结果
output/input.mp4：生成的视频文件

output/frames/：逐帧图像序列
