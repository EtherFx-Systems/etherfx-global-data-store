import redis # Python Client for Redis
import pickle # Pickle the Python object
# Sample Class to test
class sample_class:
	x = 0
	def something(self):
		self.x = 1

x = sample_class() # Instantiate sample class
x.something() # Execute a function call
r = redis.Redis(host='localhost', port=6379, db=0) # Make connection to Redis instance running locally
r.set('foo', pickle.dumps(x)) # Use the "SET" command in Redis to place the Pickle dump as a value for the key foo
res = r.get('foo') # Retrieve pickled object using "GET" command in Redis

unpacked_object = pickle.loads(res) # Unpickle the object
print unpacked_object.x # Print test value