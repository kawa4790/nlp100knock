# 08.暗号文
import re
def cipher(text):
    repatter = re.compile('[a-z]')
    temp = ""
    for ch in text:
        if re.match(repatter, ch):
            ch = chr(219 - ord(ch))
        temp += ch
    return temp

encode = cipher("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")
print("暗号化:",encode)
decode = cipher(encode)
print("復号化:",decode)