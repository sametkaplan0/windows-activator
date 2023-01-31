"""
Activation Keys:
  Home: TX9XD-98N7V-6WMQ6-BX7FG-H8Q99 
  Home N: 3KHY7-WNT83-DGQKR-F7HPR-844BM 
  Home Single Language: 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH 
  Home Country Specific: PVMJN-6DFY6-9CCP6-7BKTT-D3WVR 
  Professional: W269N-WFGWX-YVC9B-4J6C9-T83GX 
  Professional N: MH37W-N47XK-V7XM9-C7227-GCQG9 
  Education: NW6C2-QMPVW-D7KKK-3GKT6-VCFB2 
  Education N: 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ 
  Enterprise: NPPR9-FWDCX-D2C8J-H872K-2YT43 
  Enterprise N: DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4

Activation Code:
  slmgr.vbs /ipk "KEY" 
  slmgr.vbs /skms kms.lotro.cc 
  slmgr.vbs -ato
"""

from tkinter import *
import tkinter.messagebox as msg
import os
import time
import webbrowser

def callback(event):
    webbrowser.open_new("https://github.com/sametKaplan0")
def home():
    os.popen('slmgr.vbs /ipk "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"')
    time.sleep(1)
    os.popen('slmgr.vbs /skms kms.lotro.cc')
    time.sleep(1)
    os.popen('slmgr.vbs -ato')
    msg.showinfo(title="Succesfully", message="Please restart your computer for the changes to take effect.")
def homen():
    os.popen('slmgr.vbs /ipk "3KHY7-WNT83-DGQKR-F7HPR-844BM"')
    time.sleep(1)
    os.popen('slmgr.vbs /skms kms.lotro.cc')
    time.sleep(1)
    os.popen('slmgr.vbs -ato')
    msg.showinfo(title="Succesfully", message="Please restart your computer for the changes to take effect.")
def homesl():
    os.popen('slmgr.vbs /ipk "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH"')
    time.sleep(1)
    os.popen('slmgr.vbs /skms kms.lotro.cc')
    time.sleep(1)
    os.popen('slmgr.vbs -ato')
    msg.showinfo(title="Succesfully", message="Please restart your computer for the changes to take effect.")
def homecs():
    os.popen('slmgr.vbs /ipk "PVMJN-6DFY6-9CCP6-7BKTT-D3WVR"')
    time.sleep(1)
    os.popen('slmgr.vbs /skms kms.lotro.cc')
    time.sleep(1)
    os.popen('slmgr.vbs -ato')
    msg.showinfo(title="Succesfully", message="Please restart your computer for the changes to take effect.")
def pro():
    os.popen('slmgr.vbs /ipk "W269N-WFGWX-YVC9B-4J6C9-T83GX"')
    time.sleep(1)
    os.popen('slmgr.vbs /skms kms.lotro.cc')
    time.sleep(1)
    os.popen('slmgr.vbs -ato')
    msg.showinfo(title="Succesfully", message="Please restart your computer for the changes to take effect.")
def pron():
    os.popen('slmgr.vbs /ipk "MH37W-N47XK-V7XM9-C7227-GCQG9"')
    time.sleep(1)
    os.popen('slmgr.vbs /skms kms.lotro.cc')
    time.sleep(1)
    os.popen('slmgr.vbs -ato')
    msg.showinfo(title="Succesfully", message="Please restart your computer for the changes to take effect.")
def edu():
    os.popen('slmgr.vbs /ipk "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2 "')
    time.sleep(1)
    os.popen('slmgr.vbs /skms kms.lotro.cc')
    time.sleep(1)
    os.popen('slmgr.vbs -ato')
    msg.showinfo(title="Succesfully", message="Please restart your computer for the changes to take effect.")
def edun():
    os.popen('slmgr.vbs /ipk "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ"')
    time.sleep(1)
    os.popen('slmgr.vbs /skms kms.lotro.cc')
    time.sleep(1)
    os.popen('slmgr.vbs -ato')
    msg.showinfo(title="Succesfully", message="Please restart your computer for the changes to take effect.")
def ente():
    os.popen('slmgr.vbs /ipk "NPPR9-FWDCX-D2C8J-H872K-2YT43"')
    time.sleep(1)
    os.popen('slmgr.vbs /skms kms.lotro.cc')
    time.sleep(1)
    os.popen('slmgr.vbs -ato')
    msg.showinfo(title="Succesfully", message="Please restart your computer for the changes to take effect.")
def enten():
    os.popen('slmgr.vbs /ipk "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4"')
    time.sleep(1)
    os.popen('slmgr.vbs /skms kms.lotro.cc')
    time.sleep(1)
    os.popen('slmgr.vbs -ato')
    msg.showinfo(title="Succesfully", message="Please restart your computer for the changes to take effect.")
def restart():
    os.popen("shutdown /r -t 5")
window = Tk()
window.title("Windows Activator by Samet Kaplan")
window.geometry("360x290")
lbl = Label(window, text="Please select your operating system type.")
lbl.pack()
btn = Button(text="Home", command=home)
btn.pack()
btn = Button(text="Home Single Language", command=homesl)
btn.pack()
btn = Button(text="Home Country Specific", command=homecs)
btn.pack()
btn = Button(text="Professional", command=pro)
btn.pack()
btn = Button(text="Professional N", command=pron)
btn.pack()
btn = Button(text="Education", command=edu)
btn.pack()
btn = Button(text="Education N", command=edun)
btn.pack()
btn = Button(text="Enterprise", command=ente)
btn.pack()
btn = Button(text="Enterprise N", command=enten)
btn.pack()
btn = Button(text="Restart", command=restart)
github = Label(window, text="GitHub", fg="blue", cursor="hand2")
github.pack()
github.bind("<Button-1>", callback)
window.mainloop()
