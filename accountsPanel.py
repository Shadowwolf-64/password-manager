import customtkinter as ctk
from PIL import Image

def accountsPanel():
    ctk.set_appearance_mode("system") # "light" or "system" or "dark"
    ctk.set_default_color_theme("blue") # or "green", "dark-blue"

    app = ctk.CTk() 
    app.title("Account Information")
    app.geometry("420x520")

    # inner frame #
    inner = ctk.CTkFrame(app, fg_color="transparent")
    inner.pack(expand=True)
    # Images #
    logoImage = ctk.CTkImage(light_image=Image.open('images/logoNoBg.png'), 
                             dark_image=Image.open('images/logoNoBg.png'),
                             size=(200, 100))

    logoLabel = ctk.CTkLabel(inner, text="", image=logoImage)
    logoLabel.pack(pady=1)

    # Labels #
    urlLabel = ctk.CTkLabel(inner, text="URL:", anchor="w").pack(pady=(150,4))
    usernameLabel = ctk.CTkLabel(inner, text="Username:", anchor="w").pack(pady=(0,4))
    passwordLabel = ctk.CTkLabel(inner, text="password:", anchor="w").pack(pady=(0,4))
    app.mainloop()

accountsPanel()