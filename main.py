from io import BytesIO
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from utils import load_device, load_model, predict, is_image_file
from PIL import Image

 
app = FastAPI()

def read_image(file):
    img = Image.open(BytesIO(file)).convert("RGB")
    return img

device = load_device()
model = load_model(device=device)


@app.get("/")
def root():
    return {"message": "Welcome to Image Classification FastAPI"}

@app.post("/predict")
async def predict_api(file: UploadFile = File(...)):
    if not is_image_file(file.filename):
        return "file must have image format"
    img = read_image(await file.read())
    preds = predict(img, model, device)
    return preds

@app.get("/model")
def details():
    model = "ResNet18"
    accuracy = "99.25%"
    training_dataset = "https://www.kaggle.com/datasets/carlosrunner/pizza-not-pizza"
    return {"Model": model, 
            "accuracy": accuracy,
            "training dataset": training_dataset}

