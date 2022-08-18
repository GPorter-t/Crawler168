import redis

from Crawler168.settings import REDIS_CONFIG


class RedisPool:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    _redis_pool_data = redis.ConnectionPool(decode_responses=True, **REDIS_CONFIG)

    # 实例化redis
    @classmethod
    def get_conn(cls):
        conn = redis.Redis(connection_pool=cls._redis_pool_data)
        return conn

