# -*- coding: utf-8 -*-
"""
Usage (from project root):
  .venv\Scripts\python.exe scripts\run_local.py -i assets\video_sample.mp4
"""

import os
import sys
import site
import argparse
import traceback
from pathlib import Path



def _add_src_to_path():
    # 将 ../src 标记为站点目录，让解释器与 IDE 都能识别包
    scripts_dir = Path(__file__).resolve().parent
    src_dir = (scripts_dir / ".." / "src").resolve()
    site.addsitedir(str(src_dir))
    return src_dir


# 在导入包之前，确保 src 在路径中
SRC_DIR = _add_src_to_path()

try:
    
    from svd_runner.infer import run_inference
    from svd_runner.utils import log, get_cache_dir


except Exception:
    print("[ImportError] Failed to import svd_runner.*")
    print("sys.path:")
    for p in sys.path:
        print(" - " + str(p))
    print("Expected SRC_DIR: " + str(SRC_DIR))
    traceback.print_exc()
    raise


def parse_args():
    parser = argparse.ArgumentParser(description="Run local inference for svd_runner.")
    parser.add_argument(
        "-i", "--input",
        dest="input_path",
        default=str(Path("assets") / "video_sample.mp4"),
        help="Input file path (e.g., assets\\video_sample.mp4)."
    )
    parser.add_argument(
        "-l", "--log-result",
        action="store_true",
        help="Append the inference result to a log file under cache dir."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print extra diagnostic info."
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.verbose:
        log("SRC_DIR: {}".format(SRC_DIR))
        log("CWD: {}".format(os.getcwd()))

    input_path = Path(args.input_path).resolve()
    if not input_path.exists():
        log("Input not found: {}".format(input_path))
        sys.exit(2)

    log("Starting local inference...")
    log("Input: {}".format(input_path))

    try:
        # 仅传入必要参数，避免与自定义签名不匹配
        result = run_inference(str(input_path))
    except Exception as e:
        log("Inference failed: {}".format(e))
        traceback.print_exc()
        sys.exit(1)

    log("Inference complete. Result: {}".format(result))

    if args.log_result:
        try:
            cache_dir = get_cache_dir()
            if cache_dir:
                cache_dir = Path(cache_dir)
                cache_dir.mkdir(parents=True, exist_ok=True)
                log_file = cache_dir / "run_local.log"
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write("[Result] {}\n".format(result))
                log("Result appended to: {}".format(log_file))
            else:
                log("Cache dir not configured; skip writing log.")
        except Exception as e:
            log("Failed to write log: {}".format(e))

    # 用返回码表达成功
    sys.exit(0)


if __name__ == "__main__":
    main()



