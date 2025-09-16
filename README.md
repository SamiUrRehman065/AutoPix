# 🖼️ AutoPix: AI Image Captioning & Classification

## 📌 Overview

**AutoPix** is an AI-powered image processing app that performs **automatic image captioning** and **image classification**. Built using **Python**, **PyTorch**, and **Gradio**, it provides a user-friendly web interface for testing AI models on images.

This project demonstrates modular AI design, separating **model logic**, **interface logic**, and **deployment with Gradio**.

---

## ✨ Key Features

### 🖼️ Image Captioning

* Generates descriptive captions for uploaded images
* Powered by **BLIP model**

### 🏷️ Image Classification

* Classifies images into categories using **ResNet model**
* Returns top predicted label with confidence score

### 🌐 Web Interface

* Built with **Gradio**
* Interactive UI for uploading images and getting real-time results
* Handles multiple image formats gracefully

---

## 🧱 Project Structure

```
AutoPix/
├── interfaces/
│   ├── caption_interface.py
│   └── classifier_interface.py
├── models/
│   ├── blip_model.py
│   └── resnet_model.py
├── app.py
├── requirements.txt
└── .gitignore
```

---

## 🧮 Module Breakdown

| Module                    | Purpose                                         |
| ------------------------- | ----------------------------------------------- |
| `blip_model.py`           | Core logic for image captioning using BLIP      |
| `resnet_model.py`         | Core logic for image classification with ResNet |
| `caption_interface.py`    | Gradio interface for captioning                 |
| `classifier_interface.py` | Gradio interface for classification             |
| `app.py`                  | Launches Gradio app and manages UI routing      |

---

## 🖥️ How It Works

### 🔍 Analysis Flow

1. **User uploads an image**
2. **Gradio interface sends the image to the corresponding model**
3. **Model generates caption or predicts class label**
4. **Result displayed in the Gradio interface**

---

## 🖥️ Technologies Used

| Technology   | Role                             |
| ------------ | -------------------------------- |
| Python       | Backend scripting                |
| PyTorch      | Model training and inference     |
| Gradio       | Web interface for AI interaction |
| Pillow       | Image processing                 |
| Transformers | Pretrained models for captioning |
| Requests     | HTTP requests if needed          |

---

## 🚀 How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/SamiUrRehman065/AutoPix.git
   ```
2. Navigate to the project folder:

   ```bash
   cd AutoPix
   ```
3. Activate your virtual environment:

   ```bash
   & .\venv\Scripts\Activate.ps1
   ```
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Launch the app:

   ```bash
   python app.py
   ```
6. Open the browser at the Gradio link (usually `http://127.0.0.1:7860`)

---

## ⚠️ Note

> This project uses pretrained models. To run smoothly, ensure **Python 3.13+** and **PyTorch compatible GPU/CPU** are installed.

---

## 🧑‍💻 Author

**Name:** Sami Ur Rehman
**Location:** Karachi, Pakistan
**GitHub:** [SamiUrRehman065](https://github.com/SamiUrRehman065)

---

## 🪞 Developer Reflection

### What I Learned

* Deploying AI models with Gradio
* Structuring modular code for captioning and classification
* Efficient image processing with PyTorch and Pillow

### Challenges Faced

* Managing large pretrained models
* Ensuring UI responsiveness with Gradio
* Handling different image formats

### Solutions Implemented

* Modular interfaces for captioning & classification
* Cached models for faster inference
* Clean folder structure for maintainability

---

## 🤝 Contributing

Contributions welcome!
Open issues or submit pull requests for bugs, suggestions, or improvements.
