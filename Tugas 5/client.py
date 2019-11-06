import Pyro4
import base64
import json
import sys

namainstance = sys.argv[1]

def get_fileserver_object():
    uri = "PYRONAME:{}@localhost:7777" . format(namainstance)
    fserver = Pyro4.Proxy(uri)
    fserver.setName(namainstance)
    fserver.setPyroObject()
    return fserver

def manageCommand(cmd):
    listCommand = ['list', 'create', 'read', 'update', 'delete', 'help']
    cmdArr = cmd.split(' ')

    if cmdArr[0] == 'exit':
        return ['exit', 'Program closed']
    if cmdArr[0] in listCommand:
        return cmdArr
    elif cmdArr[0] not in listCommand:
        return ['error', 'Command unknown']
    else:
        return None

if __name__=='__main__':
    proxy = get_fileserver_object()
    while True:
        command = input("Type here : ")
        command = manageCommand(command)
        if command[0] == 'create':
            print(proxy.create(command[1],namainstance))
        elif command[0] == 'read':
            print(proxy.read(command[1]))
        elif command[0] == 'update':
            print(proxy.update(command[1],command[2],namainstance))
        elif command[0] == 'delete':
            print(proxy.delete(command[1],namainstance))
        elif command[0] == 'list':
            print(proxy.list())
        elif command[0] == 'help':
            print("List of commands : ")
            print("1. create [filename]")
            print("2. read [filename]")
            print("3. update [filename]")
            print("4. delete [filename]")
            print("5. list")
            print("6. help")
            print("7. exit")
        elif command[0] == 'error':
            print(command[1])
        elif command[0] == 'exit':
            print(command[1])
            exit()