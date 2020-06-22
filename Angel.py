class Angel:
    
    def __init__(self, data_file = None):
        try:
            with open(data_file, 'r') as file:
                self.name = file.readline()
                self.ascension_date = file.readline()
                tag_name = self.name.replace(' ','')
                self.search = [self.name, self.name.upper(), tag_name, tag_name.upper()]
                self.hashtags = file.readline()
                self.updates = []
                for line in file:
                    self.updates.append(line[:-1])
        except: 
            file.close()
    
    def get_status_updates(self):
        pass