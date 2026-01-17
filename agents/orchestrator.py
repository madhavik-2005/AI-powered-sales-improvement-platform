from agents.transcript_analyzer import TranscriptAnalyzerAgent
from agents.sales_coach import SalesCoachAgent
from agents.objection_expert import ObjectionExpertAgent

class AgentOrchestrator:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.transcript_agent = TranscriptAnalyzerAgent()
        self.sales_agent = SalesCoachAgent()
        self.objection_agent = ObjectionExpertAgent()

    def analyze_call(self, transcript: str):
        docs = self.vector_store.similarity_search(transcript, k=3)
        context = "\n".join([d.page_content for d in docs])

        return {
            "call_summary": self.transcript_agent.run(transcript, context),
            "sales_feedback": self.sales_agent.run(transcript, context),
            "objections": self.objection_agent.run(transcript, context)
        }
