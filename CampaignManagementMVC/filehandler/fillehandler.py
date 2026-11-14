class FileHandler:
    def save_file(self, campaigns):
        with open("campaigns.txt", 'a') as file:
            for campaign in campaigns:
                file.write(str(campaign) + "\n")

    def read_file(self):
        try:
            with open("campaigns.txt", 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    def update_file(self, campaigns):
        with open("campaigns.txt", 'w') as file:
            for campaign in campaigns:
                file.write(str(campaign) + "\n")
