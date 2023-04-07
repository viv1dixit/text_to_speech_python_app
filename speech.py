# / tum jab kahoge hum tab milenge bas shart yeh hai ki ghadi na tum pehnoge na waqt hum dekhenge

import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')

# Set the voice ID
voice_id = 'com.apple.speech.synthesis.voice.samantha'  # replace with the ID of your desired voice
engine.setProperty('voice', voice_id)
# Set the voice rate (words per minute)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100) # adjust the value to change the rate

# Generate speech
engine.say("hello there what is up github?")

# Play the speech
engine.runAndWait()
