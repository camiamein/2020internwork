#Case 2 

import os 
import wave
import numpy as np
import sys
import random 

sys.path.append("voicesdk/python/%i.%i" % (sys.version_info[0], sys.version_info[1]))

try:
    from voicesdk.media import SpeechSummaryEngine
    from voicesdk.media import SNRComputer
    from voicesdk.media import RT60Computer
except ImportError:
    from voicesdk_gpu.media import SpeechSummaryEngine
    from voicesdk_gpu.media import SNRComputer
    from voicesdk_gpu.media import RT60Computer



# 1. Init SpeechSummaryEngine, SNR, and rt60 

speech_summary_engine = SpeechSummaryEngine("voicesdk/init_data/media")
snr_computer = SNRComputer("voicesdk/init_data/media")
rt60_computer = RT60Computer("voicesdk/init_data/media")

ten_files = []

# create a for loop to pick 10 random files and create a 2d array to store everything 
for i in range(10): 

	file = random.choice([ x for x in os.listdir("voicesdk/examples/wav/verify") if os.path.isfile(os.path.join("voicesdk/examples/wav/verify", x))])
	wavpath = "voicesdk/examples/wav/verify/" + file


	summary = speech_summary_engine.get_speech_summary_from_file(wavpath)
	SNR = snr_computer.compute_with_file(wavpath)
	rt60 = rt60_computer.compute_with_file(wavpath)


	ten_files.append([summary.speech_signal_length,SNR,rt60])


print(ten_files)