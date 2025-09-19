def intro():
    print("You wake up in a dark forest. You can go left, right, or forward.")
    choice = input("Which direction do you choose? (left/right/forward): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "forward":
        center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")

def center_path():
    print("You find a small \"desire trail\" which has cleared a path from frequent use. You follow the path through
          twisting hills and you start to see stone pylons as trail markers. You continue following it back until you
          reach a monsatic temple. The monks there greet you kindly, and offer to help you return to society, after a warm meal.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("The squirrel reveals himself to be a powerful nature spirit who protects these lands from evil. As you
          accept the spirit's challenge, the very forest around you begins to quake in anticipation. The battle ensues,
          and although the spirit is powerful, you are ruthless, cunning in your swift execution of this spirit. As you
          absorb the power of the spirit, your own powers expand, granting you control over the natural world. You take
          your new powers back to your evil sanctum, where you use your newfound abilities to enforce your iron grip
          on society and the world around you.")

if __name__ == "__main__":
    intro()
