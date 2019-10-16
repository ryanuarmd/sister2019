from greet import Server
import Pyro4

def start_with_ns():
    # --- start 
    # pyro4-ns -n localhost -p 7777

    # --- list
    # pyro4-nsc -n localhost -p 7777 list
    __host = "localhost"
    __port = 7777
    server = Server()
    daemon = Pyro4.Daemon(host = __host)
    ns = Pyro4.locateNS(__host, __port)
    uri_server = daemon.register(server)
    print("URI server : ", uri_server)
    ns.register("server", uri_server)
    daemon.requestLoop()


if __name__ == '__main__':
    start_with_ns()
