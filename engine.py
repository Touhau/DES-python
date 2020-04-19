import tkinter as tk
from guiDES import gui
from transform import translate
from tkinter import messagebox as mb
import random
import re

class engine(gui):
    def __init__(self, window):
        super().__init__(window)
        self.key_generation()
        # self.entry_crypt_2.trace('w',lambda *args: self.input_text_funk())
        self.sys_of_not.trace('w', lambda *args: self.change())



#     def input_text_funk(self):
# # ДЕЛАЙ ЧЕРЕЗ АНАЛИЗ НА РУССКИЕ БУКВЫ
            


# функция создания случайных ключей при старте
    def key_generation(self):
        self.input_bin_key_56 = ''
        temp_key = 0
        while temp_key <7:
            temp_s = ''
            for i in range(8): 
                temp_s = temp_s+str(random.randint(0,1))
            if (48<=int(temp_s, 2)<=57) or (65<=int(temp_s, 2)<=90) or (97<=int(temp_s, 2)<=122) or (192<=int(temp_s, 2)<=255) or (int(temp_s, 2) == 184) or (int(temp_s, 2) == 168):
                self.input_bin_key_56+=temp_s
                temp_key+=1

        a = translate(self.input_bin_key_56, 'b', 's')
        
        c = self.ctrlBit(self.input_bin_key_56)
          
        r = ''
        for i in c:
            r+=str(hex(int(i,2))[2:]).zfill(2)
      
        self.crypt_key_ent.delete(0, tk.END)
        self.crypt_key_ctrl_bit_ent.delete(0, tk.END)
        self.crypt_key_ent.insert(0, a)
        self.crypt_key_ctrl_bit_ent.insert(0, r)

# Эта дичь добавляет контрольные биты к 56 битной строке, принимает на вход строку из 56 бит выдаёт строку из 64 бит
    def ctrlBit(self, str):
        c = [str[i:i+7] for i in range(0, len(str), 7)]
        count = 0
        for i in c:
            temp_sum = 0
            for j in range(7):
                temp_sum+=int(i[j])
            if temp_sum%2 == 1:
                c[count]= c[count]+'1'
                # print(c[count])
                count+=1     
            else:
                c[count]= c[count]+'0'
                # print(c[count])
                count+=1
        return c

#  Функция которая выводит в заданной системе счисления входные данные 
    def change(self):
        if (len(self.entry_text_ent.get()) == 8) and (len(self.crypt_key_ent.get()) >=7):
            if self.sys_of_not.get() == 1:
                self.entry_text_sys_ent.delete(0, tk.END)
                self.entry_text_sys_ent.insert(0, self.entry_text_ent.get())
                self.crypt_key_sys_ent.delete(0, tk.END)
                self.crypt_key_sys_ent.insert(0, self.crypt_key_ent.get())
                output_str = translate(self.crypt_key_ctrl_bit_ent.get(), 'h', 's')
                self.crypt_key_ctrl_bit_sys_ent.delete(0, tk.END)
                self.crypt_key_ctrl_bit_sys_ent.insert(0, output_str)   

            elif self.sys_of_not.get() == 2:
                self.entry_text_sys_ent.delete(0, tk.END)
                self.crypt_key_sys_ent.delete(0, tk.END)
                self.crypt_key_ctrl_bit_sys_ent.delete(0, tk.END)
                os_1 = translate(self.entry_text_ent.get(), 's', 'b')
                if len(self.crypt_key_ent.get())==7:
                    os_2 = translate(self.crypt_key_ent.get(), 's', 'b')
                else:
                    os_2 = translate(self.crypt_key_ent.get(), 'h', 'b')
                os_3 = translate(self.crypt_key_ctrl_bit_ent.get(), 'h', 'b')
                self.entry_text_sys_ent.insert(0, os_1)
                self.crypt_key_sys_ent.insert(0, os_2)
                self.crypt_key_ctrl_bit_sys_ent.insert(0, os_3)
            
            else:
                self.entry_text_sys_ent.delete(0, tk.END)
                self.crypt_key_sys_ent.delete(0, tk.END)
                self.crypt_key_ctrl_bit_sys_ent.delete(0, tk.END)
                os_1 = translate(self.entry_text_ent.get(), 's', 'h')
                if len(self.crypt_key_ent.get())==7:
                    os_2 = translate(self.crypt_key_ent.get(), 's', 'h')
                else:
                    os_2 = translate(self.crypt_key_ent.get(), 'h', 'h')
                os_3 = translate(self.crypt_key_ctrl_bit_ent.get(), 'h', 'h')
                self.entry_text_sys_ent.insert(0, os_1)
                self.crypt_key_sys_ent.insert(0, os_2)
                self.crypt_key_ctrl_bit_sys_ent.insert(0, os_3)
        else:
            self.sys_of_not.set(None)
            mb.showerror('Ошибка', message = 'Не заполнены поля')
            

                












if __name__ == "__main__":
    window = tk.Tk()
    q = engine(window)
    q.mainloop()
