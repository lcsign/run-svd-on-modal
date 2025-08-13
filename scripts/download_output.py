from modal import Volume

volume = Volume.from_name("svd-cache", create_if_missing=False)
volume.download("D:/svd_output")  # 或其他本地路径
