import tkinter as tk

window = tk.Tk()
window.geometry("200x200")
window.title("BMI Calculator")

_kilo = 0
_boy = 0
_calculate = 0



def setCalculations(event = any):
    global _kilo , _boy ,_calculate
    _kilo = int(weightEntry.get())
    _boy = int(heightEntry.get()) / 100
    _calculate = _kilo / (_boy ** 2)
    resultLabel(_calculate)
    print(_calculate)

def resultLabel(ort):
    text = ""
    if ort >= 30.0 and ort <= 35.0:
        text = "Obez (1.derece obezite)"
    elif ort >=25.0 and ort < 30:
        text = "Fazla Kilolu"
    elif ort >= 18.5 and ort < 25:
        text = "Normal Kilo"
    elif ort <= 18.4:
        text = "Zayıf"
    else :
        text = "Doktora Git"

    showResultLabel.config(text=text)

weightLabel = tk.Label(window, text="Enter Your Weight (kg)")
weightEntry = tk.Entry(window)

heightLabel = tk.Label(window, text="Enter Your Height (cm)")
heightEntry = tk.Entry(window)

calButton = tk.Button(window, text="Calculate" , command= setCalculations)

showResultLabel = tk.Label(window)

window.bind("<Return>", setCalculations)

weightLabel.pack()
weightEntry.pack()
heightLabel.pack()
heightEntry.pack()
calButton.pack()
showResultLabel.pack()
window.mainloop()