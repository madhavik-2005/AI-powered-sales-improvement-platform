from agents.base import BaseAgent

TRANSCRIPT_ANALYZER_PROMPT = """
You are a sales call analyst.

Task:
- Summarize the call in 3–4 bullet points
- Identify customer intent
- Identify key concerns

Transcript:
{input}

Return a concise structured summary.
"""


class TranscriptAnalyzerAgent(BaseAgent):
    def __init__(self):
        super().__init__(TRANSCRIPT_ANALYZER_PROMPT)
