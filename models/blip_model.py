# models/blip_model.py
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# load processor + model once
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):
    """
    Takes a PIL Image and returns a caption string
    """
    inputs = processor(images=image, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption
