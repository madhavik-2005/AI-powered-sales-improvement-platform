from agents.base import BaseAgent

SALES_COACH_PROMPT = """
You are a senior sales coach.

Task:
- Identify what the sales representative did well
- Suggest 1–2 improvements
- Focus on communication and discovery skills

Transcript:
{input}

Respond in bullet points.
"""


class SalesCoachAgent(BaseAgent):
    def __init__(self):
        super().__init__(SALES_COACH_PROMPT)
