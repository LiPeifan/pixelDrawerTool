import tkinter as tk
import customtkinter as ctk

class MenuBar():
    def __init__(self, master):
        """"菜单栏初始化函数"""
        self.master = master

    def create_menu_bar(self):
        """创建主菜单栏及其菜单项"""
        self.menu_bar = tk.Menu(self.master)

        #创建文件菜单
        file_menu = tk.Menu(MenuBar, tearoff=0)
        #添加菜单项
        file_menu.add_command(
            label="新建",
            #command=new_file(),
        )
        file_menu.add_command(
            label="打开",
            #command=open_file(),
        )
        file_menu.add_command(
            label="最近打开文件"
        )

