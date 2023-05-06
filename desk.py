from tkinter import BitmapImage
from customtkinter import CTkFrame,CTkLabel,CTk,CTkButton,set_appearance_mode,CTkImage
from pyqrcode import create
from socket import gethostbyname,gethostname
import api

def refr():
    global url
    url = "VolumeValet:"+gethostbyname(gethostname()) + ":5000"

def generate_code():
    global qr, img
    refr()
    qr = create(url)
    img = BitmapImage(data = qr.xbm(scale = 10))
    img.configure(background="white")
    display()

def display():
    label.configure(text=url)
    img_lbl.configure(image = img)
    top_label.configure(text="Enter Address:Port in app to connect\nor\nScan QR to connect")
    
   
def start_stop():
    global running
    if running == False:
        running = True
        api.start_server()
        top_label.configure(text="Enter Address:Port in app to connect\nor\nScan QR")
        btn_refr.configure(state="normal")
        btn_start.configure(text="Stop Server")
        generate_code()
        display()
        top_label.pack(padx=15,pady=10)
        img_lbl.pack()        
        bot_label.pack(pady=5, padx=10)
    else:
        running = False
        api.stop_server()
        top_label.configure(text="")
        label.configure(text="VolumeValet Server")
        btn_refr.configure(state="disabled")
        btn_start.configure(text="Start Server")
        img_lbl.configure(image="",)
        top_label.pack_forget()
        img_lbl.pack_forget()
        bot_label.pack_forget()
        
    
class App(CTk):
    
    def __init__(self):
        super().__init__()
        set_appearance_mode("system")
        self.title("VolumeValet Server")
        self.minsize(325,230)
        self.resizable(False, False)

        self.iconbitmap('code.ico')

        frame = CTkFrame(master=self)
        frame.pack(pady=20,padx=20, fill="both", expand=True)

        global label
        label = CTkLabel(master=frame, text="VolumeValet Server", font=("Berlin Sans FB", 20))
        label.pack(pady=10, padx=10)

        global btn_start
        btn_start = CTkButton(master=frame, text="Start Server", font=("Berlin Sans FB", 16),command=start_stop)
        btn_start.pack(ipady=5,ipadx=5,pady=10,padx=10)

        global btn_refr
        btn_refr = CTkButton(master=frame, state ="disabled", text="Refresh", font=("Berlin Sans FB", 16),command=generate_code)
        btn_refr.pack(ipady=5,ipadx=5,pady=10,padx=10)

        global top_label
        top_label = CTkLabel(master=frame,text=None,height=0, font=("Berlin Sans FB", 16))
        
        global img_lbl
        img_lbl = CTkLabel(master=frame,text=None)  

        global bot_label
        bot_label = CTkLabel(master=frame, text="Note: Please use refresh button\nupon network change/disconnect.", font=("Consolas", 12))
    

if __name__ == "__main__":
    running=False
    app = App()
    app.mainloop()