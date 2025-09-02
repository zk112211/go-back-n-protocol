# TLS Secure Communication Project

This is a Python-based TLS (Transport Layer Security) secure communication project that implements encrypted communication between client and server.

## Project Features

- **AES-128 Encryption**: Uses AES-128 algorithm for data encryption
- **CBC Mode**: Adopts Cipher Block Chaining mode to ensure encryption security
- **HMAC Verification**: Uses HMAC-SHA256 for message authentication code verification
- **PKCS7 Padding**: Implements standard data padding mechanism
- **Session Key Management**: Dynamically generates and manages session keys

## Project Structure

```
TLSpj/
├── client.py          # Client program
├── server.py          # Server program
├── session.key        # Session key file (generated at runtime)
└── README.md          # Project documentation
```

## Installation Requirements

### System Requirements
- Python 3.6+
- macOS/Linux/Windows

### Dependencies
```bash
pip install cryptography
```

## Usage

### 1. Start Server
```bash
python server.py
```
The server will listen for connections on local port 12345.

### 2. Start Client
```bash
python client.py
```
The client will connect to the server and prompt for a message to send.

### 3. Communication Flow
1. Client generates a random session key
2. Client inputs a message and performs AES encryption
3. Generates HMAC message authentication code
4. Sends encrypted data and MAC to server
5. Server verifies MAC and decrypts the message
6. Displays the decrypted original message

## Technical Implementation

### Encryption Algorithm
- **Symmetric Encryption**: AES-128
- **Encryption Mode**: CBC (Cipher Block Chaining)
- **Padding Method**: PKCS7
- **Key Length**: 128 bits

### Security Features
- **Message Integrity**: HMAC-SHA256 verification
- **Key Management**: Generates new random key for each session
- **Vector Initialization**: Uses zero vector as IV for CBC mode

## Important Notes

- This project is for learning and demonstration purposes only
- Production environments should use more secure key exchange mechanisms
- Recommended to run in controlled test environments

## License

This project is for educational use only.

## Contributing

Welcome to submit Issues and Pull Requests to improve the project.
