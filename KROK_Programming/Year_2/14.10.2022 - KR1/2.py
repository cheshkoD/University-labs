class Date:

    def __init__(self, month_date, day=0, year=0):
        self.month_date = month_date
        self.day = day
        self.year = year


    def change_format(self):
        number_date = "%d.%m.%Y"
        word_date = "%B %d, %Y"

        if self.day == 0 and self.year == 0:
            date = datetime.strptime(self.month_date, number_date)
            return date.strftime(word_date)
        string_date = self.month_date + " " + str(self.day) \
                      + ", " + str(self.year)
        date = datetime.strptime(string_date, word_date)
        return date.strftime(number_date)


    def __str__(self):
        return f"{self.change_format()}"