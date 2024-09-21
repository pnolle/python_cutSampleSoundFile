FROM python:3

# Set working directory
WORKDIR /usr/src/app

# Install ffmpeg (for handling audio files)
RUN apt-get update && apt-get install -y ffmpeg

# Copy and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Define the command to run your script
CMD [ "python", "./cutSampleSoundFile.py" ]