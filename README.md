# Projeto IA com LangChain & FastAPI

## Português 🇧🇷

API REST pronta para rodar localmente (Linux/Windows), que consulta modelos LLM (OpenAI ou Azure OpenAI) e retorna a resposta ao usuário, utilizando também busca semântica em banco vetorial (FAISS). Pronto para deploy serverless (AWS Lambda)!

### Como rodar localmente

1. **Clone o projeto**
    ```bash
    git clone https://github.com/SEU_USUARIO/projeto_ia_langchain.git
    cd projeto_ia_langchain
    ```

2. **Crie e ative um ambiente virtual**

    Linux/macOS:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    Windows:
    ```bat
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure suas chaves de API**
    - Copie o arquivo `.env.example` para `.env` e preencha com suas chaves OpenAI ou Azure.

    ```bash
    cp .env.example .env
    ```

5. **Rode a API local**
    ```bash
    uvicorn app.main:app --reload
    ```

    Acesse [http://localhost:8000/docs](http://localhost:8000/docs) para testar a API interativamente.

---

## English 🇬🇧

Ready-to-use REST API (Linux/Windows), that queries LLM models (OpenAI or Azure OpenAI) and returns responses to the user, also using semantic search with FAISS vector database. Ready for serverless deployment (AWS Lambda)!

### How to run locally

1. **Clone the repository**
    ```bash
    git clone https://github.com/YOUR_USER/projeto_ia_langchain.git
    cd projeto_ia_langchain
    ```

2. **Create and activate a virtual environment**

    Linux/macOS:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    Windows:
    ```bat
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set your API keys**
    - Copy `.env.example` to `.env` and fill in your OpenAI or Azure keys.

    ```bash
    cp .env.example .env
    ```

5. **Run the API locally**
    ```bash
    uvicorn app.main:app --reload
    ```

    Access [http://localhost:8000/docs](http://localhost:8000/docs) for interactive API testing.

---

## Español 🇪🇸

API REST lista para ejecutarse localmente (Linux/Windows), que consulta modelos LLM (OpenAI o Azure OpenAI) y devuelve respuestas al usuario, utilizando también búsqueda semántica con base de datos vectorial FAISS. ¡Lista para despliegue serverless (AWS Lambda)!

### Cómo ejecutar localmente

1. **Clona el repositorio**
    ```bash
    git clone https://github.com/TU_USUARIO/projeto_ia_langchain.git
    cd projeto_ia_langchain
    ```

2. **Crea y activa un entorno virtual**

    Linux/macOS:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    Windows:
    ```bat
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Instala las dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configura tus claves de API**
    - Copia `.env.example` a `.env` y completa tus claves de OpenAI o Azure.

    ```bash
    cp .env.example .env
    ```

5. **Ejecuta la API local**
    ```bash
    uvicorn app.main:app --reload
    ```

    Accede a [http://localhost:8000/docs](http://localhost:8000/docs) para probar la API de forma interactiva.

---

## Explicação para iniciantes / Beginner's explanation / Explicación para principiantes

- **FastAPI**: Framework moderno para criar APIs REST rápidas.
- **LangChain**: Orquestrador para usar LLMs (GPT) e bancos vetoriais juntos.
- **FAISS**: Base de dados vetorial local e gratuita para busca semântica.
- **.env**: Armazena suas chaves de API de forma segura.
- **Mangum**: Adapta FastAPI para rodar em AWS Lambda.

---

## Personalização / Customization / Personalización

- Troque a lista de `DOCUMENTOS` em `app/vector_db.py` por seus próprios textos para busca semântica personalizada.
- Ajuste o provedor de LLM (OpenAI ou Azure) conforme desejado em `.env`.

---

Projeto feito para ser simples, didático e funcional.  
Any questions or improvements, please open an issue!  
Cualquier duda o mejora, abre un issue.
