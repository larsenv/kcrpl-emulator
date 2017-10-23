import platform
import random
import time

print("KcrPL Emulator\n")

tasks = ["Have any ideas why this guy is having issues?", "I'm gonna go take a shower.", "I'm going to sleep. Good night!", "Can I make a Wii emulator in Windows Batch?", "Make a support@riiconnect24.net email.", "Send me the new IOS patches please.", "I want to implement translation support in my batch script!", "Should I merge this PR?", "Help me I'm still getting 221001.", "I wanna be admin!", "Can you ban this spammer?", "Can I add more cities for Poland?"]
tag_notag = ["@Larsenv ", ""]

print("KcrPL: " + random.choice(tag_notag) + random.choice(tasks))

time.sleep(1)

response = ["Yes", "No", "OK", "Could you stop bothering me?"]

print("Larsenv: " + random.choice(response))

time.sleep(1)

response = ["👌", "👌", "👌", "👌", "👌", "👌", "👌", "👌", "👌", "👌", "👌", "👌", "👌", "👌", "👌", "👌", "/kcrplban", "/kcrplbaseball", "/kcrplclap", "/kcrplclap2", "/kcrplcry", "/kcrpldance", "/kcrpldance2", "/kcrpldance3", "/kcrpldance4", "/kcrpldance5", "/kcrplevidence", "/kcrplfacepalm", "/kcrplfuckyou", "/kcrplhaha", "/kcrplhmm", "/kcrpllarsenv", "/kcrplno", "/kcrplno2", "/kcrplshame", "/kcrplyes", "/kcrplyes2", "/kcrplyes3"]

tag = random.choice(response)

if platform.system() == "Windows":
    if tag == "👌":
        response = ["OK", ":ok_hand:"]
        tag = random.choice(response)

print("KcrPL: " + tag)

if "/" in tag:
    time.sleep(1)
    if tag == "/kcrplobjection" or tag == "/kcrplhmm" or tag == "/kcrplevidence": print("Spectra: <Phoenix Wright GIF>")
    elif tag == "/kcrplhaha": print("Spectra: <GIF>")
    else: print("Spectra: <Destiny GIF>")

time.sleep(1)
