import customtkinter as ctk
from PIL import Image

def accountsPanel():
    ctk.set_appearance_mode("system") # "light" or "system" or "dark"
    ctk.set_default_color_theme("blue") # or "green", "dark-blue"

    app = ctk.CTk() 
    app.title("Account Information")
    app.geometry("420x420")

    # Images #
    logoImage = ctk.CTkImage(light_image=Image.open('images/logoNoBg.png'), 
                             dark_image=Image.open('images/logoNoBg.png'),
                             size=(200, 100))

    logoLabel = ctk.CTkLabel(app, text="", image=logoImage)
    logoLabel.pack(pady=20)

    credLabel = ctk.CTkLabel(app, text="Login Credentials", anchor="n", font=("Berlin Sans FB", 26))
    credLabel.pack(pady=(10,4))

    # inner frame #
    inner = ctk.CTkFrame(app, fg_color="transparent")
    inner.pack(expand=True)

    #left panel
    panelLeft = ctk.CTkFrame(inner, width=210, corner_radius=8, fg_color="#2b2b2b") 
    panelLeft.pack(side="left", fill="x", padx=1, pady=1)

    #left panel labels
    urlLabel = ctk.CTkLabel(panelLeft, text="URL:", anchor="ne")
    urlLabel.pack(pady=(15,10))
    usernameLabel = ctk.CTkLabel(panelLeft, text="Username:", anchor="w")
    usernameLabel.pack(pady=(15,10))
    passwordLabel = ctk.CTkLabel(panelLeft, text="password:", anchor="w")
    passwordLabel.pack(pady=(15,10))

    #right panel
    panelRight = ctk.CTkFrame(inner, width=210, corner_radius=8, fg_color="#2b2b2b") 
    panelRight.pack(side="right", fill="x", padx=1, pady=1)

    #right panel label
    url = ctk.CTkLabel(panelRight, text="http://www.stupid-website.com", anchor="ne")
    url.pack(pady=(15,10))
    username = ctk.CTkLabel(panelRight, text="Side show bob", anchor="w")
    username.pack(pady=(15,10))
    password = ctk.CTkLabel(panelRight, text="***********", anchor="w")
    password.pack(pady=(15,10))

    app.mainloop()

accountsPanel()