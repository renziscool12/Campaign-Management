from model.Person import Person

class Organizer(Person):
    def __init__(self, first_name, last_name, email, organization_id):
        super().__init__(first_name, last_name, email)
        self.organization_id = organization_id

    @property
    def organization_id(self):
        return self._organization_id

    @organization_id.setter
    def organization_id(self, value):
        self._organization_id = value