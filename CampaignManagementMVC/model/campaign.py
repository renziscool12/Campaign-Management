class Campaign:
    def __init__(self,campaign_id, campaign_name, description, start_date, end_date):
        self.campaign_id = campaign_id
        self.campaign_name = campaign_name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value

    @property
    def campaign_name(self):
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, value):

        self._campaign_name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value

    # override the __str__ method to provide a string representation of the campaign object and for file writing
    def __str__(self):
        return f"Campaign ID: {self.campaign_id}, Name: {self.campaign_name}, Description: {self.description}, Start Date: {self.start_date}, End Date: {self.end_date}"    