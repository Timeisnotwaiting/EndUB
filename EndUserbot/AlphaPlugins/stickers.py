from .utils import eor, get_reply_and_message
from . import Client, Message
import asyncio
from ..database import is_sudo

async def kang(_, m):
    id = m.from_user.id
