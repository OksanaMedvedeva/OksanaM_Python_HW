from address import Address
from mailing import Mailing

to_address = Address("123456", "Moscow", "Lenina", "10", "42")
from_address = Address("654321", "Saint Petersburg", "Nevsky", "20", "14")

mailing = Mailing(to_address, from_address, 500, "TR123456789")

print(mailing)
