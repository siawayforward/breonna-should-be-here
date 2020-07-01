from datetime import date, datetime

class Angel:
    
    def __init__(self, data_file = None):
        #grab attributes
        self.contents = []
        try:
            with open(data_file, 'r') as file:
                for line in file:
                    self.contents.append(line[:-1])
            file.close()
        except: pass
        #extract attributes from contents of file
        self.get_file_contents()         

    #separate attributes from file
    def get_file_contents(self):
        self.name = self.contents[0]
        self.ascension_date = self.contents[1]
        self.days_since = (date.today() - datetime.strptime(self.ascension_date, '%B %d, %Y').date()).days
        self.hashtags = self.contents[2]
        self.status_updates = []
        #look for format items; there has to be a better way?
        for update in self.contents[3:]:
            try:
                update = update.format(days=self.days_since)
            except KeyError as ke:
                update = update.format(date=self.ascension_date)
            else:
                pass
            finally:
                self.status_updates.append(update)
        #search tags for retweets and likes        
        name_tags = self.name.replace(' ','')
        self.search = [self.name, self.name.upper(), name_tags, name_tags.upper()]
                  