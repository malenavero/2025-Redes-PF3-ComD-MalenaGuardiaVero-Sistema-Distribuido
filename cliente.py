# cliente.py
import socket

def run_client():
    HOST = '127.0.0.1'  # El host del servidor
    PORT = 9999         # El puerto del servidor

    # Creamos el socket del cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Nos conectamos al servidor
        client_socket.connect((HOST, PORT))
        print(f"[CLIENTE] Conectado al servidor en {HOST}:{PORT}")

        # Enviamos una tarea al servidor (la va a capitalizar)
        tarea = "Esta es un tarea De PruEba"
        client_socket.sendall(tarea.encode('utf-8'))
        print(f"[CLIENTE] Tarea enviada: {tarea}")

        # Recibimos el resultado del servidor
        data_recibida = client_socket.recv(1024)
        resultado = data_recibida.decode('utf-8')
        print(f"[CLIENTE] Resultado recibido: {resultado}")

    except socket.error as e:
        print(f"[CLIENTE] Error de socket: {e}")
    finally:
        # Cerramos la conexión
        client_socket.close()
        print("[CLIENTE] Conexión cerrada.")

if __name__ == "__main__":
    run_client()