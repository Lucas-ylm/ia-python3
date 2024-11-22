import requests
import os
import PyPDF2
import re
from requests.auth import HTTPBasicAuth

# IMPORT DU FICHIER ENV DEPUIS LE CLOUD PUBLIC

def download_pdf_from_url(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Fichier téléchargé avec succès: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors du téléchargement du fichier: {e}")

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                if page.extract_text():
                    text += page.extract_text() + " "
    except Exception as e:
        print(f"Erreur lors de l'extraction du texte du fichier PDF {pdf_path}: {e}")
    return text

base_url = "https://madlab.mpublicite.fr/clients/display/"

os.makedirs("pdf", exist_ok=True)

pdf_urls = [
    base_url + "weatherpdf.pdf",
]

for pdf_url in pdf_urls:
    pdf_name = pdf_url.split('/')[-1]
    local_pdf_path = os.path.join("pdf", pdf_name)

    download_pdf_from_url(pdf_url, local_pdf_path)

    pdf_text = extract_text_from_pdf(local_pdf_path)

    if pdf_text:
        pdf_text = re.sub(r'\s+', ' ', pdf_text).strip()
        sentences = re.split(r'(?<=[.!?]) +', pdf_text)
        chunks = []
        current_chunk = ""
        for sentence in sentences:
            if len(current_chunk) + len(sentence) + 1 < 1000:
                current_chunk += (sentence + " ").strip()
            else:
                chunks.append(current_chunk)
                current_chunk = sentence + " "
        if current_chunk:
            chunks.append(current_chunk)

        # Tout le contenu du pdf est intégré dans le fichier vault.txt comme ceci
        with open("vault.txt", "a", encoding="utf-8") as vault_file:
            for chunk in chunks:
                vault_file.write(chunk.strip() + "\n")
        print(f"Contenu du fichier PDF ajouté à vault.txt: {pdf_name}")
