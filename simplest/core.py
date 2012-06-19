"""
Simple core functionality.
"""

from redis import StrictRedis


class Redis(StrictRedis):
    """A Redis class with sugary goodness."""

    def __getitem__(self, name):
        """Easy access to items in the database."""
        data_type = self.type(name)
        if data_type == 'string':
            return self.get(name)
        elif data_type == 'hash':
            return self.hgetall(name)
        elif data_type == 'list':
            return self.lrange(name, 0, -1)
        elif data_type == 'set':
            return self.smembers(name)
        elif data_type == 'zset':
            return self.zrange(name, 0, -1)
        else:
            return None
