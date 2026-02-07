from fastapi import FastAPI, UploadFile, File
import shutil, os, cv2
import numpy as np
from PIL import Image

from utils.preprocess import transform
from utils.heatmap import generate_heatmap
from inference.xray_infer import analyze_xray
from pacs.pacs_schema import build_pacs_json

app = FastAPI(title="X-Ray Demo Analysis (PACS Ready)")

@app.post("/analyze/xray")
async def analyze(file: UploadFile = File(...), patient_id: str = "ANON_DEMO"):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    img = Image.open(temp_path).convert("L")
    tensor = transform(img)

    analysis = analyze_xray(tensor)

    heatmap = generate_heatmap(np.array(img))
    heatmap_path = f"outputs/heatmaps/{file.filename}_heatmap.png"
    cv2.imwrite(heatmap_path, heatmap)

    os.remove(temp_path)

    return build_pacs_json(patient_id, analysis, heatmap_path)
