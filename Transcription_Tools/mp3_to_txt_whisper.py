from whisper.utils import get_writer
import whisper
import glob
import os
import torch

model = whisper.load_model("base", device="cuda")
current_files = glob.glob("reuters/mp3s/*")

print(torch.cuda.is_available())
#https://stackoverflow.com/questions/60010487/python-glob-path-issue
# Mix was bothering me.
current_files = [os.path.normpath(i) for i in current_files]
print(len(current_files))
for audio in current_files:
  print("Attempting to transcribe:", audio)
  PATH = "reuters/finished_trans" + audio[audio.rfind('\\'):-3].replace("\\", "/") + "txt"
  if not(os.path.isfile(PATH)):
    result = model.transcribe(audio, verbose=False)
    with open(PATH, "x") as txt:
      txt.write(result["text"])
  else:
    print("SKIPPING", PATH)
    continue