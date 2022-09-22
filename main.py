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

@app.get("/model/{info}")
def details(info:str, n:int=2):
    accuracy = 95.423728
    if info == 'architecture':
        return {'architecture': 'ResNet18'}
    elif info == 'dataset':
        return {'dataset url': "https://www.kaggle.com/datasets/rhammell/ships-in-satellite-imagery"}
    elif info == 'accuracy':
        formatted_accuracy = int((10**n)*accuracy)/(10**n)
        return {'accuracy': '{}%'.format(formatted_accuracy)}
    else:    
        return '{} is not available'.format(info)

