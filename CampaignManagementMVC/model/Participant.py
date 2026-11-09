from model.Person import Person

class Participant(Person):
    def __init__(self, first_name, last_name, email, participant_id):
        super().__init__(first_name, last_name, email)
        self.participant_id = participant_id

    @property
    def participant_id(self):
        return self._participant_id

    @participant_id.setter
    def participant_id(self, value):
        self._participant_id = value