from tkinter import *
import requests


class TaylorQuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Taylor Swift Quotes")
        self.root.config(padx=50, pady=50)

        self.canvas = Canvas(width=300, height=414)
        self.background_img = PhotoImage(file="background_edited (1).png")
        self.canvas.create_image(150, 207, image=self.background_img)
        self.quote_text = self.canvas.create_text(150, 207, text="Lyrics Go Here", width=250,
                                                  font=("Arial", 18, "bold"), fill="white")
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.taylor_img = PhotoImage(file="taylor.png.png")
        self.taylor_button = Button(image=self.taylor_img, highlightthickness=0, command=self.get_quote)
        self.taylor_button.grid(row=1, column=0, columnspan=2)

    def get_quote(self):
        try:
            response = requests.get("https://taylorswiftapi.onrender.com/get")
            response.raise_for_status()
            data = response.json()
            quote = datax["quote"]
            self.canvas.itemconfig(self.quote_text, text=quote)
        except requests.exceptions.RequestException as e:
            self.canvas.itemconfig(self.quote_text, text="Error fetching quote.")


if __name__ == "__main__":
    root = Tk()
    app = TaylorQuoteApp(root)
    root.mainloop()
