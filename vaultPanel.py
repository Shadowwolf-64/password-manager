import customtkinter as ctk
from PIL import Image



"""
This file is code for the main panel. (Vault)
"""

def mainPanel():
    ctk.set_appearance_mode("system") # "light" or "system" or "dark"
    ctk.set_default_color_theme("blue") # or "green", "dark-blue"

    def buttonCallback():
        print("button clicked")

    app = ctk.CTk() 
    app.title("Password Vault") 
    app.geometry("750x520") 
    app.resizable(True, True)
    
    # Right panel
    panelRight = ctk.CTkFrame(master=app, width=220, corner_radius=8, fg_color="#2b2b2b") 
    panelRight.pack(side="right", fill="y", padx=12, pady=12)

    # Images #
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
    entryWebUrl = ctk.CTkEntry(inner, width=200, placeholder_text="Website URL", show="*")
    entryWebUrl.pack(pady=(0, 12))
    ctk.CTkLabel(inner, text="Username:", anchor="w").pack(pady=(0,4))
    entryUsername = ctk.CTkEntry(inner, width=200, placeholder_text="Username")
    entryUsername.pack(pady=(0, 10))
    ctk.CTkLabel(inner, text="Password:", anchor="w").pack(pady=(0,4))
    entryPassword = ctk.CTkEntry(inner, width=200, placeholder_text="Password", show="*")
    entryPassword.pack(pady=(0, 12))

    #button
    button = ctk.CTkButton(inner, text="Add account", command=buttonCallback, fg_color="#0066ff", hover_color="#3385ff")
    button.pack(padx=20, pady=20)

    # Left panel
    panelLeft = ctk.CTkFrame(master=app, width=420, corner_radius=8, fg_color="#2b2b2b") 
    panelLeft.pack(side="left", fill="y", padx=12, pady=12)

    # Name of the screen the user is on
    ctk.CTkLabel(panelLeft, text="Password Vault", anchor="nw", font=("Berlin Sans FB", 26)).pack(pady=(10,4))

    #checkboxes
    def checkbox_event():
        print("checkbox toggled, current value:", check_var.get())

    check_var = ctk.StringVar(value="off")
    checkbox = ctk.CTkCheckBox(panelLeft, text="Web URL: https://customtkinter.tomschimansky.com/documentation/widgets/checkbox", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
    checkbox.pack(padx=5, pady=5)

    # delete checked boxes button and function
    def deleteChecked():
        print("Deleted all checked items")

    #button
    button = ctk.CTkButton(panelLeft, text="Remove stored password", command=deleteChecked, fg_color="#0066ff", hover_color="#3385ff")
    button.pack(padx=20, pady=20)
    
    app.mainloop()

