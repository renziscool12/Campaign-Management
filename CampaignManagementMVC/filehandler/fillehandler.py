class FileHandler:
    def save_file(self, campaign):
        file = open("campaigns.txt", 'a')
        file.write(str(campaign))
        file.close()