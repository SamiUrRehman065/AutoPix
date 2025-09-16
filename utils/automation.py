import os
import glob
import csv
import requests
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup

from models.blip_model import generate_caption
from models.resnet_model import classify_image


# ----- helpers -----
def scrape_image_urls(page_url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }
    resp = requests.get(page_url, timeout=15, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    urls = []
    for img in soup.find_all("img"):
        src = img.get("src")
        if not src:
            continue
        if src.startswith("//"):
            src = "https:" + src
        if not (src.startswith("http://") or src.startswith("https://")):
            continue
        if "svg" in src or "1x1" in src:
            continue
        urls.append(src)
    return list(dict.fromkeys(urls))  # unique, keep order


def _download_image(url, timeout=12):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }
    r = requests.get(url, timeout=timeout, headers=headers)
    r.raise_for_status()
    img = Image.open(BytesIO(r.content)).convert("RGB")
    if img.width * img.height < 400:  # skip tiny icons
        raise ValueError("image too small")
    return img


def _top_label_from_dict(pred_dict):
    if not pred_dict:
        return "", 0.0
    top = max(pred_dict.items(), key=lambda x: x[1])
    return top[0], float(top[1])


def _write_csv(rows, out_csv):
    """Write results into CSV with standard header."""
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["image_url_or_path", "caption_or_error", "top_label", "top_prob"])
        writer.writerows(rows)
    return out_csv


# ----- main processors -----
def process_url(page_url, out_csv="url_results.csv"):
    rows = []
    try:
        urls = scrape_image_urls(page_url)
        if not urls:
            raise ValueError("No images found on the page.")
    except Exception as e:
        # save a CSV with just the error
        rows.append([page_url, f"⚠️ Oops! Could not scrape images. Details: {e}", "", ""])
        return _write_csv(rows, out_csv)

    for img_url in urls:
        try:
            img = _download_image(img_url)
            caption = generate_caption(img)
            classes = classify_image(img)  # dict label -> prob
            label, prob = _top_label_from_dict(classes)
            rows.append([img_url, caption, label, prob])
        except Exception as e:
            rows.append([img_url, f"⚠️ Error processing: {e}", "", ""])

    return _write_csv(rows, out_csv)


def process_local_dir(dir_path, out_csv="local_results.csv"):
    dir_path = os.path.abspath(dir_path)
    if not os.path.exists(dir_path):
        rows = [[dir_path, f"⚠️ Directory not found: {dir_path}", "", ""]]
        return _write_csv(rows, out_csv)

    exts = ("*.jpg", "*.jpeg", "*.png", "*.bmp")
    paths = []
    for e in exts:
        paths.extend(glob.glob(os.path.join(dir_path, e)))

    if not paths:
        rows = [[dir_path, f"⚠️ No images found in directory.", "", ""]]
        return _write_csv(rows, out_csv)

    rows = []
    for p in sorted(paths):
        try:
            img = Image.open(p).convert("RGB")
            caption = generate_caption(img)
            classes = classify_image(img)
            label, prob = _top_label_from_dict(classes)
            rows.append([p, caption, label, prob])
        except Exception as e:
            rows.append([p, f"⚠️ Error processing: {e}", "", ""])

    return _write_csv(rows, out_csv)
