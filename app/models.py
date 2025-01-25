
class User:
    def __init__(self, username, email,password,role,photoURL):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.photoURL = photoURL

class Booking:
    def __init__(self, username, email,phone,location,service,bookingDate,bookingTime):
        self.username = username
        self.email = email
        self.phone = phone
        self.location = location
        self.service = service
        self.bookingDate = bookingDate
        self.bookingTime = bookingTime


class Service:
    def __init__(self, name, description,price,photoURL):
        self.name = name
        self.description = description
        self.price = price
        self.photoURL = photoURL
    
class saler:
    def __init__(self, name, email,phone,location,service,photoURL):
        self.name = name
        self.email = email
        self.phone = phone
        self.location = location
        self.service = service
        self.photoURL = photoURL

class Review:
    def __init__(self, username, email,comment,rate):
        self.username = username
        self.email = email
        self.comment = comment
        self.rate = rate


class Contact:
    def __init__(self, name, email,phone,location,service,message):
        self.name = name
        self.email = email
        self.phone = phone
        self.location = location
        self.service = service
        self.message = message


class Service:
    def __init__(self, name, description,price,photoURL):
        self.name = name
        self.description = description
        self.price = price
        self.photoURL = photoURL


