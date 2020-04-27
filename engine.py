import tkinter as tk
from guiDES import gui
from transform import translate
from tkinter import messagebox as mb
import table as tb
import random


class engine(gui):
    def __init__(self, window):
        super().__init__(window)
        self.key_generation()
        self.entry_crypt_1.trace('w', lambda *args: self.control())
        self.entry_crypt_2.trace('w', lambda *args: self.input_symbol_key())
        self.entry_crypt_3.trace('w', lambda *args: self.input_hex_key())
        self.type_of_crypt.trace('w', lambda *args: self.crypt())
        self.sys_of_not.trace('w', lambda *args: self.change())
        self.round_btn.config(command = lambda: self.round_info())

# РАЗДЕЛ ВЫВОДЫ И ВВОДА ДАННЫХ
# 
# 
# 
    def control(self):
        self.entry_text_ent.delete(16, tk.END)
        self.entry_text_sys_ent.delete(0, tk.END)
        self.crypt_key_sys_ent.delete(0, tk.END)
        self.crypt_key_ctrl_bit_sys_ent.delete(0, tk.END)
        if 1 <= self.sys_of_not.get() <= 3:
            self.change()
     
    def input_symbol_key(self):
        self.entry_text_sys_ent.delete(0, tk.END)
        self.crypt_key_sys_ent.delete(0, tk.END)
        self.crypt_key_ctrl_bit_sys_ent.delete(0, tk.END)
        if len(self.crypt_key_ent.get()) == 7:
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
            if translate(t_out, 's', 'h') == '00000000000000':
                self.zero_value = 1
            else:
                self.zero_value = 0
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
        if ((len(self.entry_text_ent.get()) == 8) or (len(self.entry_text_ent.get()) == 16))  and (len(self.crypt_key_ctrl_bit_ent.get()) == 16):
            if self.sys_of_not.get() == 1:
                if len(self.entry_text_ent.get()) == 8:
                    self.entry_text_sys_ent.delete(0, tk.END)
                    self.entry_text_sys_ent.insert(0, self.entry_text_ent.get())
                else:
                    self.entry_text_sys_ent.delete(0, tk.END)
                    self.entry_text_sys_ent.insert(0, translate(self.entry_text_ent.get(), 'h', 's'))
                self.crypt_key_sys_ent.delete(0, tk.END)
                self.crypt_key_sys_ent.insert(0, self.crypt_key_ent.get())
                output_str = translate(self.crypt_key_ctrl_bit_ent.get(), 'h', 's')
                self.crypt_key_ctrl_bit_sys_ent.delete(0, tk.END)
                self.crypt_key_ctrl_bit_sys_ent.insert(0, output_str)   

            elif self.sys_of_not.get() == 2:
                self.entry_text_sys_ent.delete(0, tk.END)
                self.crypt_key_sys_ent.delete(0, tk.END)
                self.crypt_key_ctrl_bit_sys_ent.delete(0, tk.END)
                if len(self.entry_text_ent.get()) == 8:
                    self.entry_text_sys_ent.delete(0, tk.END)
                    self.entry_text_sys_ent.insert(0, translate(self.entry_text_ent.get(), 's', 'b'))
                else:
                    self.entry_text_sys_ent.delete(0, tk.END)
                    self.entry_text_sys_ent.insert(0, translate(self.entry_text_ent.get(), 'h', 'b'))
                if self.zero_value == 0:
                    self.crypt_key_sys_ent.insert(0, translate(self.crypt_key_ent.get(), 's', 'b'))
                else:
                    self.crypt_key_sys_ent.insert(0, translate('00000000000000', 'h', 'b'))
                self.crypt_key_ctrl_bit_sys_ent.insert(0, translate(self.crypt_key_ctrl_bit_ent.get(), 'h', 'b'))
            
            elif self.sys_of_not.get() == 3:
                self.entry_text_sys_ent.delete(0, tk.END)
                self.crypt_key_sys_ent.delete(0, tk.END)
                self.crypt_key_ctrl_bit_sys_ent.delete(0, tk.END)
                if len(self.entry_text_ent.get()) == 8:
                    self.entry_text_sys_ent.delete(0, tk.END)
                    self.entry_text_sys_ent.insert(0, translate(self.entry_text_ent.get(), 's', 'h'))
                else:
                    self.entry_text_sys_ent.delete(0, tk.END)
                    self.entry_text_sys_ent.insert(0, translate(self.entry_text_ent.get(), 'h', 'h'))
                if self.zero_value == 0:
                    self.crypt_key_sys_ent.insert(0, translate(self.crypt_key_ent.get(), 's', 'h'))
                else:
                    self.crypt_key_sys_ent.insert(0, translate('00000000000000', 'h', 'h'))
                self.crypt_key_ctrl_bit_sys_ent.insert(0, translate(self.crypt_key_ctrl_bit_ent.get(), 'h', 'h'))
            else:
                self.entry_text_sys_ent.delete(0, tk.END)
                self.crypt_key_sys_ent.delete(0, tk.END)
                self.crypt_key_ctrl_bit_sys_ent.delete(0, tk.END)
       
