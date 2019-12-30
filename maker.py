from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play
import wave
import contextlib




def create(text):

	#Say the poem and save to audio file
	targetLanguage = 'en'
	tts = gTTS(text, targetLanguage)  
	tts.save("synthesized.wav")

	#Find ffmpg, ffprobe, and ffplay
	AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"
	AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"
	AudioSegment.ffprobe ="C:\\ffmpeg\\bin\\ffprobe.exe"
	AudioSegment.ffplay ="C:\\ffmpeg\\bin\\ffplay.exe"
	audio_in_file = "synthesized.wav"
	audio_out_file = "fin.wav"

	#Create 6 secs of silence audio segment
	one_sec_segment = AudioSegment.silent(duration=6000)  #duration in milliseconds

	#read wav file to an audio segment
	print(os.path.isfile(audio_in_file))
	song = AudioSegment.from_file(audio_in_file)

	#Add above two audio segments    
	final_song = one_sec_segment + song

	#Either save modified audio
	final_song.export(audio_out_file, format="wav")


	#Combine both of them
	sound1 = AudioSegment.from_file("e.wav")
	sound2 = AudioSegment.from_file("fin.wav")
	combined = sound1.overlay(sound2)

	combined.export("final.wav", format='wav')

	#Find the pause right after the speaking is finished
	audiofile = 'fin.wav'
	length = 0
	with contextlib.closing(wave.open(audiofile,'r')) as f: 
	  frames = f.getnframes()
	  rate = f.getframerate()
	  length = frames / float(rate)    
	  
	trim = [13.309, 21.221, 27.865, 35.767, 42.837, 51.571, 58.671, 65.771, 74.029, 81.099, 89.001, 96.487, 103.142, 110.628, 118.114, 125.600, 133.086, 140.988, 148.474, 155.544, 163.031, 171.348, 178.835, 186.321, 193.807, 200.045, 208.363, 215.849, 222.919, 230.821, 240.000]

	fintrim = 1000

	for leng in trim:
		if leng > length:
			fintrim = leng
			break
	print(leng)
	
	#Trim
	song = AudioSegment.from_mp3( 'final.wav' )
	extract = song[0:fintrim*1000]

	#Save
	extract.export('final_trim.mp3', format="mp3")


test = """Roses are red,
Violets are blue,
This is a test,
Just for you."""

create(test)