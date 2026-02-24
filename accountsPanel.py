import customtkinter as ctk
from PIL import Image

def accountsPanel():
    ctk.set_appearance_mode("system") # "light" or "system" or "dark"
    ctk.set_default_color_theme("blue") # or "green", "dark-blue"

    app = ctk.CTk() 
    app.title("Forget me not password manager") 
    app.geometry("700x420") 

    # Images #
    logoImage = ctk.CTkImage(light_image=Image.open('images/logoNoBg.png'), 
                             dark_image=Image.open('images/logoNoBg.png'),
                             size=(200, 100))

    logoLabel = ctk.CTkLabel(app, text="", image=logoImage)
    logoLabel.pack(pady=1)

    app.mainloop()

accountsPanel()