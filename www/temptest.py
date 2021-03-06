import asyncio
import sys

from www import orm
from www.models import User

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    @asyncio.coroutine
    def test():

        yield from orm.create_pool(loop=loop, host='localhost', port=3306, user='www-data',
                                   password='www--data', db='awesome')
        u = User(id='1', name='zt', email='zzgdata@gmail.com', passwd='1234567890',
                 image='about:blank', admin=False)

        yield from u.save()
        # yield from orm.destroy_pool()

    loop.run_until_complete(test())
    loop.close()
    if loop.is_closed():
        sys.exit(0)
