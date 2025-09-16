# interfaces/caption_interface.py
import gradio as gr
from models.blip_model import generate_caption

def caption_image(image):
    try:
        return generate_caption(image)
    except Exception as e:
        return f"Error: {str(e)}"

caption_demo = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Image Captioning with BLIP",
    description="Upload an image to generate a caption."
)
