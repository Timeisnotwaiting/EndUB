from os import getenv as _

API_ID = int(_("API_ID", 10763476))
API_HASH = _("API_HASH", "e7d6d5493a896264a09d04fda7a30f9d")
STRING_SESSION = _("STRING_SESSION", "BQADltcIFS0deygOdEQIgL1raT1gtD5aBdAS1wz8wbn4802yD9I8QHXJYShl-WLbzgGycee4AtU3E21UFO2iOFjySOrLGoM3_AdjO-Vtolq7caoPpw7z-POifGBJ3FNLYIc81lInZglNi2gn51l6Libd4-2JQmzEOP-DhQXjCO30Zv5btYk4fA2rQM62jj7u4z9NNN9Jlt4-oKSKYSoh5zjk3sPIezwt5DKLEBmdyEYYBWmQ7w-1_e2GOUw8eE81H95B2crLNiP_5pcoRdC1YAiKSO2YFXMTU3hzQsa1XkTg2mN8YN1WPS3XKJz0MGi2OXUNuN4jaGe7s0cr8yefUg_LAAAAAV3PR04A")
MONGO_DB_URL = _("MONGO_DB_URL", "mongodb+srv://musicbot:<password>@cluster0.61lydz4.mongodb.net/?retryWrites=true&w=majority")
COMMAND_HANDLER = _("COMMAND_HANDLER", ".")
ALIVE_PIC = _("ALIVE_PIC", "https://te.legra.ph/file/be4de09294b646d9479ee.jpg")

if not COMMAND_HANDLER:
    COMMAND_HANDLER = "!"
