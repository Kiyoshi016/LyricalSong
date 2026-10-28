import time
import os

lyrics = [
    "And any girl like you deserves a gentleman",
    "Tell me, why are we wasting time",
    "On all your wasted cryin'",
    "When you should be with me instead?",
]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_line(line, speed):
    for character in line:
        print(character, end="", flush=True)
        time.sleep(speed)
    print()
clear_screen()

print(" Backburnerr ")
print("Shaun MARVS")
print("-" * 30)

input("Press ENTER to start... ")

speed = float(input("Choose typing speed (0.05): "))

clear_screen()

for line in lyrics:
    show_line(line, speed)
    time.sleep(1)

print(" Engg engot depinde kung 3 yan ")