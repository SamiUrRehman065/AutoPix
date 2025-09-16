import gradio as gr
from models.resnet_model import classify_image

def classify(image):
    try:
        return classify_image(image)
    except Exception as e:
        return f"Error: {str(e)}"

classifier_demo = gr.Interface(
    fn=classify,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3),
    title="Image Classification with ResNet",
    description="Upload an image to classify."
)
