#Pass in name or identifier for tunings and output a dictionary of all
# frequencies that need to be passed to outputaudio function
def getTunings(name):
	tunings = {}
	if name == "E Standard":
		tunings[0] = 329.63  #E
		tunings[1] = 440.00  #A
		tunings[2] = 587.33  #D
		tunings[3] = 783.99  #G
		tunings[4] = 987.77  #B
		tunings[5] = 1318/51 #E
	elif name == "Drop D":
		tunings[0] = 293.66  #D
		tunings[1] = 440.00  #A
		tunings[2] = 587.33  #D
		tunings[3] = 783.99  #G
		tunings[4] = 987.77  #B
		tunings[5] = 1318.51 #E
	elif name == "Half Step Down":
		tunings[0] = 311.13  #Eb
		tunings[1] = 415.30  #Ab
		tunings[2] = 554.37  #Db
		tunings[3] = 739.99  #Gb
		tunings[4] = 932.33  #Bb
		tunings[5] = 1244.51 #Eb
	elif name == "Drop Db":
		tunings[0] = 277.18  #Db
		tunings[1] = 415.30  #Ab
		tunings[2] = 554.37  #Db
		tunings[3] = 739.99  #Gb
		tunings[4] = 932.33  #Bb
		tunings[5] = 1244.51 #Eb
	elif name == "D Standard":
		tunings[0] = 293.66  #D
		tunings[1] = 392.00  #G
		tunings[2] = 523.25  #C
		tunings[3] = 698.46  #F
		tunings[4] = 880.00  #A
		tunings[5] = 1174.66 #D
	elif name == "Drop C":
		tunings[0] = 261.63  #C
		tunings[1] = 392.00  #G
		tunings[2] = 523.25  #C
		tunings[3] = 698.46  #F
		tunings[4] = 880.00  #A
		tunings[5] = 1174.66 #D
	elif name == "C Standard":
		tunings[0] = 261.63  #C
		tunings[1] = 349.23  #F
		tunings[2] = 493.88  #B
		tunings[3] = 659.25  #E
		tunings[4] = 783.99  #G
		tunings[5] = 1046.50 #C
	return tunings

""" THIS IS HOW YOU GET TUNINGS for a tuning into a dictionary
dict = {}
dict = getTunings("C Standard")
for i in range(0,6):
	print(dict[i])
"""