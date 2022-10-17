from ...database import is_sudo
from ..import Client, Message

async def verify(id):
    async def verify_user(_: Client, m: Message):
        sudo = await is_sudo(m.from_user.id)
        myself = await _.get_me().id
        self_ = True if myself == id else False
        if not self_ and not sudo:
            return False
        return True
    return await verify_user(_, m)
