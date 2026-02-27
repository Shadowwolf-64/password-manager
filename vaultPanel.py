import customtkinter as ctk
from PIL import Image
from accountsPanel import Account, accounts, accountsPanel
import random
import string



"""
This file is code for the main panel. (Vault)
"""
logoImage = None
class AccountRow():
    def __init__(self, parent, data):
        self.data = data

        # creates frame
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="x", pady=5)

        # creates label ahowing url
        self.label = ctk.CTkLabel(self.frame, text="URL: " + data.website)
        self.label.pack(side="left", padx=10)

        # creates a button to open account
        self.button = ctk.CTkButton(self.frame, text="View", command=self.viewAccountInfo)
        self.button.pack(side="right", padx=10)
    
    def viewAccountInfo(self):
        accountsPanel()



def mainPanel():
    ctk.set_appearance_mode("system") # "light" or "system" or "dark"
    ctk.set_default_color_theme("blue") # or "green", "dark-blue"

    def buttonCallback():
        print("button clicked")

    app = ctk.CTk() 
    app.title("Password Vault") 
    app.geometry("750x520") 
    app.resizable(True, True)
    passwordVar = ctk.StringVar() # variable for checking password strength
    
     # Add accounts function to collect user input and store it
    def addAccount():
        website = entryWebUrl.get()
        username = entryUsername.get()
        password = entryPassword.get()

        newAcc = Account(website, username, password) 
        accounts.append(newAcc)
        AccountRow(panelLeft, newAcc)
        print("new account added")
        for acc in accounts:
            print(acc)



    # Password strength checker
    def passwordStrength(pw: str) -> int:
        score = 0 
        
        if len(pw) >= 8:
            score += 25 
        if any(c.islower() for c in pw):
            score += 15 
        if any(c.isupper() for c in pw):
            score += 15 
        if any(c.isdigit() for c in pw): 
            score += 20 
        if any(not c.isalnum() for c in pw): 
            score += 25 
        
        return min(score, 100) 
    
    def onPasswordChange(*args):
        pw = passwordVar.get()

        if pw == "": # Does not work but is an attempt to make placeholder text work with the strength checker logic.
            progressBar.set(0)
            progressBar.configure(progress_color="red")
            progressLabel.configure(text="") 
            return
        
        score = passwordStrength(pw)
        progressBar.set(score / 100)

        if score < 40: 
            progressBar.configure(progress_color="red")
            progressLabel.configure(text="Password strength: Weak")

        elif score < 70: 
            progressBar.configure(progress_color="orange") 
            progressLabel.configure(text="Password strength: Medium")
        else:
            progressBar.configure(progress_color="green")
            progressLabel.configure(text="Password strength: Strong")
    
    
    def passwordGenerator(length=20):
        chars = string.ascii_letters + string.digits + string.punctuation 
        pw = "".join(random.choice(chars) for _ in range(length))

        entryPassword.delete(0, "end") 
        entryPassword.insert(0, pw) 
        # Update the StringVar so your strength bar updates 
        passwordVar.set(pw)


    # Right panel
    panelRight = ctk.CTkFrame(master=app, width=220, corner_radius=8, fg_color="#2b2b2b") 
    panelRight.pack(side="right", fill="y", padx=12, pady=12)

    # Images #
    global logoImage
    logoImage = ctk.CTkImage(light_image=Image.open('images/logoNoBg.png'), 
                             dark_image=Image.open('images/logoNoBg.png'),
                             size=(200, 100))

    logoLabel = ctk.CTkLabel(panelRight, text="", image=logoImage)
    logoLabel.pack(pady=1)
    
    ctk.CTkLabel(panelRight, text="Add new account password", anchor="n").pack(pady=(10,4))

    # Inner frame centered inside the panel to stack widgets #
    inner = ctk.CTkFrame(panelRight, fg_color="grey") 
    inner.pack(expand=True) # centers the inner frame vertically/horizontally
    
    # inputs #
    ctk.CTkLabel(inner, text="Website URL:", anchor="e").pack(pady=(0,4))
    entryWebUrl = ctk.CTkEntry(inner, width=200, placeholder_text="Website URL")
    entryWebUrl.pack(pady=(0, 12))
    ctk.CTkLabel(inner, text="Username:", anchor="w").pack(pady=(0,4))
    entryUsername = ctk.CTkEntry(inner, width=200, placeholder_text="Username")
    entryUsername.pack(pady=(0, 10))
    ctk.CTkLabel(inner, text="Password:", anchor="w").pack(pady=(0,4))
    entryPassword = ctk.CTkEntry(inner, textvariable= passwordVar, width=200, placeholder_text="Password", show="*")
    entryPassword.pack(pady=(0, 0))
    
    # Password gui progressbar
    passwordVar.trace_add("write", onPasswordChange)
    progressBar = ctk.CTkProgressBar(inner, width=200)
    progressBar.pack()
    progressBar.set(0)

    # proggessbar label
    progressLabel = ctk.CTkLabel(inner, text="")
    progressLabel.pack()

    #button
    genButton = ctk.CTkButton(inner, text="Generate Random Password",command=passwordGenerator , fg_color="#0066ff", hover_color="#3385ff")
    genButton.pack()
    button = ctk.CTkButton(inner, text="Add account", command=addAccount, fg_color="#0066ff", hover_color="#3385ff")
    button.pack(padx=20, pady=20)
    # Left panel (scrollable)
    panelLeft = ctk.CTkScrollableFrame(master=app, width=420, corner_radius=8, fg_color="#2b2b2b", label_text="Accounts") 
    panelLeft.pack(side="left", fill="y", padx=12, pady=12)

    # Name of the screen the user is on
    #ctk.CTkLabel(panelLeft, text="Password Vault", anchor="nw", font=("Berlin Sans FB", 26)).pack(pady=(10,4))

    #checkboxes
    #def checkbox_event():
    #    print("checkbox toggled, current value:", check_var.get())

    #check_var = ctk.StringVar(value="off")
    #checkbox = ctk.CTkCheckBox(panelLeft, text="Web URL: https://customtkinter.tomschimansky.com/documentation/widgets/checkbox", command=checkbox_event,
    #                                 variable=check_var, onvalue="on", offvalue="off")
    #checkbox.pack(padx=5, pady=5)




        


    # delete checked boxes button and function
    def deleteChecked():
        print("Deleted all checked items")

    #button
   # button = ctk.CTkButton(panelLeft, text="Remove stored password", command=deleteChecked, fg_color="#0066ff", hover_color="#3385ff")
    #button.pack(padx=20, pady=20)
    
    app.mainloop()

