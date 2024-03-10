import json
from utils.anthropic_helpers import get_message_from_anthropic

def get_json_from_response(text):


    # Find the start and end of the JSON string
    start_index = text.index('[')
    end_index = text.rindex(']') + 1  # +1 to include the closing bracket

    # Extract the JSON string
    json_str = text[start_index:end_index]

    # Parse the JSON string
    topics = json.loads(json_str)

    print(topics)


def generate_topics_from_module_title(module_title):
    prompt = f"""
    Given the following module title "{module_title}", generate a list of topics that could be covered in the module.
    
    Along with each topic, I need a search query for tiktok. Try to stick to 5 or less topics.
    
    The way our app works, we are finding 1 tiktok video per topic to teach that topic. 
    
    The video should be engaging yet comprehensive.
    
    Please return the list of topics and search queries in the following format:

    [
        {{
            "topic": "topic 1",
            "search_query": "search query 1"
        }},
        {{
            "topic": "topic 2",
            "search_query": "search query 2"
        }}
    ]
    
    as valid json
    """
    # print(prompt)

    text = get_message_from_anthropic(prompt)
    response = get_json_from_response(text)
    return response
