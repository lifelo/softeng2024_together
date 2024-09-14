from hw02_replica import hw02_calculate_primes

import tkinter as tk

def main():
    window = tk.Tk()
    window.title("hw03_calculate_primes_gui")
    window.resizable(False, False)
    window.geometry("300x300+100+100")

    label = tk.Label(window, text="숫자 입력하기")
    label.pack()

    input_entry = tk.Entry(window)
    input_entry.pack()

    hw03_f2c_button = tk.Button(window, text="소수 판별", command=hw02_calculate_primes.main)
    hw03_f2c_button.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
