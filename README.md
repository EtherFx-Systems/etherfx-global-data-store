# global-data-store

In this document, I am noting the steps required to setup a functioning Redis instance from the perspective of setting up a Docker image.

1. Download a stable release of Docker from the offical page.
2. Call the Makefile : Simply use "make"
3. Call "make test" to check if a clean installation occured. Parse the last line printed to stdout/stderror. This line is "\o/ All tests passed without errors!"
4. Bring up a Redis instance (for now with default config) : "./src/redis_server"
5. Install the Python client(?) Could be done on the orchestrator. Would need to expose GDS publically. Other alternative is to make an interface on the GDS end. The GDS speaks to a local instance of Redis and other components intereact with the GDS code. Exposing Redis directly seems to be the easier alternative. This would require "pip install redis" on the orchestrator. The orchestrator would need to pickle the data.
6. Try set and get for the pickled data. A very elementary sample can be found in redis_test.py