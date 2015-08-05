import redis

config = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
}

r = redis.StrictRedis(**config)


if __name__ == '__main__':
    pubsub = r.pubsub()
    pubsub.subscribe("get_rand_numbers")
    while True:
        for item in pubsub.listen():
            print "recvd {}".format(item['data'])