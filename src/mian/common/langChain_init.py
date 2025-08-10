from langchain_ollama import ChatOllama


def ollama_chat_init(models: str):
    """ChatOllama large language models."""
    return ChatOllama(
        base_url="http://127.0.0.1:11434/",
        model=models,
        # reasoning=False,

    )


def ollama_llm_init(models: str):
    """ollamaLlm large language models."""
    return ChatOllama(
        base_url="http://127.0.0.1:11434/",
        model=models,
    )
