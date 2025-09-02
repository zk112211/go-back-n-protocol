import socket
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hmac
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding

#使用os库urandom函数随机生成会话密钥
session_key = os.urandom(16) #使用AES-128算法，使用16位会话密钥
with open('session.key', 'wb') as session_file:
        session_file.write(session_key)  #将session_key保存在session.key文件中


#客户端套接字
def client():
    # 创建套接字对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器
    client_socket.connect(('localhost', 12345))
    print("connect to server.\n")

    #将输入的字符串赋值给original_string
    original_string = input("Please input the message.\n")

    #开始对字符串进行加密
    #创建满足AES加密的填充器
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    #创建一个使用CBC模式对字符串进行AES加密的加密器，其中的b'\x00'是一个可以随意指定的向量
    cipher = Cipher(algorithms.AES(session_key), modes.CBC(b'\x00' * 16)) 
    encryptor = cipher.encryptor()  #加密器
    string = original_string.encode()  #对original_string进行编码，使其满足
    #使用padder对数据进行处理，确保其加密长度与加密算法的块长度相同
    padded_string = padder.update(string) + padder.finalize() 
    #对数据进行加密
    encrypted_string = encryptor.update(padded_string) + encryptor.finalize()
    client_socket.sendall(encrypted_string) #将加密字符串传输给服务端

    # 生成MAC
    hmac_key = b'secret_key'
    h = hmac.HMAC(hmac_key, hashes.SHA256())
    h.update(encrypted_string)
    mac = h.finalize()

    # 将加密字符串和MAC发送给服务器
    client_socket.sendall(mac)

    # 关闭连接
    client_socket.close()



client()