from datetime import datetime

def get_duration(dt_1, dt_2):
    """Return the difference of two ISO 8601 time strings in days"""

    date_1 = datetime.strptime(dt_1,'%Y-%m-%dT%H:%M:%S.%fZ')
    date_2 = datetime.strptime(dt_2,'%Y-%m-%dT%H:%M:%S.%fZ')

    if date_1 < date_2:
        duration = date_2 - date_1
    else:
        duration = date_1 - date_2    

    return duration.days

class Item:
    """To validate the Ticket summury before creating a DynamoDB entry"""

    def __init__(self, ticket):
        """Initiated with a ticket, a json object.

        Since DynamoDB does not accept None/Null values, the field will be
        filled some other representative value.
        """

        self.summary = ticket['summary']
        self.created = ticket['created']
        self.completed = ticket['completed']
        self.priority = ticket['priority']
        
        try:
            self.duration = get_duration(self.created, self.completed)
            print (self.duration)
        except Exception:
            pass
        
    def validate(self):
        """Returns a dict of field:value that are safe for DynamoDB"""

        valid_fields = {}
        for each in self.__dict__:
            # Creating the ticket id from the epoch time of `created`
            if each == 'created':
                dt = datetime.strptime(self.__dict__[each],'%Y-%m-%dT%H:%M:%S.%fZ')
                epoch_t = (dt - datetime(1970,1,1)).total_seconds()
                ticket_id = str(epoch_t).replace('.', '')
                valid_fields['id'] = ticket_id

            if self.__dict__[each] == "":
                continue
            valid_fields[each] = self.__dict__[each]

        return valid_fields
