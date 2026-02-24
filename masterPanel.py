# This file is for the master login panel of the program
import customtkinter as ctk
from PIL import Image
from vaultPanel import mainPanel

# temp login creds #
adminUser = "admin"
adminPass = "admin"

    # Button functions #
def verifyLogin(current_window, entryUsername, entryPassword):
    username = entryUsername.get()
    password = entryPassword.get()
    if username == adminUser and password == adminPass:
        current_window.destroy()
        mainPanel()
    else:
        print("error")

passwordVisible = False
def togglePassword(entryPassword, toggleButton):
    global passwordVisible
    passwordVisible = not passwordVisible

    if passwordVisible:
        entryPassword.configure(show="")
        toggleButton.configure(text="Hide")
    else:
        entryPassword.configure(show="*")
        toggleButton.configure(text="Show")

    

def masterPanel():

    ctk.set_appearance_mode("system") # "light" or "system" or "dark"
    ctk.set_default_color_theme("blue") # or "green", "dark-blue"

    app = ctk.CTk() 
    app.title("Master Login")
    app.geometry("420x520")
    app.resizable(True, True)

    # Container #
    container = ctk.CTkFrame(app, fg_color="transparent")
    container.pack(fill="both", expand=True)
    
    # Panels #
    panel = ctk.CTkFrame(container, width=410, height=510, corner_radius=8, fg_color="transparent")
    panel.pack(expand=True) # This places the panel in true center of the container

    # Inner frame centered inside the panel to stack widgets #
    inner = ctk.CTkFrame(panel, fg_color="transparent") 
    inner.pack(expand=True) # centers the inner frame vertically/horizontally

    # Images #
    logoImage = ctk.CTkImage(light_image=Image.open('images/logoNoBg.png'), 
                             dark_image=Image.open('images/logoNoBg.png'),
                             size=(200, 100))

    logoLabel = ctk.CTkLabel(inner, text="", image=logoImage)
    logoLabel.pack(pady=1)


    # Name of the screen the user is on
    ctk.CTkLabel(inner, text="Master Login", anchor="n").pack(pady=(100,4))



    # inputs #
    ctk.CTkLabel(inner, text="Username:", anchor="w").pack(pady=(0,4))
    entryUsername = ctk.CTkEntry(inner, width=200, placeholder_text="Username")
    entryUsername.pack(pady=(0, 10))
    ctk.CTkLabel(inner, text="Password:", anchor="w").pack(pady=(0,4))
    entryPassword = ctk.CTkEntry(inner, width=200, placeholder_text="Password", show="*")
    entryPassword.pack(pady=(0, 12))


    # buttons #
    toggleButton = ctk.CTkButton(inner, text="Show", command=lambda: togglePassword(entryPassword, toggleButton), fg_color="#0066ff", hover_color="#3385ff")
    toggleButton.pack(padx=1, pady=1)
    button = ctk.CTkButton(inner, text="Login", command=lambda: verifyLogin(app, entryUsername, entryPassword), fg_color="#0066ff", hover_color="#3385ff")
    button.pack(padx=20, pady=20)

    
    
    
    
    app.mainloop()


