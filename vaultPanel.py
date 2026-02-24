import customtkinter as ctk



"""
This file is code for the main panel. (Vault)
"""

def mainPanel():
    ctk.set_appearance_mode("system") # "light" or "system" or "dark"
    ctk.set_default_color_theme("blue") # or "green", "dark-blue"

    def buttonCallback():
        print("button clicked")

    app = ctk.CTk() 
    app.title("Forget me not password manager") 
    app.geometry("700x420") 

    # Name of the screen the user is on
    ctk.CTkLabel(app, text="Password Vault", anchor="n").pack(pady=(10,4))
    
    # Right panel
    panel = ctk.CTkFrame(master=app, width=220, corner_radius=8, fg_color="#2b2b2b") 
    panel.pack(side="right", fill="y", padx=12, pady=12)
    
    ctk.CTkLabel(panel, text="Add new account password", anchor="n").pack(pady=(10,4))
    # Inner frame centered inside the panel to stack widgets #
    inner = ctk.CTkFrame(panel, fg_color="grey") 
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
    button = ctk.CTkButton(inner, text="Add account", command=buttonCallback)
    button.pack(padx=20, pady=20)

    # Left panel
    panel = ctk.CTkFrame(master=app, width=420, corner_radius=8, fg_color="#2b2b2b") 
    panel.pack(side="left", fill="y", padx=12, pady=12)

    
    app.mainloop()

mainPanel()