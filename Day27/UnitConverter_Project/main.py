from tkinter import *

window=Tk()
window.title("Miles to Kilometer converter")
window.minsize(height=100,width=200)
window.config(padx=20,pady=20)
def calculate():
    miles=float(miles_input.get())
    km=round(miles*1.609344)
    kilometer_result_label["text"]=str(km)

miles_input=Entry(width=10)
miles_input.grid(column=1,row=0)

miles_label=Label(text="Miles")
miles_label.config(padx=10)
miles_label.grid(column=2,row=0)

is_equal_label=Label(text="is equal to")
is_equal_label.config(padx=10)
is_equal_label.grid(column=0,row=1)

kilometer_result_label=Label(text="0")
kilometer_result_label.config(padx=10)
kilometer_result_label.grid(column=1,row=1)

kilometer_label=Label(text="Km")
kilometer_label.grid(column=2,row=1)

calculate_button=Button(text="Calculate",command=calculate)
calculate_button.grid(column=1,row=2)

window.mainloop()


