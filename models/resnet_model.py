import torch
from torchvision import transforms
from PIL import Image
import requests

model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True).eval()
labels = requests.get("https://git.io/JJkYN").text.split("\n")

def classify_image(image):
    inp = transforms.ToTensor()(image).unsqueeze(0)
    with torch.no_grad():
        prediction = torch.nn.functional.softmax(model(inp)[0], dim=0)
    confidences = {labels[i]: float(prediction[i]) for i in range(1000)}
    return confidences
