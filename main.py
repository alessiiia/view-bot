import os
import requests
import random
import os
import random
import time
import requests
from fake_useragent import UserAgent
from colorama import Fore
from apify_client import ApifyClient
from concurrent.futures import ThreadPoolExecutor

# Initialize the ApifyClient with API token and Actor ID
client = ApifyClient(os.getenv('APIFY_TOKEN'), os.getenv('APIFY_ACTOR_ID'))
key_value_store = client.key_value_store(os.getenv('APIFY_DEFAULT_KEY_VALUE_STORE_ID'))

async def get_actor_input():
    
	# Get input from the default key-value store under the "INPUT" key
	input_data = await key_value_store.get_record('INPUT')
	return input_data['value']

def send_request(url, min_time, max_time, proxy_url):
	
	ua = UserAgent(cache=False)
	agent = ua.random
	headers = {"User-Agent": agent}
	proxies = {
		'http': proxy_url,
		'https': proxy_url
    }
    
	try:
        
		response = requests.get(url, headers=headers, proxies=proxies)
		sleep_time = random.randint(min_time, max_time)
		time.sleep(sleep_time)  # Simulate time spent on page
		
		print(f"{Fore.GREEN}Request Sent as {agent} with response code {response.status_code}. Time on page: {sleep_time} seconds.{Fore.RESET}")
	
	except requests.exceptions.RequestException as e:
		
		print(f"{Fore.RED}Error: {str(e)}{Fore.RESET}")

def main():
    input_data = get_actor_input()
    url = input_data['url']
    min_time = input_data['minTime']
    max_time = input_data['maxTime']
    num_requests = input_data['numRequests']
    avoid_repetition = input_data['avoidRepetition']
    
    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        urls = [f"{url}?q={i}" if avoid_repetition else url for i in range(num_requests)]
        futures = [executor.submit(send_request, url, min_time, max_time, os.getenv('PROXY_URL')) for url in urls]
        for future in futures:
            future.result()

if __name__ == '__main__':
    main()


