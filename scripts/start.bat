@echo off
chcp 65001

title Modal SVD 一键视频生成
setlocal enabledelayedexpansion

:: 设置路径变量
set INPUT_PATH=D:\svd_runner\assets\input.png
set OUTPUT_VIDEO=D:\svd_runner\output\input.mp4
set OUTPUT_FRAMES=D:\svd_runner\output\frames

:: 检查输入文件是否存在
if not exist "%INPUT_PATH%" (
    echo 输入文件不存在: %INPUT_PATH%
    pause
    exit /b
)

echo 清理远程缓存...
modal volume rm svd-cache /input.png

echo 上传输入文件到远程 Volume...
modal volume put svd-cache "%INPUT_PATH%" /input.png

echo 运行 Modal 脚本生成视频...
modal run generate_video_modal.py

echo 下载生成的视频文件...
modal volume get svd-cache /video/input.mp4 "%OUTPUT_VIDEO%" --force

echo 下载生成的帧图像目录...
modal volume get svd-cache /frames "%OUTPUT_FRAMES%" --force

echo 所有步骤完成！
pause

