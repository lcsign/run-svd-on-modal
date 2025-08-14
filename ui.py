import gradio as gr
import subprocess
import os

BAT_PATH = r"D:\svd_runner\scripts\start.bat"
OUTPUT_VIDEO = r"D:\svd_runner\output\output.mp4"

def run_svd_ui(input_img):
    subprocess.run([BAT_PATH, input_img, "output"], shell=True)
    return OUTPUT_VIDEO

with gr.Blocks() as demo:
    img = gr.Image(type="filepath", label="选择输入图片")
    btn = gr.Button("生成视频")
    video_out = gr.Video()
    btn.click(fn=run_svd_ui, inputs=img, outputs=video_out)

demo.launch()
