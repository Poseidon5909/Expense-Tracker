import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
from tkinter import ttk
import tkinter as tk
from db.db.db_connect import get_connection

class MainApp:
  def __init__(self, root):
    self.root = root
    self.root.title("FinTrack — Smart Expense Manager")
    self.root.geometry("1000x650")
    self.root.minsize(900, 600)

    self.style = Style(theme="flatly")
    self.current_theme = "flatly"
    
    self._create_header()
    self._create_sidebar()
    self._create_main_area()

    self.frames = {}
    self._init_frames()
    self.show_frame("Home")

# UI Building
  def _create_header(self):
    header = ttk.Frame(self.root, padding=(12, 8))
    header.pack(side=TOP, fill=X)

    title = ttk.Label(header, text="FinTrack", font=("Segoe UI", 18, "bold"))
    title.pack(side=LEFT, padx=(8,12))

    tagline = ttk.Label(header, text="Smart Personal Expense & Budget Managment", font=("Segoe UI", 10))  
    tagline.pack(side=LEFT, padx=(4, 12))

    self.theme_btn = ttk.Button(header, text="🌙 Dark Mode", bootstyle="info-outline", command=self.toggle_theme)
    self.theme_btn.pack(side=RIGHT, padx=12)
  def _create_sidebar(self):
        sidebar = ttk.Frame(self.root, width=220, padding=(10, 10))
        sidebar.pack(side=LEFT, fill=Y)

        ttk.Label(sidebar, text="Navigation", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0,8))

       # Buttons
        btns = [
            ("Home", lambda: self.show_frame("Home")),
            ("Add Expense", lambda: self.show_frame("Add")),
            ("Manage Expenses", lambda: self.show_frame("Manage")),
            ("Analytics", lambda: self.show_frame("Analytics")),
            ("Settings", lambda: self.show_frame("Settings")),
        ]

        for (text, cmd) in btns:
            b = ttk.Button(sidebar, text=text, width=20, command=cmd, bootstyle="primary")
            b.pack(pady=6, anchor="w")

       
        ttk.Label(sidebar, text="\nFinTrack v4.5", font=("Segoe UI", 9)).pack(side=BOTTOM, pady=12, anchor="w")

  def _create_main_area(self):
        self.main_area = ttk.Frame(self.root, padding=(12, 10))
        self.main_area.pack(side=LEFT, fill=BOTH, expand=True)

  def _init_frames(self):
      frm_home = ttk.Frame(self.main_area)
      lbl = ttk.Label(frm_home, text="Home - Overview", font=("Segoe UI", 14, "bold"))
      lbl.pack(anchor="nw")
      info = ttk.Label(frm_home, text="Total spent: --\nRecent transcations:\n\n(Analytics summary will show here)", justify=LEFT)
      info.pack(anchor="nw", pady=10) 
      self.frames["Home"] = frm_home

    # Add Expense
      frm_add = ttk.Frame(self.main_area)
      ttk.Label(frm_add, text="Add Expense", font=("segoe UI", 14, "bold")).pack(anchor="nw")
      ttk.Label(frm_add, text="(From widgets will go here)").pack(anchor="nw", pady=8)
      self.frames["Add"] = frm_add

    # Manage frame  
      frm_manage = ttk.Frame(self.main_area)
      ttk.Label(frm_manage, text="Manage Expenses", font=("Segoe UI", 14, "bold")).pack(anchor="nw")
      ttk.Label(frm_manage, text="(Treeeview table + Edit/Delete actions will go here)").pack(anchor="nw", pady=8)
      self.frames["Manage"] = frm_manage

    # Analytics frame
      frm_analytics = ttk.Frame(self.main_area)
      ttk.Label(frm_analytics, text="Analytics", font=("Segoe UI", 14, "bold")).pack(anchor="nw")
      ttk.Label(frm_analytics, text="(Pie chart/ Monthly bar chart will be embedded here)").pack(anchor="nw", pady=8)
      self.frames["Analytics"]  = frm_analytics

    # Settings frame
      frm_settings = ttk.Frame(self.main_area)  
      ttk.Label(frm_settings, text="Settings", font=("Segoe UI", 14, "bold")).pack(anchor="nw")
      ttk.Label(frm_settings, text="Theme and app prefernces").pack(anchor="nw", pady=8)
      self.frames["Settings"] = frm_settings

      for f in self.frames.values():
          f.place(relx=0, rely=0, relwidth=1, relheight=1)

  def show_frame(self, name):
      frame = self.frames.get(name)
      if frame:
          frame.lift()
      else:
          print(f"[FinTrack] frame '{name} not found") 

  def toggle_theme(self):
      if self.current_theme in ("darkly", "solar", "superhero"):
          new_theme = "flatly"
          new_text = "🌙 Dark Mode"
      else:
          new_theme = "darkly"    
          new_text = "☀️ Light Mode"

      try:
          self.style.theme_use(new_theme)
          self.current_theme = new_theme
          self.theme_btn.config(text=new_text)
          self.root.update_idletasks()
      except Exception as e:
          print("Theme switch failed:", e)

def main():
    root = tb.Window(themename="flatly")
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()