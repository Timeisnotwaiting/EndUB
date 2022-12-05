from os import getenv as _

API_ID = int(_("API_ID", 10763476))
API_HASH = _("API_HASH", "e7d6d5493a896264a09d04fda7a30f9d")
STRING_SESSION = _("STRING_SESSION", None)
MONGO_DB_URL = _("MONGO_DB_URL", "mongodb+srv://musicbot:<password>@cluster0.61lydz4.mongodb.net/?retryWrites=true&w=majority")
COMMAND_HANDLER = _("COMMAND_HANDLER", None)
ALIVE_PIC = _("ALIVE_PIC", "https://te.legra.ph/file/be4de09294b646d9479ee.jpg")

if not COMMAND_HANDLER:
    COMMAND_HANDLER = "!"
