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

    def __setitem__(self, name, value):
        """Setting values should be easy."""
        if isinstance(value, list) or isinstance(value, tuple):
            for item in value:
                length = self.rpush(name, item)
            return length
        elif isinstance(value, set):
            for item in value:
                length = self.sadd(name, item)
            return length
        elif isinstance(value, dict):
            return self.hmset(name, value)
        return self.set(name, value)
