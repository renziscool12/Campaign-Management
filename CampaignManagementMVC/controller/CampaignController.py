from CampaignManagementMVC.model.campaign import Campaign
from CampaignManagementMVC.filehandler.fillehandler import FileHandler

class CampaignManager:
    def __init__(self):
        self.campaigns = []
        self.file_handler = FileHandler()

    def add_campaign(self, campaign_id, campaign_name, description, start_date, end_date):
        campaign = Campaign(campaign_id, campaign_name, description, start_date, end_date)
        self.campaigns.append(campaign)
        self.file_handler.save_file(self.campaigns)

    def get_campaigns(self):
        if not self.campaigns:
            return "Campaign not found."
        return self.campaigns

    def update_campaign(self, campaign_id, campaign_name=None, description=None, start_date=None, end_date=None):
        for campaign in self.campaigns:
            if campaign.campaign_id == campaign_id:
                if campaign_name:
                    campaign.campaign_name = campaign_name
                if description:
                    campaign.description = description
                if start_date:
                    campaign.start_date = start_date
                if end_date:
                    campaign.end_date = end_date

                self.file_handler.update_file(self.campaigns)
                return "Campaign updated successfully."

        return "Campaign not found."


    def delete_campaign(self, campaign_id):
        for campaign in self.campaigns:
            if campaign.campaign_id == campaign_id:
                self.campaigns.remove(campaign)
                self.file_handler.update_file(self.campaigns)
                return "Campaign deleted successfully."
            
        return "Campaign not found."
