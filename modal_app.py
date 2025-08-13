import modal

from src.svd_runner.infer import run_inference

stub = modal.Stub("svd-runner")
image = modal.Image.debian_slim().pip_install_from_requirements("requirements.txt")

@stub.function(image=image, gpu="A10G", timeout=300)
def modal_entry(input_data: str):
    return run_inference(input_data)
