import os

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()


class GoogleSearch:
    """Utility class for doing Google search"""

    def __init__(self):
        self.__key = os.getenv('API_KEY')
        self.__cx = os.getenv('CSE_KEY')
        self.service = build('customsearch', 'v1', developerKey=self.__key)

    def search(self, query):
        """Search in Google for the given query"""

        # Make request to Google
        res = self.service.cse().list(
            q=query,
            cx=self.__cx,
            num=5
        ).execute()

        # Extract data from response and return
        return self.__extract_data(res)

    @staticmethod
    def __extract_data(response):
        """Extract required data from the Google search response"""
        result = []
        for item in response.get('items', []):
            data = {
                'title': item.get('title', ''),
                'link': item.get('link', '')
            }
            result.append(data)
        return result
