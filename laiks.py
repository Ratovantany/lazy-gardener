import tkinter as tk


class CounterApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.counter = 0
        self.started = False

        self.label = tk.Label(self.root, text="Nekas nelaistas")
        self.label.pack()

        self.button = tk.Button(
            self.root,
            text="Laistit/ Apturet",
            command=self.toggle_counter
        )
        self.button.pack()

    def toggle_counter(self):
        self.started = not self.started

        if self.started:
            self.counter = 0
            self.update_counter()
        else:
            self.label.config(text="Nekas nelaistas")

    def update_counter(self):
        self.counter += 1
        self.label.config(text=f"Laistas (sekundes): {self.counter}")
        if self.started:
            self.root.after(1000, self.update_counter)

app = CounterApp()
app.root.mainloop()


