from os import getenv as _

API_ID = int(_("API_ID", 10763476))
API_HASH = _("API_HASH", "e7d6d5493a896264a09d04fda7a30f9d")
STRING_SESSION = _("STRING_SESSION", "BQAe9JqPWUhC1G9Q9luEf0UsItzVFVmETRoTulzyj3MZy6bQQEl4o8W9DWCVJKufWQUyFdsB3gsDCU4chk33WiAeSWytgIKIxKLYVF_V-0kkkp3vvJUoNfmD3XNzXnw8-ctVDuwmAh7f7fh8OmOOGSVePM4WSQzvZevK0JYPoNuZ8r_ApEQd1iLmTOvs60ev6w_xCh5kL67IF34Sn5ttY1DBYU2nAK-9WUMKv_uwerR2ZR_U7yuEdodNomdonqQ37uM3MmHoIc31gEBfRw4CLwJr7yG0J1LAuZ6erKNJOJxbdbtKoXZHf7gKk1oPNjnqdUjwffORRl_u5bP4-jsRvs4VAAAAAV3PR04A")
MONGO_DB_URL = _("MONGO_DB_URL", "mongodb+srv://musicbot:<password>@cluster0.61lydz4.mongodb.net/?retryWrites=true&w=majority")
COMMAND_HANDLER = _("COMMAND_HANDLER", ".")
ALIVE_PIC = _("ALIVE_PIC", "https://te.legra.ph/file/be4de09294b646d9479ee.jpg")

if not COMMAND_HANDLER:
    COMMAND_HANDLER = "!"
