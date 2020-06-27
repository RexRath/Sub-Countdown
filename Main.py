import tkinter as tk
from tkinter import filedialog, messagebox
import os
import urllib


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_countdown = tk.Label(self, text="")
        self.lbl_countdown.pack(side="top")
        self.btn_settings = tk.Button(self, text="Settings")
        self.btn_settings.pack(side="left")
        self.btn_quit = tk.Button(self, text="Quit", command=self.master.destroy)
        self.btn_quit.pack(side="right")

    def update_subs(self, subs):
        self.lbl_countdown.config(text=subs)


def set_default_tiers():
    tier_list = ("65", "80", "100", "125", "150", "175", "200", "225", "250", "300",
                 "350", "400", "450", "500", "600", "700", "800", "900", "1000",
                 "1200", "1400", "1600", "1800", "2000", "2200", "2400", "2600",
                 "2800", "3000", "3200", "3400", "3600", "3800", "4000", "4200",
                 "4400", "4600", "4800", "5000", "5400", "5800", "6200", "7000")
    return tier_list


def get_stream_labels_dir():
    while True:
        stream_labels_dir = filedialog.askdirectory(parent=root, title="Locate Stream Labels Output Directory")
        if stream_labels_dir == "":
            messagebox.showerror(title="Error", message="No file chosen, closing.")
            root.destroy()
            break
        elif not os.path.isfile(stream_labels_dir + "/total_subscriber_score.txt"):
            messagebox.showerror(title="Error",
                                 message="File 'total_subscriber_score.txt' not found in selected folder. "
                                         "Please ensure the folder is correct and that the file exists.")
            continue
        else:
            total_sub_count_file = open(stream_labels_dir + "/total_subscriber_score.txt", "r")
            return str(total_sub_count_file.read())


if not os.path.isdir("res"):
    error_win = tk.Tk()
    error_win.withdraw()
    messagebox.showwarning(parent=error_win, message="Resource folder not found. Creating.")
    error_win.destroy()
    os.mkdir("res")
if not os.path.isfile("res/config.txt"):
    config_file = open("res/config.txt", "w")
    emote_tier_file = open("res/tier_cfg.txt", "w")
    for ele in set_default_tiers():
        emote_tier_file.write(ele + "\n")
else:
    config_file = open("res/config.txt", "w")
    emote_tier_file = open("res/tier_cfg.txt", "w")

root = tk.Tk()
root.geometry("300x100")
root.resizable(width=False, height=False)
root.title("Emote Unlock")
try:
    root.iconbitmap("res/app.ico")
except:
    pass
app = Application(master=root)
sub_count = str(get_stream_labels_dir())
app.update_subs(sub_count)
app.mainloop()
config_file.close()
