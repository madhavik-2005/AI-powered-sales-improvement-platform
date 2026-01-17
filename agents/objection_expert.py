from agents.base import BaseAgent

OBJECTION_EXPERT_PROMPT = """
You are a sales objection handling expert.

Task:
- Identify explicit and implicit objections
- Suggest best-practice responses
- Focus on pricing, trust, or timing objections

Transcript:
{input}

Provide actionable advice.
"""


class ObjectionExpertAgent(BaseAgent):
    def __init__(self):
        super().__init__(OBJECTION_EXPERT_PROMPT)
