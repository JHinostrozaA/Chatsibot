import PyPDF2
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Ruta al PDF nuevo
pdf_path = "docs/Bob.pdf"

def extraer_texto(path):
    texto = ""
    with open(path, "rb") as archivo:
        lector = PyPDF2.PdfReader(archivo)
        for pagina in lector.pages:
            texto += pagina.extract_text() + "\n"
    return texto

texto = extraer_texto(pdf_path)

# Dividir en fragmentos
fragmentos = texto.split(". ")
fragmentos = [frag.strip() for frag in fragmentos if frag.strip()]

# Crear vectores con modelo ligero
modelo = SentenceTransformer("all-MiniLM-L6-v2")
vectores = modelo.encode(fragmentos)

# Crear índice FAISS
dim = vectores.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(vectores)

# Guardar índice y fragmentos
faiss.write_index(index, "vector_index.faiss")
with open("fragmentos.pkl", "wb") as f:
    pickle.dump(fragmentos, f)

print("✅ ¡Texto vectorizado y guardado!")

