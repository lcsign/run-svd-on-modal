from modal import App, Volume, Image
from diffusers import StableVideoDiffusionPipeline
import torch
from pathlib import Path
import imageio
from PIL import Image as PILImage
import sys

# ---------- 镜像与缓存 ----------
image = Image.debian_slim().pip_install(
    "diffusers",
    "torch",
    "transformers",
    "imageio",
    "imageio-ffmpeg",
    "Pillow",
    "accelerate"
)

app = App("svd-img2vid")
volume = Volume.from_name("svd-cache", create_if_missing=True)

# ---------- Volume 挂载路径 ----------
VOLUME_ROOT = Path("/input")
OUTPUT_FRAMES_DIR = VOLUME_ROOT / "frames"
OUTPUT_VIDEO_DIR = VOLUME_ROOT / "video"
MODEL_CACHE_DIR = VOLUME_ROOT / "model_cache"  # 单独的模型缓存目录

def ensure_dirs():
    OUTPUT_FRAMES_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_VIDEO_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_CACHE_DIR.mkdir(parents=True, exist_ok=True)

def save_frames(frames, base_name="frame"):
    ensure_dirs()
    for idx, frame in enumerate(frames):
        frame_path = OUTPUT_FRAMES_DIR / f"{base_name}_{idx:03d}.png"
        frame.save(frame_path)
    print(f"🖼️ 帧已保存至 Volume 中的 {OUTPUT_FRAMES_DIR}")

def save_video(frames, output_path=None, fps=5):
    ensure_dirs()
    if output_path is None:
        output_path = OUTPUT_VIDEO_DIR / "output.mp4"
    imgs = [frame.convert("RGB") for frame in frames]
    imageio.mimsave(str(output_path), imgs, fps=fps)
    print(f"🎥 视频已保存至 Volume 中的 {output_path}")

def resolve_image_path(image_path: str | None) -> str:
    return str(Path(image_path or "/input/input.png"))

def load_image_pil(path_str: str) -> PILImage.Image:
    img = PILImage.open(path_str).convert("RGB")
    # 固定分辨率到官方推荐值 1024×576
    return img.resize((1024, 576), PILImage.BICUBIC)

# ---------- 单批次生成 ----------
@app.function(
    gpu="any",
    image=image,
    volumes={"/input": volume},
    timeout=600
)
def generate_video(
    image_path: str = "/input/input.png",
    total_frames: int = 50,
    fps: int = 10
):
    resolved = resolve_image_path(image_path)
    print(f"🎬 正在生成视频，输入图像路径: {resolved}")

    input_image = load_image_pil(resolved)

    pipe = StableVideoDiffusionPipeline.from_pretrained(
        "stabilityai/stable-video-diffusion-img2vid-xt",
        torch_dtype=torch.float16,
        variant="fp16",
        cache_dir=str(MODEL_CACHE_DIR)
    )
    pipe.enable_model_cpu_offload()
    pipe.enable_attention_slicing()

    # 一次性生成全部帧
    out = pipe(
        input_image,
        num_frames=total_frames,
        num_inference_steps=30,  # 增加步数，细节更丰富
        decode_chunk_size=4      # 分块解码，防爆显存
    )
    frames = out.frames[0]

    base_name = Path(resolved).stem
    save_frames(frames, base_name=base_name)
    save_video(frames, OUTPUT_VIDEO_DIR / f"{base_name}.mp4", fps=fps)

    print(f"✅ 已生成 {len(frames)} 帧，视频输出路径为 /input/video/{base_name}.mp4")

# ---------- 本地入口 ----------
if __name__ == "__main__":
    image_arg = sys.argv[1] if len(sys.argv) > 1 else None
    app.functions.generate_video.call(image_path=image_arg or "/input/input.png")

    print("🎉 远程视频生成完成，帧 & 视频已保存到 Volume svd-cache。")
    print("👉 若要下载：")
    print("   modal volume get svd-cache /video  D:/svd_output/video")
    print("   modal volume get svd-cache /frames D:/svd_output/frames")















