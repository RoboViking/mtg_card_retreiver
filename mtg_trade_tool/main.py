import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")  

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        width = "1920"
        height = "1080"
        self.title("D4 Trade Tool")
        self.geometry(f"{width}x{height}")
        self.minsize(640,480)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=120, corner_radius=0)
        self.sidebar.grid(row=0,column=0, rowspan=4, sticky="nsew")
        self.sidebar.grid_rowconfigure(5, weight=1)

        # Sidebar widgets
        self.logo_text = ctk.CTkLabel(self.sidebar, text="D4 Trade Tool", font=ctk.CTkFont(size=15,weight="bold"))
        self.logo_text.grid(row=0, column=0, padx=20, pady=20)

        self.scaling_label= ctk.CTkLabel(self.sidebar, text="Collections:", anchor="w")
        self.scaling_label.grid(row=1, column=0, padx=10, pady=(10,0))
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar, command=self.add_collection_event, text="Add collection")
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=(10, 5))
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar, command=self.remove_collection_event, text="Remove collection")
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=(5, 5))
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar, command=self.update_collections_event, text="Update collections")
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=(5, 10))

        self.scaling_label= ctk.CTkLabel(self.sidebar, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=10, pady=(20,0))
        self.scaling_option_menu = ctk.CTkOptionMenu(self.sidebar, values=["75%","100%","125%","150%","175%","200%"], command=self.scale_event)
        self.scaling_option_menu.grid(row=8, column=0, padx=10, pady=(5,20))

        # deck entry frame
        self.entry_frame = ctk.CTkFrame(self)
        self.entry_frame.grid(row=0,column=1, rowspan=3, columnspan=1, padx=(20,5),pady=(20,20), sticky="nsew")
        
        # collection frame
        self.collection_frame = ctk.CTkFrame(self)
        self.collection_frame.grid(row=0,column=2, rowspan=3, columnspan=2, padx=(5,20),pady=(20,20), sticky="nsew")

        # Set default values 
        self.scaling_option_menu.set("100%")
    
    def add_collection_event(self):
        pass

    def remove_collection_event(self):
        pass

    def update_collections_event(self):
        pass

    def scale_event(self, new_scaling: str):
        new_scale_float = int(new_scaling.replace("%", ""))/100
        ctk.set_widget_scaling(new_scale_float)




if __name__ == "__main__":
    app = App()
    app.mainloop()




