import socket

def port_scanner(target_ip, start_port, end_port):
    print(f"Scanning {target_ip} for open ports...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

def simple_password_cracker(hash, wordlist):
    import hashlib
    with open(wordlist, 'r') as file:
        for word in file.readlines():
            if hashlib.md5(word.strip().encode()).hexdigest() == hash:
                print(f"Password found: {word.strip()}")
                return
    print("Password not found")

if __name__ == "__main__":
    target_ip = "192.168.1.1"
    port_scanner(target_ip, 20, 1024)

    hash_to_crack = "5f4dcc3b5aa765d61d8327deb882cf99"  # MD5 for 'password'
    wordlist = "passwords.txt"
    simple_password_cracker(hash_to_crack, wordlist)
