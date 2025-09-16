import gradio as gr
from utils.automation import process_url, process_local_dir

def url_mode(page_url):
    try:
        csv_path = process_url(page_url, out_csv="url_results.csv")
        return "✅ Successfully processed images from URL.", csv_path
    except Exception as e:
        out_csv = "url_results.csv"
        with open(out_csv, "w", encoding="utf-8") as f:
            f.write("error\n")
            f.write(str(e) + "\n")
        return f"⚠️ Oops! Something went wrong while fetching images.\nDetails: {str(e)}", out_csv

def local_mode(dir_path):
    try:
        csv_path = process_local_dir(dir_path, out_csv="local_results.csv")
        return "✅ Successfully processed local images.", csv_path
    except Exception as e:
        out_csv = "local_results.csv"
        with open(out_csv, "w", encoding="utf-8") as f:
            f.write("error\n")
            f.write(str(e) + "\n")
        return f"⚠️ Oops! Something went wrong while processing local images.\nDetails: {str(e)}", out_csv


# --- URL interface ---
url_iface = gr.Interface(
    fn=url_mode,
    inputs=gr.Textbox(label="Web page URL", placeholder="https://example.com/page-with-images"),
    outputs=[
        gr.Textbox(label="Status / Errors", interactive=False),
        gr.File(label="Download CSV")
    ],
    title="Process images from URL",
    description="Enter a web page URL. The app will scrape images, run caption+classification, and return a CSV."
)

# --- Local interface ---
local_iface = gr.Interface(
    fn=local_mode,
    inputs=gr.Textbox(label="Local directory path", placeholder=r"C:\path\to\images"),
    outputs=[
        gr.Textbox(label="Status / Errors", interactive=False),
        gr.File(label="Download CSV")
    ],
    title="Process images from local folder",
    description="Enter a local directory path containing images; the app will process JPG/PNG/BMP files."
)

# --- Tabbed interface ---
automation_demo = gr.TabbedInterface([url_iface, local_iface], ["From URL", "From Local Dir"])
