from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class BaseAgent:
    def __init__(self, llm, prompt_template: str):
        self.prompt = PromptTemplate(
            input_variables=["input", "context"],
            template=prompt_template
        )
        self.chain = LLMChain(llm=llm, prompt=self.prompt)

    def run(self, input_text, context):
        return self.chain.run(
            input=input_text,
            context=context
        )
