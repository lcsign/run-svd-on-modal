import os
from huggingface_hub import snapshot_download
from dotenv import load_dotenv

import os
from huggingface_hub import snapshot_download
from dotenv import load_dotenv

load_dotenv()  # 显式加载 .env 文件

def download_model():
    model_repo = os.getenv("HF_REPO")
    model_dir = os.getenv("MODEL_DIR", "D:/svd_runner/assets")  # 路径建议无空格

    # 触发下载（含缓存检测）
    local_path = snapshot_download(
        repo_id=model_repo,
        cache_dir=model_dir,
        local_dir=model_dir,
        resume_download=True,
        local_dir_use_symlinks=False
    )

    # 可选：打印落地路径
    print("[Model] Saved to:", local_path)

    return local_path  # 更准确：返回具体模型所在路径

