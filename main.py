import requests, threading, time
from fake_useragent import UserAgent

ua = UserAgent()
agent = ua.random


url ='https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FRojanGamingYT%2FRojanGamingYT'

urll = 'https://l.instagram.com/?u=https%3A%2F%2Frojansapkota.com.np%2F&e=ATOOyL2K5Q0S91Mk-jqZPvf5UY-xewGCP2RGEtcxXhJWnN_VZOirdnVBPlyHDwfCQg0AuQuUG2cVKHijBljlUg&s=1'

headers = {
    "User-Agent":
    agent
}

def requests_sender():
	while True:
		requests.get(url, headers=headers)
		agent = ua.random
		print(f"Request Sent as {agent}")

if __name__ == "__main__":
	requests_sender()