import tkinter as tk

app = tk.Tk()

part_text = ""
part_label = tk.Label(app, text="part name", font=("bold", 14), pady=20)
part_label.grid(row=0, column=0)
part_entry = tk.Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

customer_text = ""
customer_label = tk.Label(app, text="customer", font=("bold", 14))
customer_label.grid(row=0, column=3)
customer_entry = tk.Entry(app, textvariable=part_text)
customer_entry.grid(row=0, column=4)


app.title("Manager")
app.geometry("700x350")

app.mainloop()

