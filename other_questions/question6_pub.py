import redis
import time
import random


config = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
}

r = redis.StrictRedis(**config)

if __name__ == '__main__':
    while True:
        rand_value = random.random()
        print "sent {}".format(rand_value)
        r.publish("get_rand_numbers", rand_value)
        time.sleep(random.randint(1,3))