import cmd
import threading
import time

class Program(cmd.Cmd):
    def do_start(self, line):
        # Bir thread oluşturun
        t = threading.Thread(target=self.start)
        # Thread'i çalıştırın
        t.start()

    def start(self):
        # 10 saniye bekleyin
        time.sleep(10)
        # "hello, world!" yazısını gösterin
        print("hello, world!")
    def do_exit(self, line):
      return True
# Program sınıfını çalıştırın
Program().cmdloop()
