from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

def split_audio_on_silence(aif_path, output_dir, silence_thresh=-50, min_silence_len=500, keep_silence=200):
    # Step 1: Load the AIF file
    audio = AudioSegment.from_file(aif_path, format="aiff")

    # Step 2: Detect and split the audio at silences
    audio_chunks = split_on_silence(
        audio, 
        min_silence_len=min_silence_len,  # Minimum silence length to be considered
        silence_thresh=silence_thresh,    # Silence threshold (in dB)
        keep_silence=keep_silence         # Keep a bit of silence before and after each chunk
    )
    
    # Step 3: Save each chunk as a new file
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for i, chunk in enumerate(audio_chunks):
        chunk_filename = os.path.join(output_dir, f"chunk_{i+1}.aif")
        chunk.export(chunk_filename, format="aiff")
        print(f"Exported {chunk_filename}")

# Usage:
aif_file = "Synthwave_AllNight.aif"
output_directory = "output_chunks"
split_audio_on_silence(aif_file, output_directory)
