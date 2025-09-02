import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hmac
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding

with open('session.key','rb') as session_file:
    session_key = session_file.read()

# 服务器端代码
def server():
    # 创建套接字对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server listening 12345")

    # 接受连接
    client_socket, addr = server_socket.accept()
    print("Connection from:", addr)

    # 接收来自客户端的加密字符串和MAC
    encrypted_string = client_socket.recv(16)
    mac = client_socket.recv(1024)

    with open('session.key','rb') as session_file:
        session_key = session_file.read()

    # 解密加密字符串
    cipher = Cipher(algorithms.AES(session_key), modes.CBC(b'\x00' * 16))  #创建解码器
    decryptor = cipher.decryptor()
    decrypted_string = decryptor.update(encrypted_string) + decryptor.finalize() #对客户端信息进行解码
    # 使用去填充器对解密后的数据进行处理
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_string = unpadder.update(decrypted_string) + unpadder.finalize()

    # 验证MAC
    hmac_key = b'secret_key'
    h = hmac.HMAC(hmac_key, hashes.SHA256())
    h.update(encrypted_string)
    try:
        h.verify(mac)
        print("MAC verified")
    except:
        print("MAC verification failed")
        server_socket.close()

    string = unpadded_string.decode()
    # 显示解密后的字符串
    print("Message from client:\n", string)

    # 关闭连接
    server_socket.close()

#启动服务端
server()


