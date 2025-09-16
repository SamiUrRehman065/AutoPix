from interfaces.caption_interface import caption_demo
from interfaces.classifier_interface import classifier_demo
import gradio as gr

demo = gr.TabbedInterface(
    [caption_demo, classifier_demo],
    ["BLIP Captioning", "ResNet Classification"]
)
demo.launch(server_name="127.0.0.1", server_port=7860)
