int_print = 20182204
hex_trans = "0123456789abcdef"

def go(num, len):
    if (num == 0):
        return ("0")
    if (num < 1):
        return ("")
    return (go(num / len, len) + hex_trans[int(num % len)])

octal_print = "0o" + go(int_print, 8)
hex_print = "0x" + go(int_print, 16)

##### 아래의 방식으로도 가능 #####
#  octal_print = oct(int_print) #
#  hex_print = hex(int_print)   #
################################

print(int_print)
print(octal_print)
print(hex_print)