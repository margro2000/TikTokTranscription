import json
from utils.openai_helpers import get_openai_response

def get_json_from_response(text):


    # Find the start and end of the JSON string
    start_index = text.index('[')
    end_index = text.rindex(']') + 1  # +1 to include the closing bracket

    # Extract the JSON string
    json_str = text[start_index:end_index]

    # Parse the JSON string
    topics = json.loads(json_str)

    return topics


def generate_topics_from_module_title(module_title):
    prompt = f"""
    Given the following module title "{module_title}", generate a list of topics that could be covered in the module.
    
    Along with each topic, I need a search query for tiktok.
    
    The way our app works, we are finding 1 tiktok video per topic to teach that topic. Try to stick to no more than 5 topics please.
    
    The video should be engaging yet comprehensive. 
    
    For example, given the module title "Working with objects using Adobe Illustrator", we expect output like this, except whittled down to 5.
    
    [
        {{
            "topic": "Creating shapes and objects",
            "search_query": "adobe illustrator creating shapes objects tutorial"
        }},
        {{
            "topic": "Selecting and grouping objects",
            "search_query": "adobe illustrator selecting grouping objects tips"
        }},
        {{
            "topic": "Transforming objects (resize, rotate, reflect)",
            "search_query": "adobe illustrator transform objects tutorial"
        }},
        {{
            "topic": "Aligning and distributing objects",
            "search_query": "adobe illustrator align distribute objects guide"
        }},
        {{
            "topic": "Using the Pathfinder panel",
            "search_query": "adobe illustrator pathfinder panel tutorial"
        }},
        {{
            "topic": "Working with layers and stacking order",
            "search_query": "adobe illustrator layers stacking order tips"
        }},
        {{
            "topic": "Masking and clipping objects",
            "search_query": "adobe illustrator masking clipping objects tutorial"
        }},
        {{
            "topic": "Blending and merging objects",
            "search_query": "adobe illustrator blend merge objects guide"
        }},
        {{
            "topic": "Using the Shape Builder tool",
            "search_query": "adobe illustrator shape builder tool tutorial"
        }},
        {{
            "topic": "Organizing objects with groups and layers",
            "search_query": "adobe illustrator organize objects groups layers tips"
        }}
    ]
    
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

    text = get_openai_response(prompt)
    response = get_json_from_response(text)
    return response
