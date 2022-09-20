import re
import long_responses as lr
import random

# Testing the response system

def msg_probability(msg, recognized_words, single_response=False, required_words=[]):
    msg_certainity = 0
    has_required_words = True
    for word in msg:
        if word in recognized_words:
            msg_certainity += 1

        percentage = float(msg_certainity) / float(len(recognized_words))

    for word in required_words:
        if word not in msg:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_msg(message):
    highest_prob_list = {}
    def response(bot_response, word_list, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = msg_probability(message, word_list, single_response, required_words)
    # ~~~~~~~~~~~~replies~~~~~~~~~~~~~~~~~
    response('Hello! I am a robot', ['hi', 'hello', 'hey'], single_response=True)
    response('I am doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank you!!', ['i', 'love', 'coding'], required_words=['coding', 'love'])
    response(lr.r_eat, ['what', 'you', 'eat'], required_words=['eat', 'you'])
    response(lr.r_weather, ['what', 'is ','the ','weather','today'], required_words=['weather'])
    response(lr.r_joke(),['tell','me','a','joke'],required_words=['joke'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return lr.unknown() if highest_prob_list[best_match] < 1 else best_match

    #return best_match

def get_response(user_input):
    split_msg = re.split(r'\s+|[-,.;!?]\s*', user_input.lower())
    response = check_msg(split_msg)
    return response


while True:
    print('Computer: ' + get_response(input('JJ:')))

