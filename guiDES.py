import tkinter as tk

class gui(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        window.title('DES crypt')
        window.geometry('1000x540')
        window.resizable(False, False)

        self.entry_crypt_1 = tk.StringVar()
        self.entry_crypt_2 = tk.StringVar()
        self.entry_crypt_3 = tk.StringVar()

        self.entry_text_lbl = tk.Label(window, font = 'Arial 14', text = 'Введите текст (8 символов)')
        self.crypt_key_lbl = tk.Label(window, font = 'Arial 14', text = 'Введите ключ шифрования (7 символов)')
        self.crypt_key_ctrl_bit_lbl = tk.Label(window, font = 'Arial 14', text = 'Ключ шифрования с битами чётности')

        self.entry_text_ent = tk.Entry(window, font = 'Arial 14', width = 20, textvariable = self.entry_crypt_1)
        self.crypt_key_ent = tk.Entry(window, font = 'Arial 14', width = 30, textvariable = self.entry_crypt_2)
        self.crypt_key_ctrl_bit_ent = tk.Entry(window, font = 'Arial 14', width = 30, textvariable = self.entry_crypt_3)

        self.lblFrame1 = tk.LabelFrame(window, font = 'Arial 14', text = 'Выбор системы представления')
        self.lblFrame2 = tk.LabelFrame(window, font = 'Arial 14', text = 'Исходные данные в выбранной системе:')
        self.lblFrame3 = tk.LabelFrame(window, font = 'Arial 14', text = 'Раундовая информация')

        self.sys_of_not = tk.IntVar()

        self.sym_rb = tk.Radiobutton(self.lblFrame1, value = 1, variable = self.sys_of_not, font = 'Arial 14', text = 'Символьная')
        self.bin_rb = tk.Radiobutton(self.lblFrame1, value = 2, variable = self.sys_of_not, font = 'Arial 14', text = 'Двоичная')
        self.hex_rb = tk.Radiobutton(self.lblFrame1, value = 3, variable = self.sys_of_not, font = 'Arial 14', text = 'Шестнадцатеричная')

        self.entry_text_sys_lbl = tk.Label(self.lblFrame2, font = 'Arial 14', text = 'Открытый текст')
        self.crypt_key_sys_lbl = tk.Label(self.lblFrame2, font = 'Arial 14', text = 'Ключ шифрования')
        self.crypt_key_ctrl_bit_sys_lbl = tk.Label(self.lblFrame2, font = 'Arial 14', text = 'Ключ с проверкой чётности')

        self.entry_text_sys_ent = tk.Entry(self.lblFrame2, font = 'Arial 14', width = 65)
        self.crypt_key_sys_ent = tk.Entry(self.lblFrame2, font = 'Arial 14', width = 65)
        self.crypt_key_ctrl_bit_sys_ent = tk.Entry(self.lblFrame2, font = 'Arial 14', width = 65)

        self.round_lbl = tk.Label(self.lblFrame3, font = 'Arial 14', text = 'Раунд')
        self.round_ent = tk.Entry(self.lblFrame3, font = 'Arial 14', width = 3)
        self.round_ent.insert(0, '0')
        self.round_btn = tk.Button(self.lblFrame3, font = 'Arial 14', text = 'Следующий раунд')

        self.type_of_crypt = tk.IntVar()

        self.encrypt_rb = tk.Radiobutton(self.lblFrame3, value = 1, variable = self.type_of_crypt, font = 'Arial 14', text = 'Зашифровка')
        self.decrypt_rb = tk.Radiobutton(self.lblFrame3, value = 2, variable = self.type_of_crypt, font = 'Arial 14', text = 'Расшифровка')

        self.left_block_lbl = tk.Label(self.lblFrame3, font = 'Arial 14', text = 'Левый полублок')
        self.right_block_lbl = tk.Label(self.lblFrame3, font = 'Arial 14', text = 'Правый полублок')
        self.round_key_block_lbl = tk.Label(self.lblFrame3, font = 'Arial 14', text = 'Раундовый ключ')

        self.left_block_ent = tk.Entry(self.lblFrame3, font = 'Arial 14', width = 73)
        self.right_block_ent = tk.Entry(self.lblFrame3, font = 'Arial 14', width = 73)
        self.round_key_block_ent = tk.Entry(self.lblFrame3, font = 'Arial 14', width = 73)

        self.crypt_text_lbl = tk.Label(window, font = 'Arial 14', text = 'Зашифрованный текст')
        self.crypt_text_ent = tk.Entry(window, font = 'Arial 14', width = 65)

        self.entry_text_lbl.grid(row = 0, column = 0, padx = 6)
        self.crypt_key_lbl.grid(row = 0, column = 1, columnspan = 2, padx = 6)
        self.crypt_key_ctrl_bit_lbl.grid(row = 0, column = 3, columnspan = 2, padx = 6)

        self.entry_text_ent.grid(row = 1, column = 0, sticky = 'w', padx = 6)
        self.crypt_key_ent.grid(row = 1, column = 1, sticky = 'w', columnspan = 2, padx = 8)
        self.crypt_key_ctrl_bit_ent.grid(row = 1, column = 3, columnspan = 2, padx = 8)

        self.lblFrame1.grid(row = 2, column = 0, columnspan = 5, sticky = 'nesw', pady = 15)
        self.sym_rb.grid(row = 0, column = 0, padx = 15, pady = 6, sticky = 'w')
        self.bin_rb.grid(row = 0, column = 1, padx = 15, pady = 6, sticky = 'n')
        self.hex_rb.grid(row = 0, column = 3, padx = 15, pady = 6, sticky = 'e')

        self.lblFrame2.grid(row = 3, column = 0, columnspan = 5, sticky = 'nesw')
        self.entry_text_sys_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = 'w', pady = 4, padx = 5)
        self.crypt_key_sys_lbl.grid(row = 1, column = 0, columnspan = 2, sticky = 'w', pady = 4, padx = 5)
        self.crypt_key_ctrl_bit_sys_lbl.grid(row = 2, column = 0, columnspan = 2, sticky = 'w', pady = 4, padx = 5)

        self.entry_text_sys_ent.grid(row = 0, column = 2, columnspan = 3, sticky = 'w', pady = 4, padx = 5)
        self.crypt_key_sys_ent.grid(row = 1, column = 2, columnspan = 3, sticky = 'w', pady = 4, padx = 5)
        self.crypt_key_ctrl_bit_sys_ent.grid(row = 2, column = 2, columnspan = 3, sticky = 'w', pady = 4, padx = 5)

        self.lblFrame3.grid(row = 4, column = 0, columnspan = 5, sticky = 'nesw', pady = 10)
        self.round_lbl.grid(row = 0, column = 0)
        self.round_ent.grid(row = 0, column = 1)
        self.round_btn.grid(row = 0, column = 2, padx = 8, pady = 6)
        self.encrypt_rb.grid(row = 0, column = 3)
        self.decrypt_rb.grid(row = 0, column = 4)
        self.left_block_lbl.grid(row = 1, column = 0, columnspan = 2, pady = 4, padx = 5)
        self.right_block_lbl.grid(row = 2, column = 0, columnspan = 2, pady = 4, padx = 5)
        self.round_key_block_lbl.grid(row = 3, column = 0, columnspan = 2, pady = 4, padx = 5)
        self.left_block_ent.grid(row = 1, column = 2, columnspan = 3, pady = 4, padx = 5)
        self.right_block_ent.grid(row = 2, column = 2, columnspan = 3, pady = 4, padx = 5)
        self.round_key_block_ent.grid(row = 3, column = 2, columnspan = 3, pady = 4, padx = 5)

        self.crypt_text_lbl.grid(row = 5, column = 0,  sticky = 'w')
        self.crypt_text_ent.grid(row = 5, column = 1, columnspan = 4, sticky = 'w')     

if __name__ == "__main__":
    window = tk.Tk()
    q = gui(window)
    q.mainloop()