from tkinter import *
from PIL import Image, ImageTk
from random import choice

root = Tk()
root.title("HAND SMASH")

try:
    root.iconbitmap(r"rock-paper-scissors.ico")
except Exception as e:
    print("Icon error:", e)

root.configure(bg="purple")
root.geometry('800x250')
root.resizable(False, False)

# Resize images and convert to PhotoImage
def load_image(file_path, size):
    try:
        img = Image.open(file_path).resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading image {file_path}: {e}")
        return None

rock_user_photo = load_image("rock_user.png", (100, 100))
paper_user_photo = load_image("paper_user.png", (100, 100))
scissor_user_photo = load_image("scissors_user.png", (110, 110))
rock_comp_photo = load_image("rock_comp.png", (100, 100))
paper_comp_photo = load_image("paper_comp.png", (100, 100))
scissor_comp_photo = load_image("scissor_comp.png", (110, 110))

# Check if any image failed to load
if None in [rock_user_photo, paper_user_photo, scissor_user_photo, rock_comp_photo, paper_comp_photo, scissor_comp_photo]:
    print("One or more images failed to load. Please check file paths.")
    root.destroy()

# Inserting pictures
user_label = Label(root, image=scissor_user_photo, bg="purple")
comp_label = Label(root, image=scissor_comp_photo, bg="purple")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Score
player_score = Label(root, text=0, font=("Helvetica", 30, "bold"), bg="purple", fg="white")
comp_score = Label(root, text=0, font=("Helvetica", 30, "bold"), bg="purple", fg="white")
comp_score.grid(row=1, column=1)
player_score.grid(row=1, column=3)

# Indicators
user_indicator = Label(root, text="USER", font=("Helvetica", 12, "bold"), bg="purple", fg="white")
comp_indicator = Label(root, text="COMPUTER", font=("Helvetica", 12, "bold"), bg="purple", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# Message
msg = Label(root, font=("Helvetica", 12, "bold"), bg="purple", fg="white", text="")
msg.grid(row=3, column=2)

# Choices and update function
choices = ["rock", "paper", "scissor"]

def update_choice(user_choice):
    comp_choice = choice(choices)
    
    print(f"User choice: {user_choice}, Computer choice: {comp_choice}")

    if comp_choice == "rock":
        comp_label.configure(image=rock_comp_photo)
    elif comp_choice == "paper":
        comp_label.configure(image=paper_comp_photo)
    else:
        comp_label.configure(image=scissor_comp_photo)
        
    if user_choice == "rock":
        user_label.configure(image=rock_user_photo)
    elif user_choice == "paper":
        user_label.configure(image=paper_user_photo)
    else:
        user_label.configure(image=scissor_user_photo)
        
    determine_winner(user_choice, comp_choice)

def determine_winner(user, computer):
    print(f"Determine winner: User - {user}, Computer - {computer}")
    if user == computer:
        msg.config(text="It's a Tie!")
    elif (user == "rock" and computer == "scissor") or (user == "paper" and computer == "rock") or (user == "scissor" and computer == "paper"):
        msg.config(text="You Win!")
        player_score.config(text=int(player_score.cget("text")) + 1)
    else:
        msg.config(text="You Lose!")
        comp_score.config(text=int(comp_score.cget("text")) + 1)

# Buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white", command=lambda: update_choice("rock"), font=("Helvetica", 10, "bold"))
rock.grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#FFB22C", fg="white", command=lambda: update_choice("paper"), font=("Helvetica", 10, "bold"))
paper.grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#36C2CE", fg="white", command=lambda: update_choice("scissor"), font=("Helvetica", 10, "bold"))
scissor.grid(row=2, column=3)

root.mainloop()
