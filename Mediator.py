import time

class TrafficMediator:
    def __init__(self):
        self.semafoare = {}

    def register_semafor(self, id, semafor):
        self.semafoare[id] = semafor

    def request_change(self, id, state):
        for semafor_id, semafor in self.semafoare.items():
            if semafor_id != id:
                semafor.change_state(state)

class Semafor:
    def __init__(self, id, mediator):
        self.id = id
        self.mediator = mediator
        self.state = "RED"

    def change_state(self, state):
        self.state = state
        print(f"Semaforul {self.id} a fost setat la starea {self.state}")

        if self.state == "GREEN":
            self.mediator.request_change(self.id, "RED")

mediator = TrafficMediator()

semafor1 = Semafor("S1", mediator)
mediator.register_semafor("S1", semafor1)

semafor2 = Semafor("S2", mediator)
mediator.register_semafor("S2", semafor2)


semafor1.change_state("GREEN")

time.sleep(3)

semafor2.change_state("GREEN")
