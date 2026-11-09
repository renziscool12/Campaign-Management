from controller.CampaignController import CampaignManager
from controller.ParticipantController import ParticipantManager
from controller.OrganizerController import OrganizerManager
from view.menu import CampaignView

def main():
    campaign_manager = CampaignManager()
    organizer_manager = OrganizerManager()
    participant_manager = ParticipantManager()

    view = CampaignView(campaign_manager, organizer_manager, participant_manager)
    view.display_menu()

if __name__ == "__main__":
    main()