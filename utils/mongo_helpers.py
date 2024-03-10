import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def save_to_mongo(module_title, topics, module_summary, module_image_path="", force=False):
    mongo_url = os.getenv('MONGO_URL')
    client = MongoClient(mongo_url)
    # Replace 'your_database_name' with your actual database name
    db = client.module_qa
    # Replace 'your_collection_name' with your actual collection name
    collection = db.module_qa

    if force:
        # If force is True, insert or update the document
        collection.update_one({'module_title': module_title}, {
                              '$set': {
                                  'topics': topics,
                                  'module_summary': module_summary,
                                  'module_image_url': module_image_path
                              }}, upsert=True)
        print(
            f"Document with module_title '{module_title}' inserted or updated with force.")
    else:
        # Check if a document with the same module_title exists
        if collection.find_one({'module_title': module_title}) is None:
            # If not found, insert the new document
            document = {
                'module_title': module_title,
                'topics': topics,
                'module_summary': module_summary,
                'module_image_path': module_image_path
            }
            collection.insert_one(document)
        else:
            print(
                f"Document with module_title '{module_title}' already exists. Skipping insertion.")

    # Close the connection
    client.close()


def get_module_summary(module_title):
    mongo_url = os.getenv('MONGO_URL')
    client = MongoClient(mongo_url)
    db = client.module_qa
    collection = db.module_qa

    module_data = collection.find_one(
        {'module_title': module_title}, {'module_summary': 1})
    client.close()

    if module_data:
        return module_data.get('module_summary', '')
    else:
        return None


def get_module(module_title):
    mongo_url = os.getenv('MONGO_URL')
    client = MongoClient(mongo_url)
    db = client.module_qa
    collection = db.module_qa

    module_data = collection.find_one({'module_title': module_title})
    client.close()

    if module_data:
        # Convert ObjectId to string
        module_data['_id'] = str(module_data['_id'])

    return module_data
