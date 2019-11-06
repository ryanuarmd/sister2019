import os
import Pyro4

class FileServer(object):
    def __init__(self):
        self.name = None
        self.pyro_objects = dict()
        self.pyro_name_list = ["fileserver1","fileserver2","fileserver3"]

    def setPyroObject(self):
        i = 0
        for x in self.pyro_name_list:
            if self.name == x:
                pass
            else:
                self.pyro_objects[i] = Pyro4.Proxy("PYRONAME:{}@localhost:7777".format(x))
                self.pyro_objects[i].setName(x)
                i = i + 1

    def getPyroObjects(self):
        return self.pyro_objects

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def create_return_message(self,kode='000',message='kosong',data=None):
        return dict(kode=kode,message=message,data=data)

    def list(self):
        print("list ops")
        try:
            daftarfile = []
            for x in os.listdir():
                if x[0:4]=='FFF-':
                    daftarfile.append(x[4:])
            return self.create_return_message('200',daftarfile)
        except:
            return self.create_return_message('500','Error')

    def create(self, name='filename000', instance='none'):
        if instance == 'none':
            return self.create_return_message('400','OK','Bad Request Error')

        if self.name == instance:
            for x in range(0,len(self.pyro_objects)):
                self.pyro_objects[x].create(name,self.name)

        nama='FFF-{}' . format(name)
        print("{}: CREATE ops {} FROM {} instance" . format(self.name, name, instance))
        try:
            if os.path.exists(name):
                return self.create_return_message('102', 'OK','File Exists')
            f = open(nama,'wb',buffering=0)
            f.close()
            return self.create_return_message('100','OK')
        except:
            return self.create_return_message('500','Error')

    def read(self,name='filename000'):
        nama='FFF-{}' . format(name)
        print("read ops {}" . format(self.name,name))
        try:
            if not os.path.exists(nama):
                return self.create_return_message('404', 'OK', 'File Not Found')
            f = open(nama,'r+b')
            contents = f.read().decode()
            f.close()
            return self.create_return_message('101','OK',contents)
        except:
            return self.create_return_message('500','Error')

    def update(self,name='filename000',content='',instance='none'):
        if instance == 'none':
            return self.create_return_message('400', 'OK', 'Bad Request Error')

        if self.name == instance:
            for x in range(0, len(self.pyro_objects)):
                self.pyro_objects[x].update(name, content, self.name)

        nama='FFF-{}' . format(name)
        print("{}: UPDATE ops {} FROM {} instance".format(self.name, nama, instance))

        if (str(type(content))=="<class 'dict'>"):
            content = content['data']
        try:
            if not os.path.exists(nama):
                return self.create_return_message('404', 'OK', 'File Not Found')
            f = open(nama,'w+b')
            f.write(content.encode())
            f.close()
            return self.create_return_message('101','OK')
        except Exception as e:
            return self.create_return_message('500','Error',str(e))

    def delete(self,name='filename000',instance='none'):
        if instance == 'none':
            return self.create_return_message('400', 'OK', 'Bad Request Error')

        if self.name == instance:
            for x in range(0, len(self.pyro_objects)):
                self.pyro_objects[x].delete(name, instance)

        nama = 'FFF-{}'.format(name)
        print("{}: DELETE ops {} FROM {} instance".format(self.name, nama, instance))
        try:
            os.remove(nama)
            return self.create_return_message('101','OK')
        except:
            return self.create_return_message('500','Error')