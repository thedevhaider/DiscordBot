import os
import re
import logging
import traceback

from pymongo import MongoClient
from dotenv import load_dotenv
from utils.helper import to_csv
from pymongo.errors import OperationFailure

load_dotenv()


class DatabaseClient:
    """Utility class to perform database queries"""

    def __init__(self):
        self.__db = MongoClient(os.getenv('MONGODB_CONNECTION')).gamebot
        self.__history_collection = self.__db.history

    def push_history(self, keyword, author):
        """Push the search history to the database"""
        # Make a document structure
        history = {
            'keyword': keyword,
            'author': author
        }

        # Save the document to database
        try:
            self.__history_collection.insert_one(history)
        except OperationFailure:
            trace = traceback.format_exc()
            logging.error('Could not able to insert into database', extra=trace)

    def author_history(self, keyword, author):
        """Fetch the author history from the database"""
        # Search for recent searches matching the keyword
        try:
            result = self.__history_collection.find({'author': author, 'keyword': re.compile(keyword, re.IGNORECASE)})
        except OperationFailure:
            trace = traceback.format_exc()
            logging.error('Could not able to search from database', extra=trace)
            return

        # Convert the result to CSV format
        return to_csv(result)
