import tkinter as tk
import speedtest
import threading

root = tk.Tk()
root.title("Internet Speedtest")
root.geometry("400x300")
root.resizable(False, False)

resultD = tk.Label(root, text="")
resultU = tk.Label(root, text="")
resultP = tk.Label(root, text="")

loading_label = tk.Label(root, text="Testing in process...", fg="green")


def SpTest():
    Startbutton.pack_forget()
    loading_label.pack(pady=10)
    
    st = speedtest.Speedtest(secure=True)
    st.get_best_server()

    download = st.download()
    upload = st.upload()
    ping = st.results.ping
    resultD.config(text=f"download {download / 1_000_000:.2f} Mbps")
    resultU.config(text=f"upload {upload / 1_000_000:.2f} Mbps")
    resultP.config(text=f"Ping: {ping:.2f} ms")
    
    loading_label.config(text="Test Completed")

    
    
    
def spTestThread():
    threading.Thread(target=SpTest).start()
    

title = tk.Label(root, font=("Arial", 24), text="Internet Speedtest")
Startbutton = tk.Button(root, text="Test your internet!", command=spTestThread)

# Made by luka

madeBytxt = tk.Label(root, text="Made by Tryharddev | Luka")

title.pack()
Startbutton.pack(pady=10)
resultD.pack()
resultU.pack()
resultP.pack()
madeBytxt.pack(side="bottom")
root.mainloop()