
from datetime import datetime

class CampaignView:
    def __init__(self, campaign_controller, organization_controller, participant_controller):
        self.campaign_controller = campaign_controller
        self.organization_controller = organization_controller
        self.participant_controller = participant_controller

    def manage_organizers(self):
       first_name = input("Enter organizer's first name: ")
       last_name = input("Enter organizer's last name: ")
       email = input("Enter organizer's email: ")
       organization_id = input("Enter organization ID: ")

       self.organization_controller.add_organizer(first_name, last_name, email, organization_id)
       print("Organizer added successfully.")

    def manage_participants(self):
        first_name = input("Enter participant's first name: ")
        last_name = input("Enter participant's last name: ")
        email = input("Enter participant's email: ")
        participant_id = input("Enter participant ID: ")

        self.participant_controller.add_participant(first_name, last_name, email, participant_id)
        print("Participant added successfully.")

    def create_campaign(self):
        campaign_id = input("Enter campaign ID: ")
        campaign_name = input("Enter campaign name: ")
        description = input("Enter campaign description: ")
        start_date = datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
        end_date = datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d")

        self.campaign_controller.add_campaign(campaign_id, campaign_name, description, start_date, end_date)
        print("Campaign created successfully.")

    def view_campaigns(self):
        campaigns = self.campaign_controller.get_campaigns()

        if not campaigns or isinstance(campaigns, str):
            print("No campaigns available.")
            return

        for campaign in campaigns:
            print(campaign)

    def update_campaign(self):
        campaign_id = input("Enter campaign ID to update: ")
        campaign_name = input("Enter new campaign name (leave blank to keep current): ")
        description = input("Enter new description (leave blank to keep current): ")

        start_input = input("Enter new start date (YYYY-MM-DD) (leave blank to keep current): ")
        end_input = input("Enter new end date (YYYY-MM-DD) (leave blank to keep current): ")

        start_date = datetime.strptime(start_input, "%Y-%m-%d") if start_input else None
        end_date = datetime.strptime(end_input, "%Y-%m-%d") if end_input else None

        self.campaign_controller.update_campaign(
            campaign_id, campaign_name, description, start_date, end_date
        )

    def delete_campaign(self):
        campaign_id = input("Enter campaign ID to delete: ")
        self.campaign_controller.delete_campaign(campaign_id)

    def display_menu(self):
        while True:
            print("\nCampaign Management System")
            print("1. Create Campaign")
            print("2. View Campaigns")
            print("3. Update Campaign")
            print("4. Delete Campaign")
            print("5. Manage Organizers")
            print("6. Manage Participants")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_campaign()
            elif choice == '2':
                self.view_campaigns()
            elif choice == '3':
                self.update_campaign()
            elif choice == '4':
                self.delete_campaign()
            elif choice == '5':
                self.manage_organizers()
            elif choice == '6':
                self.manage_participants()
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
