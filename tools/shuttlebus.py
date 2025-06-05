"""
title: String Inverse
author: Your Name
author_url: https://website.com
git_url: https://github.com/username/string-reverse.git
description: This tool calculates the inverse of a string
required_open_webui_version: 0.4.0
requirements: langchain-openai, langgraph, ollama, langchain_ollama
version: 0.4.0
licence: MIT
"""

import requests
import json # Used for pretty-printing in the __main__ block

class Tools:
    def __init__(self):
        """
        Constructor for the SKKU Shuttle Bus Tool.
        Can be used for one-time setup if needed.
        """
        pass

    def get_skku_shuttle_status(self) -> dict:
        """
        Fetches the latest publicly available real-time location and status for a Sungkyunkwan University (SKKU) shuttle bus.
        The API typically provides a list of bus updates; this tool returns the first entry from that list, which is presumed to be the most recent update.
        The information includes details like the bus line number, its current status (e.g., 'ENTERED' a stop, 'LEFT' a stop), stop number, sequence in the route, stop name, and the timestamp of when the data was recorded.
        Returns a dictionary containing the latest shuttle bus data. If an error occurs during the fetch operation or if no data is found, it returns a dictionary with an 'error' key detailing the issue.
        """
        url = "http://route.hellobus.co.kr:8787/pub/routeView/skku/getSkkuLoc.aspx"
        try:
            response = requests.get(url, timeout=10)  # Added a 10-second timeout
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            
            data = response.json()

            if isinstance(data, list) and data:
                # The API returns a list of bus data objects.
                # We return the first one, assuming it's the latest information available.
                return data[0] 
            elif isinstance(data, list) and not data:
                # The API returned an empty list.
                return {"error": "No shuttle bus data received. The API returned an empty list."}
            else:
                # The API returned data but not in the expected list format.
                return {
                    "error": "Unexpected data format received from the shuttle bus API.",
                    "received_data_type": str(type(data))
                }

        except requests.exceptions.HTTPError as http_err:
            error_message = f"HTTP error occurred: {http_err}."
            # response might not be defined if the error is before the request completes (e.g. DNS failure)
            # but for HTTPError, response should exist.
            if hasattr(response, 'status_code'):
                error_message += f" Status Code: {response.status_code}."
            return {"error": error_message}
        except requests.exceptions.ConnectionError as conn_err:
            return {"error": f"Error connecting to the shuttle bus API server: {conn_err}"}
        except requests.exceptions.Timeout as timeout_err:
            return {"error": f"The request to the shuttle bus API timed out: {timeout_err}"}
        except requests.exceptions.RequestException as req_err: 
            # Catch any other request-related errors
            return {"error": f"An unexpected error occurred during the request to the shuttle bus API: {req_err}"}
        except ValueError:  # Catches json.JSONDecodeError
            error_message = "Error decoding JSON response from the shuttle bus API."
            # It's helpful to see what the response was if it's not valid JSON
            if 'response' in locals() and hasattr(response, 'text'):
                # Include a snippet of the response text if available
                error_message += f" Response text snippet: {response.text[:200]}..." 
            return {"error": error_message}
        except Exception as e:
            # Catch any other unexpected errors
            return {"error": f"An unexpected error occurred: {str(e)}"}

# This block allows you to test the tool directly by running `python skku_shuttle_tool.py`
if __name__ == "__main__":
    tool_instance = Tools()
    shuttle_info = tool_instance.get_skku_shuttle_status()
    
    print("SKKU Shuttle Bus Status:")
    # Pretty print the JSON output using the json module
    print(json.dumps(shuttle_info, indent=2, ensure_ascii=False))