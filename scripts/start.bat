@echo off
chcp 65001
title Modal SVD 一键视频生成
setlocal enabledelayedexpansion

:: %1 输入图片路径
:: %2 输出视频名（不含路径和后缀）
set INPUT_PATH=%~1
set BASENAME=%~n2
set OUTPUT_VIDEO=D:\svd_runner\output\%BASENAME%.mp4
set OUTPUT_FRAMES=D:\svd_runner\output\frames

if not exist "%INPUT_PATH%" (
    echo ❌ 输入文件不存在: %INPUT_PATH%
    pause
    exit /b
)

echo 🔄 清理远程缓存...
modal volume rm svd-cache /input.png
modal volume rm svd-cache /video/output.mp4

echo 📤 上传输入文件到远程 Volume...
modal volume put svd-cache "%INPUT_PATH%" /input.png

echo 🚀 运行 Modal 脚本生成视频...
modal run scripts\generate_video_modal.py

echo 📥 下载生成的视频文件...
modal volume get svd-cache /video/output.mp4 "%OUTPUT_VIDEO%" --force

if not exist "%OUTPUT_VIDEO%" (
    echo ❌ 视频下载失败，文件不存在: %OUTPUT_VIDEO%
    pause
    exit /b
)

echo 📥 下载生成的帧图像目录...
modal volume get svd-cache /frames "%OUTPUT_FRAMES%" --force

echo ✅ 所有步骤完成！



