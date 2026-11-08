# Transcribe Recordings

## Choose the route

- Use an existing transcript when it meets the request. Otherwise choose an available transcription connector or local model for the required language, accuracy, and privacy.

- For local work, inspect the recording's duration and the CPU and memory limits reported by exec. Compressed file size does not bound decoded audio or feature-extraction memory. Even an iterator that yields transcript segments can preprocess the entire recording first.

## Transcribe locally

- Use the bundled helper with an installed local CTranslate2 model, FFmpeg, and a Python environment containing NumPy and faster-whisper. It loads one model with one CPU worker and transcribes 60-second chunks with two seconds of overlapping audio on each side. It matches shared words when joining chunks and flags conflicting boundaries. It does not download models, install dependencies, or write intermediate audio files.

- Run it through muse.exec with the model directory and a new output directory under the workspace:

  ```sh
  python3 /opt/muse/assets/audio/transcribe_chunks.py \
    --input ~/workspace/recording.mp3 \
    --model ~/workspace/models/whisper-small \
    --output-dir ~/workspace/transcripts/recording \
    --language en
  ```

- Omit `--language` for automatic detection. Choose `--chunk-seconds` between 5 and 120 when needed. Start with one transcription command and measure its memory use alongside other work before adding concurrency. Chunking bounds audio processing, but the model must still fit in memory.

## Recover and verify

- After an interruption, rerun the same command and output directory. The helper reuses completed chunks, including the saved words needed to join the next chunk. It commits each checkpoint only after transcription succeeds and prevents concurrent writers to the output directory.

- After a confirmed OOM, reducing concurrent work lets you retry the same command and output directory while preserving completed chunks.

- Shortening chunks or choosing a smaller model requires a new output directory and restarts transcription from the beginning. Changing the recording or language also requires a new directory. The helper rejects incompatible checkpoints. Preserve the previous chunks and source recording.

- Treat chunk files as partial work until the helper succeeds and writes `complete.json` and `transcript.txt`. A `needs_review` result means transcription finished with disputed boundaries. Review the marked passages against the recording; the corresponding chunk files retain both readings. Do not present those passages as verified text.

- Check that the transcript covers the recording and verify uncertain names against the audio. Partial output or a successful wrapper command does not establish a complete transcript.

## Available connectors

- Use muse.connector_search to find available transcription services and muse.skill_search for related workflows. For speech generation, find Spoken Audio.
