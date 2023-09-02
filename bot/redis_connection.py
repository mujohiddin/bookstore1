import json

from redis import Redis

redis_connection = Redis()

# redis_connection.mset({'494473113': json.dumps({
#     'phone_number': '903467701'
#     })
# })

# print(redis_connection.get('494473113'))

# redis_connection.delete('494473113')