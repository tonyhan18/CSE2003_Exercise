## error section
fp_r = open(".L_In.txt",'r')
fp_w = open(".L_Out.txt","w")
line = int(fp_r.readline())
charOne = ord("A")
ans = 0
print("index = ",line,file=fp_w)

for s in fp_r:
    num = list(int(x) for x in s.split())
    ans += num[2]
    print(chr(charOne),"=",num, file = fp_w)
    charOne += 1
print("A[2] + B[2] =", ans, file = fp_w, end = "")

fp_r.close()
fp_w.close()
    