from utils.mongo_helpers import save_to_mongo
import json
from utils.openai_helpers import get_openai_response
from Download import download_video_from_tiktok
from Transcribe import extract_transcript_from_deepgram, is_transcript_usable


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
        {{generate_topics_from_module_title
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


def extract_qa_from_transcript(module_title, topic, transcript):
    prompt = f"""
    Given the following module, topic and transcript of short video, extract a list of questions and answers for a quiz.
    
    Keep it light, at a 9th-11th grade accessible level. But do test the student's understanding of the topic.

    Module title: {module_title}
    Topic: {topic}
    Transcript:
    {transcript}
    
    Return your response in the format
    
    [
        {{
            "question": "who moved the cheese?"
            "answer": "you did",
            "options": []
            "style": "free_text"
        }}
    ]
    
    The two options for question style are "free_text" and "multiple_choice". If the qa style is "multiple_choice", the answer MUST be in the options.
    
    If there are no questions to be asked, return a soft generic question or two related to the module or preferably the topic.
    
    AVOID asking questions that are phrased negatively eg "what is not a good way to do X?"

    Questions and answers:
    """
    # print(prompt)
    text = get_openai_response(prompt)
    # print(text)
    response = get_json_from_response(text)
    return response

def generate_module_summary(module_title, topics):
    prompt = f"""
    Given the following module title "{module_title}" and topics, generate a summary of the module.
    
    The max length is 2500 words. This is a hard limit. 
    
    This summary will be passed on to a smaller LLM and used in context to answer student questions.
    
    Students are not very sophisticated and are not expected to have a lot of background knowledge. Nor is the LLM.
    So you should make this summary easy to follow, easy to generate great answers from, yet have a lot of technical and emotive depth.
    
    You are a master AI tutor. Go forth and produce something epic that students and smaller AIs can use as a touchstone for the module.
    """
    summary = get_openai_response(prompt)
    return summary


def hydrate_module_from_title(module_title, save=False):
    topics = generate_topics_from_module_title(module_title)
    for topic in topics:
        index = 0
        while index < 10:
            video = download_video_from_tiktok(topic["search_query"], index)
            transcript = extract_transcript_from_deepgram(
                video["path"])
            print(transcript)
            if is_transcript_usable(transcript):
                video["transcript"] = transcript
                break
            else:
                index += 1

        topic["video"] = video
        qa = extract_qa_from_transcript(
            module_title,
            topic["topic"],
            video["transcript"]
        )
        topic["qa"] = qa
    
    module_summary = generate_module_summary(module_title, topics)

    if save:
        save_to_mongo(module_title, topics, module_summary)

    return topics
