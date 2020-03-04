import os
import sys
import random
import socket
import select
import datetime
import threading

lock = threading.RLock(); os.system('cls' if os.name == 'nt' else 'clear')

def real_path(file_name):
    return os.path.dirname(os.path.abspath(__file__)) + file_name

def filter_array(array):
    for i in range(len(array)):
        array[i] = array[i].strip()
        if array[i].startswith('#'):
            array[i] = ''

    return [x for x in array if x]

def colors(value):
    patterns = {
        'R1' : '\033[31;1m', 'R2' : '\033[31;2m',
        'G1' : '\033[33;1m', 'Y1' : '\033[31;1m',
        'P1' : '\033[35;1m', 'CC' : '\033[0;32m',
        'P2' : '\033[36;1m', 'C1' : '\033[30;1m'
    }

    for code in patterns:
        value = value.replace('[{}]'.format(code), patterns[code])

    return value

def log(value, status='', color=''):
    value = colors('{color}[{time}] [P2]{color}{status} [G1]{color}{value}[CC]'.format(
        time=datetime.datetime.now().strftime('%H:%M'),
        value=value,
        color=color,
        status=status
    ))
    with lock: print(value)

def log_replace(value, status='Inject', color=''):
    value = colors('{}{} ({})        [P1]\r'.format(color, status, value))
    with lock:
        sys.stdout.write(value)
        sys.stdout.flush()

class inject(object):
    def __init__(self, inject_host, inject_port):
        super(inject, self).__init__()

        self.inject_host = str(inject_host)
        self.inject_port = int(inject_port)

    def log(self, value, color='[G1]'):
        log(value, color=color)

    def start(self):
        try:
            socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_server.bind((self.inject_host, self.inject_port))
            socket_server.listen(1)
            frontend_domains = open(real_path('/.https___axisnet.id_.ehi')).readlines()
            frontend_domains = filter_array(frontend_domains)
            if len(frontend_domains) == 0:
                self.log(' Domains not found. tolong datang kerumah ewinz bawa sebungkus surya16', color='G1')
                return
            self.log(' [P1]hari ini bisa jadi terakhir HIDUP' '[G1]\nLocal Host :127.0.0.1\nLocal Port :8080\nmantaps' '[CC]\n jalankan Psiphon jika ingin merubah\nKouta game jadi reguler!!!'.format(self.inject_host, self.inject_port),color='[R1]')
            while True:
                socket_client, _ = socket_server.accept()
                socket_client.recv(4096)
                domain_fronting(socket_client, frontend_domains).start()
        except Exception as exception:
            self.log('ERROR!!! anda kurang banyak  sedekah'.format(self.inject_host, self.inject_port), color='[R1]')

            
class domain_fronting(threading.Thread):
    def __init__(self, socket_client, frontend_domains):
        super(domain_fronting, self).__init__()

        self.frontend_domains = frontend_domains
        self.socket_tunnel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_client = socket_client
        self.buffer_size = 1028
        self.daemon = True

    def log(self, value, status='', 
    color=''):
        log(value, status=status, color=color)

    def handler(self, socket_tunnel, socket_client, buffer_size):
        sockets = [socket_tunnel, socket_client]
        timeout = 0
        while True:
            timeout += 2
            socket_io, _, errors = select.select(sockets, [], sockets, 3)
            if errors: break
            if socket_io:
                for sock in socket_io:
                    try:
                        data = sock.recv(buffer_size)
                        if not data: break
                        # SENT -> RECEIVED
                        elif sock is socket_client:
                            socket_tunnel.sendall(data)
                        elif sock is socket_tunnel:
                            socket_client.sendall(data)
                        timeout = 0
                    except: break
            if timeout == 20: break

    def run(self):
        try:
            self.proxy_host_port = random.choice(self.frontend_domains).split(':')
            self.proxy_host = self.proxy_host_port[0]
            self.proxy_port = self.proxy_host_port[1] if len(self.proxy_host_port) >= 3 and self.proxy_host_port[1] else '443'
            self.log('[Y1]lost connection' '[C1]-cepat Taubat oii' '[Y1] reconeg'.format(self.proxy_host, self.proxy_port),color='[C1]')
            self.socket_tunnel.connect((str(self.proxy_host), int(self.proxy_port)))
            self.socket_client.sendall(b'HTTP/1.1 200 OK\r\n\r\n')
            self.handler(self.socket_tunnel, self.socket_client, self.buffer_size)
            self.socket_client.close()
            self.socket_tunnel.close()
            self.log('[P2]Sedekah oii--!!' '[CC] Connection sukses' '[P2]-''[CC] HTTP/1.1 200' '[CC] OK'.format(self.proxy_host, self.proxy_port),color='[CC]')
           

        except OSError:
            self.log('Connection error', color='[Y1]')
        except TimeoutError:
            self.log('{} not responding'.format(self.proxy_host), color='[CC]')

G = '\033[1;33m'
R = '\033[31;1m'
C = '\033[0;32m'
print(colors('\n'.join([
          '[P1]     >>>>>>>WELCOME GRETONGERS INDONESIA<<<<<<\n'
     
          '[P2]       >>>>>>>>>PUTRA BORNEO  EWINZ<<<<<<<<<\n'
      
          '[C1]           >>JADILAH ORANG yang TAQWA <<\n'
      ])))
print(colors('\n'.join([
          '[Y1]     >>kurangi lah kebiasan anda pegang Gawai<<\n'
      ])))
print(colors('\n'.join([
          '                  Baca! Deskripsi \n' 
     
     
          '[CC]                  PAKAI PSIPHON YA\n'      
      
          '            SET SESUAI HOST&PORT DIBAWAH\n'

       ])))
print(colors('[C1]\n'.join([
        '[G1]*Script   :Axis game','[CC]'
        
        '[G1]*Oprek   :ewinz bungas','[CC]'
        
        '[G1]*FROM   :patigan TEXAS ','[CC]' 
        '[G1]*REQ scrip :call me ','[CC]' 

        '[C1]*******Tiup api digunung madang,**********','[C1]' 

        '******abu abunya  diHAMBURKAN.************','[C1]' 

        '*****Hakikat hati dari semenjak Bujang,***','[C1]' 

        '****JANDA JANDA nya tetap di naNtikan.****','[C1]' 

        '    #################################','[CC]' 
        
    ])))
print(colors('[P1]* Script generated by eWinz alpatigani Apps Inc. *'))
 
 
 
if __name__ == '__main__':
    
    
   
    
    inject('127.0.0.1', '8080').start()

