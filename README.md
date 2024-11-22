- pip install -r requirements.txt (ça n'a marché de mon côté qu'en utilisant la version 3.11 de python)
- intaller Ollama
- ollama pull llama3
- ollama pull mxbai-embed-large
- Importer les fichiers sur le filezilla de M Publicité dans le dossier "/madlab.mpublicite.fr/clients/display" (Il y a déjà un fichier pdf importé, vous n'aurez pas les accès donc vous pouvez skip cette étape.)
- python upload.py (pour upload le pdf dans vault.txt)
- python localrag.py (SANS RAG)
- python localrag.py --use_rag (AVEC RAG)

- question à poser au modèle : Tell me about extreme weather

- FYI: je voulais faire un fetch sur le dossier qui contient TOUT les pdfs mais je n'ai pas les accès nécessaires, j'ai une erreur 403 en faisant cela, il faut donc importer manuellement avec un lien direct du fichier en le précisant à la main c'est la seule manière qui fonctionne correctement.