from flask import request,jsonify
import json
import time

from chat import get_response
from db import ChatDatabase
from chat import bot_name

user_name = ""
contact_number = ""
transcript = ""
count = 0


def predict():
    global user_name, contact_number , transcript , count
    text = request.get_json().get("message")
    response = ""

    if text.lower() in ["hi" , "hello", "hii"] or transcript == "":
        response = "Hi there! Please enter your name."

    elif user_name == "":
        user_name = text
        response = "Hi " + user_name + "! Please enter your contact number."

    elif contact_number == "":
        contact_number = text
        response = "Thank you, " + user_name + ". Your contact number is " + contact_number + ". How can I assist you today?"

    elif text.lower() in ["bye","Thank you","ok"] and contact_number != "" and user_name != "":

        db = ChatDatabase()
        db.add_chat(contact_number=contact_number, username=user_name, chat=transcript)
        response = "Thank You! Please give us feedback whether you are satisfied with our support or not."

    elif text.lower() in ["yes","satisfied"] or text.lower() in ["not","no","Not Satisfied"]:
        if text.lower() in ["yes","satisfied"]:
            response = "Thanks for Visiting , Have a nice day :)"
        else:
            response = "Sorry for the inconvenience, You can contact to our Doubt Assitant"
        # print(transcript)

    else:
        response = get_response(text)

    if response == "Sorry! I am not able to understand...":
        count=count+1
        with open('newQuery.json','a') as file:
            query_data = {"query":text}
            json.dump(query_data,file)
            file.write('\n')

    if count == 3:
        response = "Sorry for the inconvenience, Our doubt support team will contact you very soon or you can contact with us through mail. Our mail is edtech.gmail.com"

    message = {"answer": response}
    transcript += f"{user_name}-{text}\n{bot_name}-{response}\n"
    return jsonify(message)
