import datetime

class Event:
    def __init__(self, title, date, description):
        self.title = title
        self.date = date
        self.description = description

class EventMemento:
    def __init__(self, event):
        self.title = event.title
        self.date = event.date
        self.description = event.description

class EventPlanner:
    def __init__(self):
        self.events = []
        self.history = []

    def create_event(self, title, date, description):
        event = Event(title, date, description)
        self.events.append(event)

    def get_event(self, index):
        return self.events[index]

    def save_event_state(self, index):
        event = self.events[index]
        memento = EventMemento(event)
        self.history.append(memento)

    def restore_event_state(self, index):
        event = self.events[index]
        memento = self.history.pop()
        event.title = memento.title
        event.date = memento.date
        event.description = memento.description

    def print_events(self):
        for event in self.events:
            print(f"Title: {event.title}")
            print(f"Date: {event.date}")
            print(f"Description: {event.description}")
            print("-----------------------")

planner = EventPlanner()

planner.create_event("Event 1", datetime.datetime(2023, 5, 1), "Description 1")
planner.create_event("Event 2", datetime.datetime(2023, 5, 5), "Description 2")
planner.create_event("Event 3", datetime.datetime(2023, 5, 10), "Description 3")

planner.save_event_state(1)

event2 = planner.get_event(1)
event2.title = "Updated Event 2"
event2.date = datetime.datetime(2023, 5, 8)
event2.description = "Updated Description 2"

planner.restore_event_state(1)

planner.print_events()
