from datetime import date

class Angel:
    
    def __init__(self, data_file = None):
        #grab file data
        self.updates = []
        try:
            with open(data_file, 'r') as file:
                self.name = file.readline()
                self.ascension_date = file.readline()
                self.ascension_obj = date.strptime(self.ascension_date, '%B %d, %Y')
                self.days_since = (date.today() - self.ascension_obj).days
                tag_name = self.name.replace(' ','')
                self.search = [self.name, self.name.upper(), tag_name, tag_name.upper()]
                self.hashtags = file.readline()
                for line in file:
                    self.updates.append(line[:-1])
        except: 
            file.close()
    
    def get_file_data(self):
        #for update in self.updates:
        #    if '{days}' in update: update = update.format(self.days_since)
        #    if '{date}' in update: update = update.format(self.ascension_date)
        #return self.updates
        pass