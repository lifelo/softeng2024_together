from hw02_replica import hw02_f2c

import tkinter as tk

def main():

    window = tk.Tk()
    window.title("hw03_f2c_gui")
    window.resizable(False, False)
    window.geometry("300x300+100+100")

    label= tk.Label(window, text="화씨온도 입력")
    label.pack()

    input_entry = tk.Entry(window)
    input_entry.pack()

    hw03_f2c_button = tk.Button(window, text="화씨를 섭씨로 변환",command=hw02_f2c.main)
    hw03_f2c_button.pack()

    output1 = tk.Entry(window)
    output1.pack()

    output2 = tk.Label(window, text="")
    output2.pack()




    window.mainloop()


if __name__ == "__main__":
    main()












