class Project:
    def __init__(self, email, title, details, target, start_date, end_date):
        self.email = email
        self.title = title
        self.details = details
        self.target = target
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return str(self.__dict__)
