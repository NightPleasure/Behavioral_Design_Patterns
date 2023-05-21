class Event:
    def __init__(self, name):
        self.name = name

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_event(self, event):
        pass

class NotificationHandler(Handler):
    def handle_event(self, event):
        if event.name == 'notification':
            print("Notificare: Un eveniment a fost primit.")
        elif self.successor is not None:
            self.successor.handle_event(event)

class SubscriptionHandler(Handler):
    def handle_event(self, event):
        if event.name == 'subscription':
            print("Abonament: Un utilizator s-a abonat la evenimente.")
        elif self.successor is not None:
            self.successor.handle_event(event)

class LoggingHandler(Handler):
    def handle_event(self, event):
        print("Jurnal: Evenimentul a fost înregistrat.")
        if self.successor is not None:
            self.successor.handle_event(event)

notification_handler = NotificationHandler()
subscription_handler = SubscriptionHandler(notification_handler)
logging_handler = LoggingHandler(subscription_handler)

event1 = Event('notification')
logging_handler.handle_event(event1)

event2 = Event('subscription')
logging_handler.handle_event(event2)

event3 = Event('other')
logging_handler.handle_event(event3)
