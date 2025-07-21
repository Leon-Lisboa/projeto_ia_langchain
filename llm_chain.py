from .config import OPENAI_API_KEY, AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Para OpenAI
from langchain_openai import OpenAI as LangchainOpenAI

# Para Azure OpenAI (opcional)
from langchain_openai import AzureOpenAI

def get_llm():
    if AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_DEPLOYMENT:
        return AzureOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            deployment_name=AZURE_OPENAI_DEPLOYMENT,
            temperature=0.7,
            model="gpt-35-turbo"  # ajuste se necessário
        )
    elif OPENAI_API_KEY:
        return LangchainOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7)
    else:
        raise ValueError("Nenhuma chave de API de LLM configurada. Configure OPENAI_API_KEY ou variáveis da Azure.")

def consultar_llm(pergunta, contexto=None):
    input_text = ""
    if contexto:
        input_text += f"Contexto:\n{contexto}\n\n"
    input_text += f"Pergunta: {pergunta}\nResposta:"
    prompt = PromptTemplate(
        input_variables=["input"],
        template="{input}"
    )
    llm = get_llm()
    chain = LLMChain(llm=llm, prompt=prompt)
    resposta = chain.run(input=input_text)
    return resposta.strip()