import torch

# 检查CUDA是否可用
if torch.cuda.is_available():
    # 获取GPU设备数量
    device_count = torch.cuda.device_count()

    # 列出可用的GPU设备
    for i in range(device_count):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("CUDA is not available. No GPU devices found.")
