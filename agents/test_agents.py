from langchain_community.llms import FakeListLLM
from langchain_community.chat_models import BedrockChat
import os

def get_llm():
    use_fallback = os.getenv("USE_FALLBACK", "true").lower() == "true"

    if use_fallback:
        return FakeListLLM(responses=[
            "The customer showed interest but raised pricing concerns.",
            "The sales representative performed well but should address objections earlier.",
            "A pricing objection was identified; recommend ROI-based follow-up."
        ])

    return BedrockChat(
        model_id="anthropic.claude-3-haiku-20240307-v1:0",
        region_name="us-east-1",
        model_kwargs={
            "temperature": 0.3,
            "max_tokens": 500
        }
    )
