import torch
from models.xray_model import XRayModel

device = "cuda" if torch.cuda.is_available() else "cpu"

model = XRayModel().to(device)
model.load_state_dict(torch.load("xray_demo_model.pth", map_location=device))
model.eval()

def analyze_xray(img_tensor):
    with torch.no_grad():
        score = torch.sigmoid(
            model(img_tensor.unsqueeze(0).to(device))
        ).item()

    return {
        "abnormality_detected": score > 0.5,
        "confidence": round(score, 3)
    }
