from tkinter import *

def euclid(a,b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

def generate_keys(p, q):
    n = p*q # modulus 할 n
    m = (p-1)*(q-1) # p(n)
    e = int(2)
    while e < m:
        if euclid(e,m) == 1:
            break
        else:
            e = e + 1
    w = 1
    while(((e*w)%m)!=1):
        w = w+1
    d = w
    return [(e, n), (d, n)]

def rsa():
    global l2
    p = int(a.get())
    q = int(b.get())
    msg = int(c.get())
    pub_key, priv_key = generate_keys(p, q)
    print('공개키 : ', pub_key)
    print('비밀키 : ', priv_key)
    print('test : ', str(msg))
    e, n = pub_key # 공개키(n, e)
    d, n = priv_key # 비밀키(n, d)
    crypted = (msg ** e) % n
    l2.config(text = crypted)
    return crypted**d % n

def decry():
    b = rsa()
    global l3
    original = b
    l3.config(text = original)

root = Tk()
root.title('RSA 계산기')
l = Label(root, text = '첫번째 P (소수): ')
l.pack()
a = Entry(root)
a.pack()
l = Label(root, text = '두번째 Q (소수): ')
l.pack()
b = Entry(root)
b.pack()
l = Label(root, text = '평문 M (정수):')
l.pack()
c = Entry(root)
c.pack()
f1 = Frame()
f1.pack(side = TOP)
button = Button(f1, text = "암호화", command = rsa)
button.pack(side = LEFT)
button2 = Button(f1, text = "복호화", command = decry)
button2.pack(side = RIGHT)
f2 = Frame()
f2.pack(side = TOP)
l2 = Label(f2, text = '암호된 메시지 : C')
l2.pack(side = LEFT)
l3 = Label(f2, text = '복호된 메시지 : M')
l3.pack(side = RIGHT)

root.mainloop()
