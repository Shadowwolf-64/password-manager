import customtkinter as ctk

def accountsPanel():
    ctk.set_appearance_mode("system") # "light" or "system" or "dark"
    ctk.set_default_color_theme("blue") # or "green", "dark-blue"

    app = ctk.CTk() 
    app.title("Forget me not password manager") 
    app.geometry("700x420") 

    app.mainloop()

accountsPanel()