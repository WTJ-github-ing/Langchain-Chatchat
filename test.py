import torch
# 驱动 11.5
# cuda 11.4, V11.4.120
#cudnn

#pip install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio==0.10.1+cu113

# 检查CUDA是否可用
if torch.cuda.is_available():
    # 获取GPU设备数量
    device_count = torch.cuda.device_count()

    # 列出可用的GPU设备
    for i in range(device_count):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("CUDA is not available. No GPU devices found.")
