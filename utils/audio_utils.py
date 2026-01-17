from pydub import AudioSegment

def convert_mp4_to_wav(mp4_path):
    """
    Converts MP4 video file to WAV audio file
    """
    audio = AudioSegment.from_file(mp4_path, format="mp4")
    wav_path = mp4_path.replace(".mp4", ".wav")
    audio.export(wav_path, format="wav")
    return wav_path
