from Crypto.Cipher import AES
from getpass import getpass

class NasPass(object):
    """ Hideout for NAS user password.
    Based on CLicS """

    def __init__(self):        
        self.secret = AES.new('VerYStUpiD435Key')

    def encryptPassword(self, passwd):
        plexi16 = len(passwd)%16
        if plexi16 <> 0:
            while plexi16 < 16:
                passwd = passwd + '\0'
                plexi16 += 1
        enc = self.secret.encrypt(passwd)
        return enc

    def decryptPassword(self, passwd):
        enc = self.secret.decrypt(passwd)
        endIndex = enc.find('\0')
        if endIndex == -1:
            return enc
        else:
            return enc[:endIndex]


if __name__ == '__main__':
    import sys

    secret = NasPass()
    paintextpass = getpass("Provide NAS password ")
    encPWD = secret.encryptPassword(paintextpass)
    file = open("passwd.bin", "wb")
    file.write(encPWD)
    file.close
    print "Password file passwd.bin was created in current path."