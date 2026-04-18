import json
import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range( random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_site():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except:
        messagebox.showerror(title="Error page",message="No Data File Found")
    else:
        if website_input.get().capitalize() in data:
            email_found = data[website_input.get().capitalize()]["email"]
            passowrd_found = data[website_input.get().capitalize()]["password"]
            messagebox.showinfo(title=f"{website_input.get().capitalize()} details :",message=f"Email: {email_found}\nPassword:{passowrd_found}")
        else:
            messagebox.showinfo(title="Search details",message=f"No details for the {website_input.get()} exists")



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")
window.config(bg="white")

def validate_field(value):
    return len(value) > 0

def save_password():
    webiste_name = website_input.get().capitalize()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        webiste_name:{
            "email":email,
            "password":password
        }
    }

    if not validate_field(webiste_name) or not validate_field(email) or  not validate_field(password):
        messagebox.showerror(title="Missing information",message="Please enter all relevant infomration: ")
    else:
        try:
            with open("data.json","r") as file:
                data = json.load(file)
        except:
            print("File not found.. will create new ")
            with open("data.json","w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)


canvas = Canvas(width=200, height= 200)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= image)
canvas.config(bg= "white", highlightthickness=0)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.config(bg= "white", highlightthickness=0)
website_label.grid(row=1, column=0)

website_input = Entry()
website_input.grid(row=1, column=1)
website_input.focus()
website_input.config(width=21)

website_search_button = Button(text="Search")
website_search_button.config(bg= "white", highlightthickness=0,width=15,command=search_site)
website_search_button.grid(row=1, column=2)

email_username_label = Label(text="Email/Username:")
email_username_label.config(bg= "white", highlightthickness=0)
email_username_label.grid(row=2, column=0)

email_input = Entry()
email_input.insert(0,"hpaks23@gmail.com")
email_input.config(width=50)
email_input.grid(row=2,column=1,columnspan=2)

password_label = Label(text="Password:")
password_label.config(bg= "white", highlightthickness=0)
password_label.grid(row=3, column=0)

password_input = Entry()
password_input.config(width=25)
password_input.grid(row=3, column=1,columnspan=1)

password_generate_button = Button(text="Generate Password")
password_generate_button.config(bg= "white", highlightthickness=0,width=20,command=generate_password)
password_generate_button.grid(row=3, column=2,columnspan=1)

add_button = Button(text="Add", width=43)
add_button.config(bg= "white", highlightthickness=0,command=save_password)
add_button.grid(row=4, column=1,columnspan=2)



window.mainloop()