from hw02_replica import hw02_odd_even_num

import tkinter as tk

def main():

    window = tk.Tk()
    window.title("hw03_odd_even_num_gui")
    window.resizable(False, False)
    window.geometry("300x300+100+100")

    label= tk.Label(window, text="숫자 입력")
    label.pack()

    input_entry = tk.Entry(window)
    input_entry.pack()

    hw03_f2c_button = tk.Button(window, text="소수 구하기",command=hw02_odd_even_num.main)
    hw03_f2c_button.pack()

    output1 = tk.Entry(window)
    output1.pack()

    output2 = tk.Label(window, text="")
    output2.pack()




    window.mainloop()


if __name__ == "__main__":
    main()