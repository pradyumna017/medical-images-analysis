import torchvision.transforms as T

transform = T.Compose([
    T.Resize((224, 224)),
    T.ToTensor()
])
