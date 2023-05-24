class Weather:

    def __init__(self,date, average_temperature, atmospheric_pressure, precipitation):
        self.date = date
        self.average_temperature = average_temperature
        self.atmospheric_pressure = atmospheric_pressure
        self.precipitation = precipitation

    def print_summary(self):
        print('Date: {}\nAverage_temperature: {}°C\nAtmospheric_pressure: {}\nPrecipitation: {}'
            .format(self.date, self.average_temperature, self.atmospheric_pressure,self.precipitation))

print('Weather for Kiev')
Kiev = Weather('14.10.2022', '23',0.1, 0.63)
Kiev.print_summary()

print()

print('Weather for Lviv')
Lviv = Weather('14.10.2022', '22',0.15, 0.78)
Lviv.print_summary()

