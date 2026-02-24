# This file is for the master login panel of the program
import customtkinter as ctk

def masterPanel():
    ctk.set_appearance_mode("system") # "light" or "system" or "dark"
    ctk.set_default_color_theme("blue") # or "green", "dark-blue"

    app = ctk.CTk() 
    app.title("Forget me not password manager")
    app.geometry("420x620")
    app.resizable(True, True)

    # Container #
    container = ctk.CTkFrame(app, fg_color="transparent")
    container.pack(fill="both", expand=True)

    # Panels #
    panel = ctk.CTkFrame(container, width=400, height=600, corner_radius=8)
    panel.pack(expand=True) # This places the panel in true center of the container

    # Inner frame centered inside the panel to stack widgets #
    inner = ctk.CTkFrame(panel, fg_color="transparent") 
    inner.pack(expand=True) # centers the inner frame vertically/horizontally

    # inputs #
    ctk.CTkLabel(inner, text="Username:", anchor="w").pack(pady=(0,4))
    entryUsername = ctk.CTkEntry(inner, width=200, placeholder_text="Username")
    entryUsername.pack(pady=(0, 10))
    ctk.CTkLabel(inner, text="Password:", anchor="w").pack(pady=(0,4))
    entryPassword = ctk.CTkEntry(inner, width=200, placeholder_text="Password", show="*")
    entryPassword.pack(pady=(0, 12))

    app.mainloop()

masterPanel()