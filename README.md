# 🖼️ AutoPix: AI-Powered Image Tools

## 📌 Overview

**AutoPix** is an AI-powered toolkit that performs:

* **Automatic image captioning** with BLIP
* **Image classification** with ResNet
* **Bulk automation** for scraping and processing images from websites or local folders

Built using **Python**, **PyTorch**, and **Gradio**, it provides a clean, tabbed web interface with CSV export support.

This project demonstrates a **modular AI app architecture**, clean separation of **models**, **interfaces**, and **utility code**, and user-friendly deployment with Gradio.

---

## ✨ Key Features

### 🖼️ Image Captioning

* Generate natural language captions for single images
* Powered by the **BLIP model**

### 🏷️ Image Classification

* Predicts object categories using **ResNet**
* Returns top label with confidence score

### 🤖 Automation (Bulk Mode)

* Process **all images from a web page URL**
* Or process **all images in a local directory**
* Saves results (image path, caption, classification, confidence) into a **downloadable CSV**
* Handles errors gently and reports them in the CSV

### 🌐 Web Interface

* Built with **Gradio TabbedInterface**
* Three main tabs:

  * BLIP Captioning
  * ResNet Classification
  * Automation (URL / Local)

---

## 🧱 Project Structure

```
AUTOPIX/
│
├── interfaces/                       # Gradio / UI interfaces
│   ├── automation_interface.py       # Interface for scraping/processing images (URL & local)
│   ├── caption_interface.py          # Interface for image captioning
│   ├── classifier_interface.py       # Interface for image classification
│
├── models/                           # ML model wrappers
│   ├── blip_model.py                 # BLIP model for image captioning
│   ├── resnet_model.py               # ResNet model for classification
│
├── utils/                            # Helper functions
│   ├── automation.py                 # Core logic for scraping & processing images
│
├── venv/                             # Virtual environment (ignored in git)
│
├── .gitignore                        # Git ignore rules
├── app.py                            # Main entry point (runs Gradio / app)
├── README.md                         # Project documentation
├── requirements.txt                  # Python dependencies

```

---

## 🧮 Module Breakdown

| Module                    | Purpose                                             |
| ------------------------- | --------------------------------------------------- |
| `blip_model.py`           | BLIP model for image captioning                     |
| `resnet_model.py`         | ResNet model for classification                     |
| `caption_interface.py`    | Gradio UI for captioning                            |
| `classifier_interface.py` | Gradio UI for classification                        |
| `automation_interface.py` | Gradio UI for automation (URL + Local → CSV export) |
| `automation.py`           | Logic for bulk image scraping and processing        |
| `app.py`                  | Launches the tabbed Gradio app                      |

---

## 🖥️ How It Works

### 🔍 Flow for Single Images

1. User uploads an image
2. Chosen model (BLIP or ResNet) runs inference
3. Caption / classification displayed in the UI

### 🔍 Flow for Automation

1. User enters **URL** or **local directory path**
2. AutoPix fetches all images
3. Each image is captioned and classified
4. A **CSV file** is generated for download
5. Errors (like 403 forbidden) are written in the CSV too, not just hidden

---

## 🖥️ Technologies Used

| Technology      | Role                             |
| --------------- | -------------------------------- |
| Python          | Backend scripting                |
| PyTorch         | Model inference                  |
| Gradio          | Web interface for AI interaction |
| Pillow          | Image processing                 |
| Transformers    | Pretrained models for captioning |
| Requests        | Web scraping for automation      |
| CSV / Tempfiles | Export & download results        |

---

## 🚀 How to Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/SamiUrRehman065/AutoPix.git
   cd AutoPix
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   & .\venv\Scripts\Activate.ps1   # Windows PowerShell
   source venv/bin/activate        # Linux/Mac
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   python app.py
   ```

5. Open the browser at the Gradio link (usually `http://127.0.0.1:7860`)

---

## ⚠️ Notes

* AutoPix uses **pretrained models** (BLIP, ResNet18).
* Works with **Python 3.10+** (tested up to 3.13).
* GPU recommended for faster processing, but CPU also supported.
* CSVs are created as **temporary files** for user download (no clutter).

---

## 🧑‍💻 Author

**Name:** Sami Ur Rehman  
**Location:** Karachi, Pakistan  
**GitHub:** [SamiUrRehman065](https://github.com/SamiUrRehman065)

---

## 🪞 Developer Reflection

### What I Learned

* How to modularize AI apps (models, interfaces, utils)
* Building a tabbed UI with Gradio
* Automating bulk image scraping & captioning/classification
* Handling errors gracefully in both UI & CSV

### Challenges

* Keeping folder structure clean as project grew
* Making automation robust against broken links / 403s
* Avoiding leftover CSV clutter

### Solutions

* Introduced `utils/automation.py` for reusable logic
* Used Python `tempfile` for on-demand CSV download
* Tabbed Gradio design keeps UI simple yet powerful

---

## 🤝 Contributing

Contributions welcome! 🎉
Feel free to open issues or submit PRs with new features, bug fixes, or improvements.

