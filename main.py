from tkinter import *
import requests

def get_quote():
    pass
    res=requests.get("https://taylorswiftapi.onrender.com/get")
    res.raise_for_status()
    data=res.json()
    quote=data["quote"]
    canvas.itemconfig(quote_text, text=quote)



window = Tk()
window.title("Taylor says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background_edited (1).png")
canvas.create_image(150, 207, image=background_img,)
quote_text = canvas.create_text(150, 207, text="Lyrics Goes HERE", width=250, font=("Arial", 24, "bold"), fill="white")
canvas.grid(row=0, column=0)

taylor_img = PhotoImage(file="taylor.png.png")
taylor_button = Button(image=taylor_img, highlightthickness=0, command=get_quote)
taylor_button.grid(row=1, column=0)



window.mainloop()