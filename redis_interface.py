import redis
import dill

redis_client = redis.Redis(host='localhost', port=6379, db=0) # Make connection to Redis instance running locally

def add_args_to_gds(task_id,list_of_args):

	# Check if this key already exists
	if check_key_exists_in_gds(task_id): # Returns number of keys found - should be 0
		raise Exception("Task ID already has arguments/results stored in the GDS") # Temporary - Replace by EtherFx error
	
	return insert_in_key_list_redis(list_of_args)

def get_args_from_gds(task_id):

	if not check_key_exists_in_gds(task_id):
		raise Exception("Task ID not found on GDS") # Temporary - Replace by EtherFx error
	

def retrieve_value_list_for_key_gds(redis_key):

	number_of_vals = redis_client.llen(redis_key)
	vals_retrieved = redis_client.lrange(redis_key, 0,number_of_args-1)

	return args_retrieved if args_retrieved else None


def check_key_exists_in_gds(task_id):
	if redis_client.exist(task_id) > 0:
		return True
	else:
		return False

def insert_in_key_list_redis(values_to_be_added):
	
	try:
		for x in values_to_be_added:
		redis_client.rpush(task_id,byte_arg)
	except:
		return False
	return True


def set_result_in_gds(task_id, execution_result):
	'''
	TODO: Figure out if errors need to be stored as elements as opposed to the first (and only) element of the list

	'''
	if check_key_exists_in_gds(task_id):
		clear_gds_for_task_id(task_id)
		return insert_in_key_list_redis(execution_result)

	else:
		raise Exception("Task ID does not exist on the GDS.")

	return False

def get_result_from_gds():

	'''
	TODO: Coordinate with Message Queue to ensure results being retrieved for a task ID in the Completed topic
	'''


def clear_gds_for_task_id(task_id):
	if redis_client.exists(task_id) > 0:
		redis_client.delete(task_id)
		return True
	else:
		return False


def main():
	test_obj = sample_class()
	args = ["abc", "def", "ghi"]
	clear_gds_for_task_id("fooda")
	add_args_to_gds("fooda", args)
	#print get_args_from_gds("fooda")
if __name__ == '__main__':
	main()