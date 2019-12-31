# import system function
import os
# import user dump
import json

# list all scoreboard
def listall():
    print("This is the command: ")
    with open("commands/listallcommand.cmds", 'r') as f_obj:
        cmd = f_obj.read()
        print(cmd)
# create scoreboard
def createsb():
    print("We will help you to create a scoreboard.")
    sbname = input("First, Enter your scoreboard's name(Not display name.Just your management name.): ")
    sbdisplayname = input("Next, Enter your scoreboard's display name: ")
    print("Choose the type: ")
    print("1. Dummy")
    print("2. Trigger")
    print("3. Death Count")
    print("4. playerKillCount")
    print("5. totalKillCount")
    print("6. Health")
    print("7. XP")
    print("8. XP Level")
    print("9. food")
    print("10. air")
    print("11. armor")
    print("Here is the instruction.")
    print("Dummy: Points can only be modified with commands, and are usually used to store scores, currencies, and more.")
    print("Trigger: Points can only be modified with commands, and are usually used to store scores, currencies, and more. Unlike the dummy, the administrator can control the switch that allows the score to be modified through the / trigger command.")
    print("deathCount: Points will be automatically increased when killed.")
    print("playerKillCount: When you defeat other players, you will automatically increase the score.")
    print("totalKillCount: Points are automatically increased when defeating creatures (including animals and monsters).")
    print("Health: The current health value, half a heart represents 1 point (the value is 0 before the first update of the health value).")
    print("XP: The current experience value.")
    print("XP Level: current level.")
    print("food: Current saturation (this value was 0 before the first health update).")
    print("air: The remaining air in the current dive is consistent with Air in NBT.")
    print("armor: Current armor value (this value was 0 before the armor value was first updated).")
    types = input("Option(1-11): ")
    print("Don't forget to display it!")
    if types == "1":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname +  " dummy " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "2":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname +  " trigger " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "3":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " deathCount "+ sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "4":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " playerKillCount " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "5":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " totalKillCount " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "6":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " health " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "7":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " xp " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "8":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " level " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "9":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " food " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "10":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " air " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "11":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " armor " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    else:
        print("We cannot reach the command!")
# show scoreboard
def displaysb():
    sbname = input("Enter the scoreboard name(Not display name, Leave blank to clear the selected display): ")
    print("Where do you want to put it?")
    print("1. Shown after TAB key player name")
    print("2. Show on the right side of the screen")
    print("3. Shown under player name (visible in multiplayer mode)")
    opt = input("Select some where(1-3): ")
    if opt == "1":
        print("Converting...")
        currentcmd = "/scoreboard objectives setdisplay list " + sbname
        print("We are done! The command is " + currentcmd)
    if opt == "2":
        print("Converting...")
        currentcmd = "/scoreboard objectives setdisplay sidebar " + sbname
        print("We are done! The command is " + currentcmd)
    if opt == "3":
        print("Converting...")
        currentcmd = "/scoreboard objectives setdisplay belowName " + sbname
        print("We are done! The command is " + currentcmd)


# user run
print("Adjust you can execute commands: ")
print("1. List all exist scoreboards")
print("2. Create a scoreboard")
print("3. Display a scoreboard")

options = input("Option Number: ")

# judge options
if options == "1":
    listall()
if options == "2":
    createsb()
if options == "3":
    displaysb()
