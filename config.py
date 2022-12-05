from os import getenv as _

API_ID = int(_("API_ID", 10763476))
API_HASH = _("API_HASH", "e7d6d5493a896264a09d04fda7a30f9d")
STRING_SESSION = _("STRING_SESSION", "BQBtXATuNg3sGwXYPj0Ty-aCMMwdmB3kAvJlART1SF9ikODmAKt26WO_aoMzB1Fl-g3Py0VXAW3hcK8DSFVKN6nUj4KFF0buhQwvSl5cpGMAEZLkr_prBpkivtw5S7mHoc5ksSQjHGQpI8MAIW3ShaOGkK7VsX1vfbqU-2FQZM8esa5h8-zpZCEhpPjK8TM0Z0hK8Ho9HBjyO0Ikh8x10GPiIE6ellOyaf-WX1xm7w8pAutO9zTvm4qTq30wDA7ghZ0tHpVha5Irb7TwY4NzRCoPwWFy9BMu91Ygs-gD_siZBD7Y2lfYPHiCG9UnQ8ue36qjANdLS51jMASK2TsXErhKAAAAAV3PR04A")
MONGO_DB_URL = _("MONGO_DB_URL", "mongodb+srv://musicbot:<password>@cluster0.61lydz4.mongodb.net/?retryWrites=true&w=majority")
COMMAND_HANDLER = _("COMMAND_HANDLER", None)
ALIVE_PIC = _("ALIVE_PIC", "https://te.legra.ph/file/be4de09294b646d9479ee.jpg")

if not COMMAND_HANDLER:
    COMMAND_HANDLER = "!"
