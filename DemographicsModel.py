from DataModelDemographics import Demographics
#import geopy
#from geopy.geocoders import Nomination

db=Demographics()
# initialize Nominatim API
#geolocator = Nominatim(user_agent="geoapiExercises")
Latitude = "25.594095"
#Longitude = "85.137566"
#location = geolocator.reverse(Latitude + "," + Longitude)
#address = location.raw['address']
#item1 = address.get('state', '')

item=(1,'CA','25.594095')

db.insertTable(item)
db.readTable()
db.conClose()
