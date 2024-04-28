{
	"title": "Actor Input",
	"type": "object",
	"properties": {
		"url": {
			"title": "URL",
			"type": "string",
			"description": "The URL to send requests to."
		},
		"minTime": {
			"title": "Minimum Time on Page",
			"type": "integer",
			"description": "Minimum time spent on each page in seconds."
		},
		"maxTime": {
			"title": "Maximum Time on Page",
			"type": "integer",
			"description": "Maximum time spent on each page in seconds."
		},
		"numRequests": {
			"title": "Number of Requests",
			"type": "integer",
			"description": "Number of requests to make."
		},
		"avoidRepetition": {
			"title": "Avoid Repetition",
			"type": "boolean",
			"description": "Whether to avoid repeating the page view."
		}
	},
	"required": [
		"url",
		"minTime",
		"maxTime",
		"numRequests"
	]
}
