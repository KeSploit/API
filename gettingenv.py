import os

# Retrieve the API key from the environment secret
API_KEY = os.getenv('API_KEY')

# Check if the API key is retrieved successfully
if API_KEY:
    print("API key:", API_KEY)
else:
    print("Error: API key not found in environment secret")
