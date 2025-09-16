# app.py
import gradio as gr
from interfaces.caption_interface import caption_demo
from interfaces.classifier_interface import classifier_demo
from interfaces.automation_interface import automation_demo

# Main Tabbed Interface (no title/description allowed directly)
demo = gr.TabbedInterface(
    [caption_demo, classifier_demo, automation_demo],
    ["BLIP Captioning", "ResNet Classification", "Automation (URL / Local)"]
)

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",  # localhost
        server_port=7860,         # change if needed
        debug=True,               # helpful for dev
        share=False               # set True if you want public Gradio link
    )
