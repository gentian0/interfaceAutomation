from langchain.chains.llm import LLMChain
from langchain.chains.question_answering.map_reduce_prompt import messages
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate

from common.langChain_init import *

model  = ollama_chat_init("qwen3:14b")

# 提示词模版
messages  = ChatPromptTemplate.from_messages(
    SystemMessage("你是一个翻译各种语言的助手"),
    HumanMessagePromptTemplate.from_template("把 {poetry} 的原文诗翻译为英文")
)

chain = messages | model  | StrOutputParser
prompt_val = chain.invoke({"poetry": "静夜思"})
print(prompt_val)