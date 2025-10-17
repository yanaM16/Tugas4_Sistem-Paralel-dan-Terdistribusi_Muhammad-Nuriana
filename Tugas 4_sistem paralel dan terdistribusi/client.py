import socket


HOST = '192.168.0.21'  
PORT = 1234        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    print(f"Mencoba terhubung ke server {HOST}:{PORT}...")
    s.connect((HOST, PORT))
    print("Berhasil terhubung ke server!\n")
    
    while True:
        pesan = input("Ketik pesan (atau 'exit' untuk keluar): ")
        
        if pesan.lower() == 'exit':
            print("Menutup koneksi...")
            break
        
        s.sendall(pesan.encode('utf-8'))
        
        data = s.recv(1024)
        
        balasan = data.decode('utf-8')
        print(f"Balasan dari server: {balasan}\n")
    
    print(" Koneksi ditutup.")