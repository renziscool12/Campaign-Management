from model.Organizer import Organizer

class OrganizerManager:
    def __init__(self):
        self.organizers = []

    def add_organizer(self, first_name, last_name, email, organization_id):
        organizer = Organizer(first_name, last_name, email, organization_id)
        self.organizers.append(organizer)