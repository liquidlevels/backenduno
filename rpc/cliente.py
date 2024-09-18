from rpc import RPCClient
server = RPCClient('localhost', 9000)
server.connect()
print(server.add(5,6))
print(server.sub(5,6))
print(server.hi())
server.disconnect()
