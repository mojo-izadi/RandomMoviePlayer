from tkinter import *
from tkinter import messagebox


def show_error_message_box():
    messagebox.showerror("Error", "No movies matched your filters")


def create_GUI():
    def toggle_textboxes1():
        if chk1_var.get() == 1:
            min_year_label.grid(row=0, column=2)
            min_year.grid(row=0, column=3)
            max_year_label.grid(row=0, column=4)
            max_year.grid(row=0, column=5)
        else:
            min_year.grid_forget()
            max_year.grid_forget()
            min_year_label.grid_forget()
            max_year_label.grid_forget()

    def toggle_textboxes2():
        if chk2_var.get() == 1:
            min_runtime_label.grid(row=1, column=2)
            min_runtime.grid(row=1, column=3)
            max_runtime_label.grid(row=1, column=4)
            max_runtime.grid(row=1, column=5)
            minute_label.grid(row=1, column=6)
        else:
            min_runtime.grid_forget()
            max_runtime.grid_forget()
            min_runtime_label.grid_forget()
            max_runtime_label.grid_forget()
            minute_label.grid_forget()

    root = Tk()

    root.title("movie attributes")
    root.geometry('600x200')

    chk1_var = IntVar()
    chk1 = Checkbutton(root, text="year", variable=chk1_var, command=toggle_textboxes1)
    chk1.grid(row=0, column=0)

    min_year = Entry(root)
    max_year = Entry(root)
    min_year_label = Label(root, text='from')
    max_year_label = Label(root, text='to')

    chk2_var = IntVar()
    chk2 = Checkbutton(root, text="runtime", variable=chk2_var, command=toggle_textboxes2)
    chk2.grid(row=1, column=0)

    min_runtime = Entry(root)
    max_runtime = Entry(root)
    min_runtime_label = Label(root, text='from')
    max_runtime_label = Label(root, text='to')
    minute_label = Label(root, text='minutes')

    to_return = []
    play_button = Button(root, command=lambda: (
        to_return.append(chk1_var.get() == 1),
        to_return.append(min_year.get()),
        to_return.append(max_year.get()),
        to_return.append(chk2_var.get() == 1),
        to_return.append(min_runtime.get()),
        to_return.append(max_runtime.get()),
        root.destroy()
    ), text='play random movie')

    play_button.grid(row=4, column=0)

    root.mainloop()

    return to_return
