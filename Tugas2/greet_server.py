from greet import *
import Pyro4



def start_with_ns():

    #ganti "localhost dengan ip yang akan anda gunakan sebagai server" 

    #name server harus di start dulu dengan  pyro4-ns -n localhost -p 7777

    #gunakan URI untuk referensi name server yang akan digunakan

    #untuk mengecek service apa yang ada di ns, gunakan pyro4-nsc -n localhost -p 7777 list

    _host = "localhost"
    daemon = Pyro4.Daemon(host=_host)
    ns = Pyro4.locateNS(_host,7777)
    x_GreetServer = Pyro4.expose(GreetServer)
    uri_greetserver = daemon.register(x_GreetServer)
    print("URI greet server : ", uri_greetserver)
    ns.register("greetserver", uri_greetserver)
    daemon.requestLoop()





if __name__ == '__main__':

    start_with_ns()
