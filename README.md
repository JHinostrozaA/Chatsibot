# Proyecto Chatbot Bob Esponja

## Descripción  
Este proyecto consiste en un chatbot que responde preguntas basándose en el contenido de un documento PDF que analiza la caricatura de Bob Esponja y los valores que transmite. El chatbot utiliza técnicas de procesamiento de lenguaje natural para entender preguntas y buscar respuestas en el texto vectorizado del PDF.

---

## Herramientas utilizadas

- **Python 3.13**: Lenguaje principal para desarrollar el script de vectorización y el chatbot.  
- **PyPDF2**: Para extraer texto del archivo PDF.  
- **sentence-transformers**: Para generar vectores (embeddings) a partir del texto.  
- **FAISS**: Para realizar búsquedas rápidas de similitud en vectores.  
- **Ollama**: Plataforma para ejecutar localmente un modelo de lenguaje ligero que genera las respuestas del chatbot.  
- **GitHub y GitHub Desktop**: Para control de versiones y gestión del proyecto.  
- **Cursor**: Editor de código usado para programar los scripts.

---

## Cómo ejecute el proyecto

1. Clone el repositorio o descargar el proyecto localmente.  
2. Me asegure de tener instalado Python 3.13 o superior.  
3. Instalar las dependencias necesarias ejecutando en la terminal:

   ```bash
   pip install PyPDF2 sentence-transformers faiss-cpu
Colocar el archivo PDF con el análisis de Bob Esponja en la carpeta docs/.

Ejecutar el script para vectorizar el PDF:

bash
Copiar
Editar
python vectorizar.py
Ejecutar el chatbot para realizar preguntas:

bash
Copiar
Editar
python chatbot.py
Escribir preguntas relacionadas con el contenido del PDF. Para salir, escribir salir.

**Proceso realizado y aprendizajes**
Durante el desarrollo del proyecto, aprendí a extraer y procesar texto desde un PDF, a transformar textos en vectores mediante modelos preentrenados y a implementar búsquedas semánticas rápidas con FAISS. También integré un modelo de lenguaje local para generar respuestas a partir de los fragmentos de texto más relevantes.

Este proyecto reforzó mis conocimientos en procesamiento de lenguaje natural, manejo de librerías de Python y gestión de proyectos con GitHub.

**Dificultades encontradas**
Algunas dificultades técnicas y de aprendizaje fueron:

Limitaciones de memoria RAM para ejecutar modelos de lenguaje locales, lo que afectó en ocasiones la calidad o consistencia de las respuestas del chatbot.

La programación y depuración de scripts fue un reto debido a mi experiencia limitada, por lo que utilicé inteligencia artificial para apoyo en la generación y corrección del código.

Ajustar el prompt para que el chatbot responda siempre en base al documento y no rechace preguntas fue un proceso iterativo.

Manejo de rutas y archivos en Windows generó algunos inconvenientes al principio.

A pesar de estos retos, el chatbot funciona correctamente y responde a la mayoría de las preguntas sobre el contenido del PDF.
