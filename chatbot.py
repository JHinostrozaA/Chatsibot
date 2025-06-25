import faiss
import pickle
from sentence_transformers import SentenceTransformer
import subprocess

# Cargar fragmentos y el índice FAISS
with open("fragmentos.pkl", "rb") as f:
    fragmentos = pickle.load(f)

index = faiss.read_index("vector_index.faiss")

# Cargar modelo para embeddings
modelo = SentenceTransformer("all-MiniLM-L6-v2")

def buscar_fragmentos(pregunta, top_k=5):
    vector = modelo.encode([pregunta])
    D, I = index.search(vector, top_k)
    return [fragmentos[i] for i in I[0]]

def preguntar_ollama(prompt):
    proceso = subprocess.Popen(
        ["ollama", "run", "deepseek-coder:instruct"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        text=True
    )
    salida, error = proceso.communicate(input=prompt)
    if error:
        print("⚠️ Error de Ollama:", error)
    return salida.strip()

def construir_prompt(contexto, pregunta):
    if not contexto.strip():
        return "No tengo información suficiente para responder esa pregunta basándome en el documento."

    prompt = f"""
Actúa como un experto en análisis pedagógico y cultural de medios infantiles. Has leído un documento titulado "La caricatura televisiva. Un análisis de Bob Esponja y los valores que transmite".

Toda tu respuesta debe estar basada en este documento o usando inferencia lógica a partir de él. No digas nunca que no puedes responder. Si la respuesta no está textual, intenta deducirla con sentido común, como si hubieras leído todo el trabajo.

DOCUMENTO:
\"\"\"
{contexto}
\"\"\"

PREGUNTA:
{pregunta}

RESPUESTA:
"""
    return prompt

def main():
    print("🤖 Chatbot listo. Escribe una pregunta o 'salir' para terminar.")
    while True:
        pregunta = input("\nTu pregunta: ")
        if pregunta.lower().strip() == "salir":
            break
        fragmentos_rel = buscar_fragmentos(pregunta)
        contexto = "\n".join(fragmentos_rel)
        prompt = construir_prompt(contexto, pregunta)
        if prompt.startswith("No tengo información"):
            print("\nChatbot:", prompt)
            continue
        respuesta = preguntar_ollama(prompt)
        print("\nChatbot:", respuesta)

if __name__ == "__main__":
    main()
