from requests import get
import logging


def download_summary():
	"""
  Send HTTP request to API /summary and return the response in JSON format.

  API details: https://documenter.getpostman.com/view/10808728/SzS8rjbc#00030720-fae3-4c72-8aea-ad01ba17adf8

	"""
  # Send the HTTP request
  # Check for the HTTP response status 200 (OK)
  	# Return the response as JSON
return response.json()
  # Otherwise, something went wrong
    # Show the error message
 # Log the error message
        logging.error(f'An error has occurred: HTTP status {response.status_code}')
        # Return an empty result
        return {}