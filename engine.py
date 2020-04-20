import tkinter as tk
from guiDES import gui
from transform import translate
from tkinter import messagebox as mb
import random


class engine(gui):
    def __init__(self, window):
        super().__init__(window)
        self.key_generation()
        self.entry_crypt_1.trace('w', lambda *args: self.control())
        self.entry_crypt_2.trace('w', lambda *args: self.input_symbol_key())
        self.entry_crypt_3.trace('w', lambda *args: self.input_hex_key())
        self.sys_of_not.trace('w', lambda *args: self.change())


    def control(self):
        self.entry_text_ent.delete(8, tk.END)
        self.entry_text_sys_ent.delete(0, tk.END)
        self.crypt_key_sys_ent.delete(0, tk.END)
        self.crypt_key_ctrl_bit_sys_ent.delete(0, tk.END)
        if 1 <= self.sys_of_not.get() <= 3:
            self.change()
            
    def input_symbol_key(self):
        self.entry_text_sys_ent.delete(0, tk.END)
        self.crypt_key_sys_ent.delete(0, tk.END)
        self.crypt_key_ctrl_bit_sys_ent.delete(0, tk.END)
        if len(self.crypt_key_ent.get()) >= 7:
            temp = translate(self.crypt_key_ent.get(), 's', 'b')
            temp = temp[:56]
            temp_1 = self.ctrlBit(temp)
            t_out = ''
            for i in temp_1:
                t_out+=str(hex(int(i,2))[2:]).zfill(2)
            self.crypt_key_ctrl_bit_ent.delete(0, tk.END)
            self.crypt_key_ent.delete(7, tk.END)
            self.crypt_key_ctrl_bit_ent.insert(0, t_out)
        if 1 <= self.sys_of_not.get() <= 3:
            self.change()

    def input_hex_key(self):

        self.entry_text_sys_ent.delete(0, tk.END)
        self.crypt_key_sys_ent.delete(0, tk.END)
        self.crypt_key_ctrl_bit_sys_ent.delete(0, tk.END)

        if len(self.crypt_key_ctrl_bit_ent.get()) == 16:
            t_out = self.ctrlBitReverse(self.crypt_key_ctrl_bit_ent.get())
            self.crypt_key_ent.delete(0, tk.END)
            self.crypt_key_ent.insert(0, t_out)
            self.crypt_key_ctrl_bit_ent.delete(16, tk.END)
        if 1 <= self.sys_of_not.get() <= 3:
            self.change()
        
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

# Эта дичь добавляет контрольные биты к 56 битной строке, принимает на вход строку из 56 бит выдаёт строку из массив из строк по 8 бит 
    def ctrlBit(self, strk):
        c = [strk[i:i+7] for i in range(0, len(strk), 7)]
        count = 0
        for i in c:
            temp_sum = 0
            for j in range(7):
                temp_sum+=int(i[j])
            if temp_sum%2 == 1:
                c[count]= c[count]+'0'   
                count+=1     
            else:
                c[count]= c[count]+'1'
                count+=1
        return c

# Реверс 64 битной строки в 56 битную путём убирания контрольных битов, принимает строку из 16 16-ричных символов выдаёт строку из 7 символов 
    def ctrlBitReverse(self, strk):
        temp = translate(strk, 'h', 'b')
        b = [temp[i:i+8] for i in range(0, 64, 8)]
        
        c = ''
        for i in b:
            c+=i[0:7]
            
        c1 = translate(c, 'b', 's')
        return c1

#  Функция которая выводит в заданной системе счисления входные данные 
    def change(self):
        if (len(self.entry_text_ent.get()) == 8) and (len(self.crypt_key_ent.get()) == 7) and (len(self.crypt_key_ctrl_bit_ent.get()) == 16):
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
            
            elif self.sys_of_not.get() == 3:
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
                self.entry_text_sys_ent.delete(0, tk.END)
                self.crypt_key_sys_ent.delete(0, tk.END)
                self.crypt_key_ctrl_bit_sys_ent.delete(0, tk.END)
       
            
            

                
if __name__ == "__main__":
    window = tk.Tk()
    q = engine(window)
    q.mainloop()
