import modal

volume = modal.Volume.from_name("your_volume_name", create_if_missing=False)
volume.download("D:/output")
