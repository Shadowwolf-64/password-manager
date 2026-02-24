import customtkinter as ctk



"""
This file is code for the main panel. (Vault)
"""

def mainPanel():
    ctk.set_appearance_mode("system") # "light" or "system" or "dark"
    ctk.set_default_color_theme("blue") # or "green", "dark-blue"

    app = ctk.CTk() 
    app.title("Forget me not password manager") 
    app.geometry("700x420") 
    
    # Right panel
    panel = ctk.CTkFrame(master=app, width=220, corner_radius=8, fg_color="#2b2b2b") 
    panel.pack(side="right", fill="y", padx=12, pady=12)
    
    app.mainloop()

mainPanel()