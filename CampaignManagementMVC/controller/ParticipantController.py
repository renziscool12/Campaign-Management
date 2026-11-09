from model.Participant import Participant

class ParticipantManager:
    def __init__(self):
        self.participants = []

    def add_participant(self, first_name, last_name, email, participant_id):
        participant = Participant(first_name, last_name, email, participant_id)
        self.participants.append(participant)