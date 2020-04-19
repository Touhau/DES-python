# по итогу один хер пришлось писать, короче функция меняет входную строку в одной системе отображения в другую, sys1 = это в какой пришло, 
# sys2 = соответственно в какой ушло
# ключи для sys1 sys2 - 'b' - двоичка, 's'  - символьная, 'h' - шестадцатиричная
# битовая строку которую запихиваешь должна делиться на 8
# шестнадцатиричная строка которую запихиваешь должна делиться на 2
# вроде всё
# 
def translate(strl, sys1, sys2):
# из двоичной в любую
    if sys1 == 'b':
        if sys2 == 'b':
            return strl
        elif sys2 == 'h':
            out_1 = ''
            temp_1 = [strl[i:i+8] for i in range(0, len(strl), 8)]
            for i in temp_1:
                out_1+=str(hex(int(i,2))[2:]).zfill(2)
            return out_1
        else:
            out_2 = ''
            temp_2 = [strl[i:i+8] for i in range(0, len(strl), 8)]
            for i in temp_2:
                temp_3 =int(i,2)
                if (48<=temp_3<=57) or (65<=temp_3<=90) or (97<=temp_3<=122):
                    out_2+=chr(temp_3)
                elif 192<=temp_3<=255:
                    out_2+=chr(temp_3+848)
                elif temp_3 == 168:
                    out_2+='Ё'
                else:
                    out_2+='ё'
            return out_2
# Перевод из симовольной в любую
    elif sys1 == 's':
        if sys2 == 's':
            return strl
        elif sys2 == 'b':
            out_3 = ''
            for i in strl:
                if 1040<=ord(i)<=1103:
                    out_3+=str(bin(ord(i)-848))[2:].zfill(8)
                elif ord(i) == 1105:
                    out_3+='10111000'
                elif ord(i) == 1025:
                    out_3+='10101000'
                else:
                    out_3+=str( bin (   ord (i) )   )[2:].zfill(8)
            return out_3
        else:
            out_4 = ''
            for i in strl:
                if 1040<=ord(i)<=1103:
                    out_4+=str(hex(ord(i)-848))[2:].zfill(2)
                elif ord(i) == 1105:
                    out_4+='b8'
                elif ord(i) == 1025:
                    out_4+='a8'
                else:
                    out_4+=str(hex(ord(i)))[2:].zfill(2)
            return out_4
#  Из 16-ричной в любую
    else:
        if sys2 == 'h':
            return strl
        elif sys2 == 's':
            out_5 = ''
            for i in range(0, len(strl), 2):
                temp_4 = strl[i:i+2]
                temp_5 = int(temp_4, 16)
                if 192<=temp_5<=255:
                    out_5+=chr(temp_5+848)
                elif temp_5 == 168:
                    out_5+='Ё'
                elif temp_5 == 184:
                    out_5+='ё'
                else:
                    out_5+=chr(temp_5)
            return out_5
        else:
            out_6 = ''
            for i in range(0, len(strl), 2):
                temp_6 = strl[i:i+2] 
                out_6+=str(bin(int(temp_6, 16)))[2:].zfill(8)
            return out_6
