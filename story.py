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
    print("As your hand grips the leather wraps on the hilt, the glow of the sword intensifies. The pommel's
          unknown insignia glows with a holy yellow light, and glowing runes appear along the flat of the blade.
          Great power courses through you, as you are given the sight and means to destroy evil wherever you may find it.
          In the coming months, you work your way through the Realm of Darkness and face off against the Nightmare
          King. It is a great battle, shadow clashing against light, but your skill and power allow you to overcome him,
          finally bringing peace to forgotten lands.")

def center_path():
    print("You find a small \"desire trail\" which has cleared a path from frequent use. You follow the path through
          twisting hills and you start to see stone pylons as trail markers. You continue following it back until you
          reach a monsatic temple. The monks there greet you kindly, and offer to help you return to society, after a warm meal.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

if __name__ == "__main__":
    intro()
