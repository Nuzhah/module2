import subprocess

def say(text):
    subprocess.call(['say', text])

say("Hello World!")
