import customtkinter as cTK
import tkinter as tk
from PIL import Image
import json
import os
from app.views.widgets.menu_bar import MenuBar


class MainApp(cTK.CTk):
    def __init__(self):
        super().__init__()
        self.title("PixelDrawer")
        self.geometry("800x600")
        menu_bar = MenuBar(self)
