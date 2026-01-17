import streamlit as st
import tempfile
import uuid

from aws.s3_utils import upload_audio_to_s3
from aws.transcribe_utils import transcribe_audio
from rag.vector_store import create_vector_store
from agents.orchestrator import AgentOrchestrator

st.set_page_config(page_title="AI Sales Call Analyzer", layout="wide")

st.title("🎧 AI-Powered Sales Call Analyzer")

MAX_FILE_SIZE_MB = 5

audio_file = st.file_uploader(
    "Upload a sales call recording",
    type=["wav", "mp3", "mp4"]
)

if audio_file:
    file_size_mb = audio_file.size / (1024 * 1024)
    st.write(f"📦 File size: {file_size_mb:.2f} MB")

    if file_size_mb > MAX_FILE_SIZE_MB:
        st.error("File must be under 5MB")
        st.stop()

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(audio_file.read())
        temp_path = tmp.name

    if st.button("Analyze Call"):
        with st.spinner("Uploading audio to S3..."):
            s3_uri = upload_audio_to_s3(temp_path, audio_file.name)

        with st.spinner("Transcribing audio..."):
            job_name = f"sales-call-{uuid.uuid4()}"
            transcript, language = transcribe_audio(job_name, s3_uri)

        st.success("Transcription completed")
        st.caption(f"Detected language: {language}")

        st.subheader("📝 Transcript")
        st.text_area("Transcript", transcript, height=250)

        with st.spinner("Running AI agents..."):
            vector_store = create_vector_store("rag/knowledge_base.txt")
            orchestrator = AgentOrchestrator(vector_store)
            result = orchestrator.analyze_call(transcript)

        st.subheader("📊 AI Sales Insights")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### ✅ What went well")
            st.write(result["sales_feedback"])

        with col2:
            st.markdown("### ⚠️ Missed Opportunities / Objections")
            st.write(result["objections"])

        st.markdown("### 📌 Call Summary")
        st.write(result["call_summary"])
