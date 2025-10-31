# servidor.py
import socket
import threading
import time

# Vamos a generar un worker para cada cliente que se conecte.
def handle_client(conn, addr):
    print(f"[NUEVO WORKER] Conectado con {addr}")

    try:
        # Recibimos la tarea del cliente
        data = conn.recv(1024)
        if not data:
            print(f"[WORKER] Cliente {addr} se desconectó.")
            return

        tarea_recibida = data.decode('utf-8')
        print(f"[WORKER] Tarea recibida de {addr}: {tarea_recibida}")

        # Procesamos la tarea (ejemplo: ponerla en mayúsculas)
        # Le agregamos un tiempo para que nos de tiempo de probar la concurrencia
        print(f"[WORKER] {addr} procesando tarea... (tardará 5 seg)")
        time.sleep(5) 
        resultado = tarea_recibida.upper()

        # Enviamos el resultado de vuelta
        conn.sendall(resultado.encode('utf-8'))
        print(f"[WORKER] Resultado enviado a {addr}")

    except socket.error as e:
        print(f"Error con {addr}: {e}")
    finally:
        # Cerramos la conexión con ese cliente
        conn.close()
        print(f"[WORKER] Conexión con {addr} cerrada.")

# Iniciamos el servidor
def start_server():
    HOST = '127.0.0.1'  # 'localhost'
    PORT = 9999

    # CReamos el socket del servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Los amarramos a la dirección y puerto
    server_socket.bind((HOST, PORT))

    # Ponemos el servidor a escuchar conexiones
    server_socket.listen()
    print(f"[SERVIDOR] Escuchando en {HOST}:{PORT}")

    while True:
        # Aceptamos nueva conexión de un cliente
        #    conn = el socket del cliente
        #    addr = la dirección (IP, puerto) del cliente
        conn, addr = server_socket.accept()
        
        # Se delega a un worker la atención de este cliente:
        worker_thread = threading.Thread(target=handle_client, args=(conn, addr))
        worker_thread.start()
        print(f"[SERVIDOR] Workers activos: {threading.active_count() - 1}")

# --- Iniciar el servidor ---
if __name__ == "__main__":
    start_server()