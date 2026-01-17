from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.bedrock_llm import get_llm

class BaseAgent:
    def __init__(self, prompt_template: str):
        self.llm = get_llm()

        self.prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["input"]
        )

        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def run(self, transcript: str, context: str = "") -> str:
        combined_input = f"""
Transcript:
{transcript}

Relevant Sales Knowledge:
{context}
"""
        return self.chain.invoke({"input": combined_input})["text"]
