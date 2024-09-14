from hw02_replica import hw02_is_even

import tkinter as tk

def main():

    window = tk.Tk()
    window.title("hw03_is_even_gui")
    window.resizable(False, False)
    window.geometry("300x300+100+100")

    hw03_f2c_button = tk.Button(window, text="1부터 100까지 짝수의 합",command=hw02_is_even.main)
    hw03_f2c_button.pack()


    window.mainloop()


if __name__ == "__main__":
    main()