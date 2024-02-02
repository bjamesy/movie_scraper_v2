from rq import Queue
from redis import Redis
from src.scrapers.theatre_scraper import get_fox


redis_conn = Redis()
# redis_conn = Redis("", 6379)
q = Queue(connection=redis_conn)  # no args implies the default queue

# Delay execution of count_words_at_url('http://nvie.com')
job = q.enqueue(get_fox())
print(job.result)   # => None  # Changed to job.return_value() in RQ >= 1.12.0

# Now, wait a while, until the worker is finished
print(job.result)   # => 889  # Changed to job.return_value() in RQ >= 1.12.0
