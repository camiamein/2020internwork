# Case 1 

import os
import wave
import numpy as np
import sys

sys.path.append("voicesdk/python/%i.%i" % (sys.version_info[0], sys.version_info[1]))

try:
    from voicesdk.verify import VerifyEngine, VoiceTemplate
except ImportError:
    from voicesdk_gpu.verify import VerifyEngine, VoiceTemplate


wavpath = "voicesdk/examples/wav/verify"

# init engine 
verify_engine = VerifyEngine("voicesdk/init_data/verify/verify_init_data_16k", VerifyEngine.M_TI_X_2)


# retrieve random wav files, 2 of the same speake one different 

person1 = os.path.join(wavpath,"f001_02_001.wav" )
person1b = os.path.join(wavpath,"f001_08_001.wav" )
person2 = os.path.join(wavpath,"f002_02_001.wav" )


# make the voice templates 

temp1 = verify_engine.create_voice_template_from_file(person1)
temp1b = verify_engine.create_voice_template_from_file(person1b)
temp2 = verify_engine.create_voice_template_from_file(person2)

voicetemplates = [temp1,temp1b,temp2]

#verifying the voice templates and matching them to the same user 

matching = []
count = 0 


for i in range(len(voicetemplates)):
	for j in range(len(voicetemplates)):
		if i < j:
			count = count + 1 #tracking the number of viable matching options 

			compare_temp = verify_engine.verify(voicetemplates[i],voicetemplates[j])
			matching.append(compare_temp)

			print("match %i \n"%(count) + "comparing users %i and %i"%(i+1,j+1))

			print(compare_temp) 

			if compare_temp.probability > 0.5:  #using probability of 0.5 as suggested by documentation
				print("recordings match, most likely the same user")
			else:
				print("warning: recordings do not match, likely not the same user")

			print("-" * 20)

# checking the probabilty for the matching users is greater than different users 
	

for k in matching:
	for w in matching:
		if k.probability > w.probability: 
			print("match%i"%(matching.index(k)+1) + " has a higher probabililty of being the same user than match"+ "match%i"%(matching.index(w)+1))




# match1 = verify_engine.verify(voicetemplate1a,voicetemplate1b)
# print(match1)

# if match1.probability > 0.5: #using probability of 0.5 as suggested by documentation
# 	print("recordings match")
# else:
# 	print("warning: likely not a match")

# print("-" * 20)

# match2 = verify_engine.verify(voicetemplate1a,voicetemplate2)
# print(match2)

# if match2.probability > 0.5:
# 	print("recordings match")
# else:
# 	print("warning: likely not a match")

# print("-" * 20)

# match3 = verify_engine.verify(voicetemplate1b,voicetemplate2)
# print(match3)

# if match3.probability > 0.5:
# 	print("recordings match")
# else:
# 	print("warning: likely not a match")

# print("-"*20)



# # 
# probabilities = (match1.probability,match2.probability,match3.probability)
# print(probabilities[1])

# for i in probabilities:
# 	for j in probabilities:
# 		if i > j: 
# 			print("match%i"%(i) + " has a higher probabililty of being the same user than ")