import json
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

def normalize_audio(chunk, target_dBFS=-0.1):
    """Normalize the audio chunk to the target dBFS."""
    # Calculate the difference between the target dBFS and the current chunk's dBFS
    change_in_dBFS = target_dBFS - chunk.dBFS
    
    # Apply the gain to normalize the chunk
    return chunk.apply_gain(change_in_dBFS)

def split_audio_on_silence(file_name, output_dir, silence_thresh=-50, min_silence_len=500, keep_silence=200):
    file_path = f"{input_folder}/{file_name}.aif"
    print(f"Reading {file_name}")
    
    # Load the audio file
    audio = AudioSegment.from_file(file_path, format="aiff")
    
    # Split the audio at silences
    audio_chunks = split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh, keep_silence=keep_silence)
    
    print (f"Split into {len(audio_chunks)} chunks. Got {len(sample_names)} sample names.")

    # Save each chunk to the output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, chunk in enumerate(audio_chunks):
        # Normalize each chunk to -0.1 dBFS to avoid digital clipping
        normalized_chunk = normalize_audio(chunk, target_dBFS=-0.1)
        
        if i < len(sample_names):
            chunk_filename = os.path.join(output_dir, f"{chunk_prefix}{file_name}_{sample_names[i]}.aif")
        else:
            chunk_filename = os.path.join(output_dir, f"{chunk_prefix}{file_name}_chunk{i+1}.aif")

        normalized_chunk.export(chunk_filename, format="aiff")
        print(f"Exported {chunk_filename}")

# Load the JSON configuration
with open("config.json", "r") as f:
    config = json.load(f)

# Extract the names
file_names = config["file_names"]
sample_names = config["sample_names"]
chunk_prefix = config["chunk_prefix"]
input_folder = config["input_folder"]

# Loop through the file names, assuming each corresponds to an AIF file
for file in file_names:
    input_file = f"{file}"

    file_path = f"{input_folder}/{input_file}.aif"
    if not os.path.exists(file_path):
        print(f"File {input_file}.aif does not exist. Skipping...")
        continue  # Skip to the next sample if the file is missing

    split_audio_on_silence(input_file, f"output_chunks")