# РАЗДЕЛ ШИФРОВАНИЯ ДЕШИФРОВАНИЯ
# 
# 
# 
    def shift(self, strk, n):
        for i in range(n):
            strk.append(strk.pop(0))
        return strk

    def keyPrepare(self):
        input_Key = translate(self.crypt_key_ctrl_bit_ent.get(), 'h', 'b')
        Key1 = []
        gKey = []
        cArray = []
        dArray = []
        readyKey = []
        # Получение ключа 64 бита
        for i in input_Key: Key1.append(int(i))
        # G матрица первоначальной подготовки ключа
        for i in range(56): gKey.append(Key1[tb.gBox[i]-1])
        # Получаем заготовки для сдвигов 
        c0 = gKey[:28]
        d0 = gKey[28:]
        cArray.append(c0)
        dArray.append(d0)
        for i in range(16):
            hKey = []

            tempC = self.shift(cArray[i], tb.shiftBox[i])
            cTemp = ''
            tempD = self.shift(dArray[i], tb.shiftBox[i])
            dTemp = ''
            
            cArray.append(tempC)
            dArray.append(tempD)

            for j in tempC: cTemp+=str(j)
            for k in tempD: dTemp+=str(k)
            tempKey = cTemp+dTemp

            for a in range(48): hKey.append(int(tempKey[tb.hBox[a]-1]))

            readyStrKey = ''
            for y in hKey: readyStrKey+=str(y)
            readyKey.append(readyStrKey)

        return readyKey
        
    def encrypt(self, key):
        if len(self.entry_text_ent.get()) == 8:
            inputData = translate(self.entry_text_ent.get(), 's', 'b')
        else:
            inputData = translate(self.entry_text_ent.get(), 'h', 'b')
        inputPer = []
        rBlock = []
        lBlock = []
        for i in range(64): inputPer.append(int(inputData[tb.ip[i]-1]))
        l0 = inputPer[:32]
        r0 = inputPer[32:]
        rBlock.append(r0)
        lBlock.append(l0)
        for i in range(16):
            e = ''
            temp_r = rBlock[i]
            lBlock.append(rBlock[i])
            for q in range(32): e+=str(temp_r[tb.eBox[q]-1])
            ek = str(bin(int(e,2)^int(key[i],2)))[2:].zfill(48)
            eks = [ek[w:w+6] for w in range(0, 48, 6)]
            s1 = eks[0]
            s2 = eks[1]
            s3 = eks[2]
            s4 = eks[3]
            s5 = eks[4]
            s6 = eks[5]
            s7 = eks[6]
            s8 = eks[7]
            s1_x = int((s1[0]+s1[5]),2)
            s1_y = int((s1[1]+s1[2]+s1[3]+s1[4]),2)

            s2_x = int((s2[0]+s2[5]),2)
            s2_y = int((s2[1]+s2[2]+s2[3]+s2[4]),2)

            s3_x = int((s3[0]+s3[5]),2)
            s3_y = int((s3[1]+s3[2]+s3[3]+s3[4]),2)

            s4_x = int((s4[0]+s4[5]),2)
            s4_y = int((s4[1]+s4[2]+s4[3]+s4[4]),2)

            s5_x = int((s5[0]+s5[5]),2)
            s5_y = int((s5[1]+s5[2]+s5[3]+s5[4]),2)

            s6_x = int((s6[0]+s6[5]),2)
            s6_y = int((s6[1]+s6[2]+s6[3]+s6[4]),2)

            s7_x = int((s7[0]+s7[5]),2)
            s7_y = int((s7[1]+s7[2]+s7[3]+s7[4]),2)

            s8_x = int((s8[0]+s8[5]),2)
            s8_y = int((s8[1]+s8[2]+s8[3]+s8[4]),2)
            
            newS_1 = str(bin(tb.sb1[s1_x][s1_y]))[2:].zfill(4)
            newS_2 = str(bin(tb.sb2[s2_x][s2_y]))[2:].zfill(4)
            newS_3 = str(bin(tb.sb3[s3_x][s3_y]))[2:].zfill(4)
            newS_4 = str(bin(tb.sb4[s4_x][s4_y]))[2:].zfill(4)
            newS_5 = str(bin(tb.sb5[s5_x][s5_y]))[2:].zfill(4)
            newS_6 = str(bin(tb.sb6[s6_x][s6_y]))[2:].zfill(4)
            newS_7 = str(bin(tb.sb7[s7_x][s7_y]))[2:].zfill(4)
            newS_8 = str(bin(tb.sb8[s8_x][s8_y]))[2:].zfill(4)
            pPrepare = newS_1 + newS_2 + newS_3 + newS_4 + newS_5 + newS_6 + newS_7 + newS_8 
            rP = ''
            for z in range(32): rP+=pPrepare[tb.pBox[z]-1]
            tempL = lBlock[i]
            lforXOR = ''
            for f in tempL: lforXOR+=str(f)
            finalR = str(bin(int(lforXOR,2)^int(rP,2)))[2:].zfill(32)
            NewR = []
            for v in finalR: NewR.append(int(v))
            rBlock.append(NewR)
        cryptL = ''
        cryptR = ''
        for i in lBlock[16]: cryptL+=str(i)
        
        for i in rBlock[16]: cryptR+=str(i)
       
        cryptBeforeIPR = cryptR+cryptL
        finalCrypt = ''
        for i in range(64): finalCrypt+=cryptBeforeIPR[tb.ipr[i]-1]
        if len(self.entry_text_ent.get()) == 8:
            return translate(finalCrypt, 'b', 'h'), rBlock, lBlock
        else:
            return translate(finalCrypt, 'b', 's'), rBlock, lBlock
        # return translate(finalCrypt, 'b', 'h'), rBlock, lBlock

    def decrypt(self, key):
        inputData = translate(self.entry_text_ent.get(), 'h', 'b')
        inputPer = []
        rBlock = []
        lBlock = []
        for i in range(64): inputPer.append(int(inputData[tb.ip[i]-1]))
        r0 = inputPer[:32]
        l0 = inputPer[32:]
        rBlock.append(r0)
        lBlock.append(l0)
        for i in range(16):
            e = ''
            temp_l = lBlock[i]
            rBlock.append(lBlock[i])
            for q in range(32): e+=str(temp_l[tb.eBox[q]-1])
            ek = str(bin(int(e,2)^int(key[i],2)))[2:].zfill(48)
            eks = [ek[w:w+6] for w in range(0, 48, 6)]
            s1 = eks[0]
            s2 = eks[1]
            s3 = eks[2]
            s4 = eks[3]
            s5 = eks[4]
            s6 = eks[5]
            s7 = eks[6]
            s8 = eks[7]
            s1_x = int((s1[0]+s1[5]),2)
            s1_y = int((s1[1]+s1[2]+s1[3]+s1[4]),2)

            s2_x = int((s2[0]+s2[5]),2)
            s2_y = int((s2[1]+s2[2]+s2[3]+s2[4]),2)

            s3_x = int((s3[0]+s3[5]),2)
            s3_y = int((s3[1]+s3[2]+s3[3]+s3[4]),2)

            s4_x = int((s4[0]+s4[5]),2)
            s4_y = int((s4[1]+s4[2]+s4[3]+s4[4]),2)

            s5_x = int((s5[0]+s5[5]),2)
            s5_y = int((s5[1]+s5[2]+s5[3]+s5[4]),2)

            s6_x = int((s6[0]+s6[5]),2)
            s6_y = int((s6[1]+s6[2]+s6[3]+s6[4]),2)

            s7_x = int((s7[0]+s7[5]),2)
            s7_y = int((s7[1]+s7[2]+s7[3]+s7[4]),2)

            s8_x = int((s8[0]+s8[5]),2)
            s8_y = int((s8[1]+s8[2]+s8[3]+s8[4]),2)
            
            newS_1 = str(bin(tb.sb1[s1_x][s1_y]))[2:].zfill(4)
            newS_2 = str(bin(tb.sb2[s2_x][s2_y]))[2:].zfill(4)
            newS_3 = str(bin(tb.sb3[s3_x][s3_y]))[2:].zfill(4)
            newS_4 = str(bin(tb.sb4[s4_x][s4_y]))[2:].zfill(4)
            newS_5 = str(bin(tb.sb5[s5_x][s5_y]))[2:].zfill(4)
            newS_6 = str(bin(tb.sb6[s6_x][s6_y]))[2:].zfill(4)
            newS_7 = str(bin(tb.sb7[s7_x][s7_y]))[2:].zfill(4)
            newS_8 = str(bin(tb.sb8[s8_x][s8_y]))[2:].zfill(4)
            
            pPrepare = newS_1 + newS_2 + newS_3 + newS_4 + newS_5 + newS_6 + newS_7 + newS_8 
            lP = ''
            for z in range(32): lP+=pPrepare[tb.pBox[z]-1]
            tempR = rBlock[i]
            rforXOR = ''
            for f in tempR: rforXOR+=str(f)
            finalL = str(bin(int(rforXOR,2)^int(lP,2)))[2:].zfill(32)
            NewL = []
            for v in finalL: NewL.append(int(v))
            lBlock.append(NewL)
        cryptL = ''
        cryptR = ''
        for i in lBlock[16]: cryptL+=str(i)
        
        for i in rBlock[16]: cryptR+=str(i)
        
        cryptBeforeIPR = cryptL+cryptR
        finalCrypt = ''
        for i in range(64): finalCrypt+=cryptBeforeIPR[tb.ipr[i]-1]
        
        return translate(finalCrypt, 'b', 's'), rBlock, lBlock
        
    def crypt(self):
        self.left_block_ent.delete(0, tk.END)
        self.right_block_ent.delete(0, tk.END)
        self.round_key_block_ent.delete(0, tk.END)
        self.round_ent.delete(0, tk.END)
        self.round_ent.insert(0, '0')
        if (self.type_of_crypt.get() == 1) and ((len(self.entry_text_ent.get()) == 8) or (len(self.entry_text_ent.get()) == 16)) and (len(self.crypt_key_ctrl_bit_ent.get()) == 16): 
            self.keyArray_enc = self.keyPrepare()
            encryptText, self.re, self.le = self.encrypt(self.keyArray_enc)
            self.crypt_text_ent.delete(0, tk.END)
            self.crypt_text_ent.insert(0, encryptText)
            self.le.pop(0)
            self.re.pop(0) 
        elif (self.type_of_crypt.get() == 2) and (len(self.entry_text_ent.get()) == 16) and (len(self.crypt_key_ctrl_bit_ent.get()) == 16):
            keyArray = self.keyPrepare()
            self.keyArrayRevers = list(reversed(keyArray))
            decryptText, self.rd, self.ld = self.decrypt(self.keyArrayRevers)
            self.crypt_text_ent.delete(0, tk.END)
            self.crypt_text_ent.insert(0, decryptText)
            self.ld.pop(0)
            self.rd.pop(0)

    def round_info(self):
        if int(self.round_ent.get()) <16:
            if self.type_of_crypt.get() == 1:
                self.left_block_ent.delete(0, tk.END)
                self.right_block_ent.delete(0, tk.END)
                self.round_key_block_ent.delete(0, tk.END)
                temp_counter = int(self.round_ent.get())
                lb1 = ''
                rb1 = ''
                for i in self.le[temp_counter]: lb1+=str(i)
                for i in self.re[temp_counter]: rb1+=str(i)
                self.left_block_ent.insert(0, lb1)
                self.right_block_ent.insert(0, rb1)
                self.round_key_block_ent.insert(0, self.keyArray_enc[temp_counter])
                self.round_ent.delete(0, tk.END)
                self.round_ent.insert(0, str(temp_counter+1))
            elif self.type_of_crypt.get() == 2: 
                self.left_block_ent.delete(0, tk.END)
                self.right_block_ent.delete(0, tk.END)
                self.round_key_block_ent.delete(0, tk.END)
                temp_counter = int(self.round_ent.get())
                lb2 = ''
                rb2 = ''
                for i in self.le[temp_counter]: lb2+=str(i)
                for i in self.re[temp_counter]: rb2+=str(i)
                self.left_block_ent.insert(0, lb2)
                self.right_block_ent.insert(0, rb2)
                self.round_key_block_ent.insert(0, self.keyArrayRevers[temp_counter])
                self.round_ent.delete(0, tk.END)
                self.round_ent.insert(0, str(temp_counter+1))
            else:
                mb.showerror('Ошибка', message = 'Не выбран тип шифрования')
        else:
            self.round_ent.delete(0, tk.END)
            self.round_ent.insert(0, '0')
            self.left_block_ent.delete(0, tk.END)
            self.right_block_ent.delete(0, tk.END)
            self.round_key_block_ent.delete(0, tk.END)

               
if __name__ == "__main__":
    window = tk.Tk()
    q = engine(window)
    q.mainloop()
