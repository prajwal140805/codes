from os import system
text = "hello world"
 
system('powershell -Command "Add-Type -AssemblyName System.Speech; '
f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"')      