import threading

class EmailThread(threading.Thread):
    def __init__(self,email):
        threading.Thread.__init__(self)
        self.email_obj = email
    def run(self):
        self.email_obj.send()