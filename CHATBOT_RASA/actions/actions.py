# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet, Form
import logging
import datetime

LANGUAGES = {
    "french":
        {
            "name": "french",
            "resource": "fr"
        },
    "english":
        {
            "name": "english",
            "resource": "en"
        },
    "hindi":
        {
            "name": "hindi",
            "resource": "hn"
        },
    "german":
        {
            "name": "german",
            "resource": "de"
        },
    "spanish":
        {
            "name": "spanish",
            "resource": "es"
        },
    "marathi":
        {
            "name": "marathi",
            "resource": "mr"
        },
    "russian":
        {
            "name": "russian",
            "resource": "ru"
        },
    "italian":
        {
            "name": "italian",
            "resource": "it"
        },
    "japanese":
        {
            "name": "japanese",
            "resource": "ja"
        },
    "chinese":
        {
            "name": "chinese",
            "resource": "che"
        }
}
#LANGUAGE = ["Hindi","Marathi","English","French","German","Spanish","Russian","Italian","Japanese","Chinese"];
#MOOD= ["happy","sad","upset","worry","excited","silly","frustrated","scared","angry"]
MOOD= ["happy","sad","frustrated","scared","angry"]

SMILIES = [
    "http://assets.stickpng.com/thumbs/580b57fcd9996e24bc43c4c4.png",
    "https://freepngimg.com/thumb/sad_emoji/36900-6-sad-emoji-transparent-background.png",
    #"https://cdn.pixabay.com/photo/2020/12/30/01/45/smile-5872116_960_720.png",
    #"https://images.vexels.com/media/users/3/134883/isolated/preview/1269f12b5ff489b48a95de85e2ca594d-worry-emoji-emoticon-by-vexels.png",
    #"https://www.nicepng.com/png/full/57-578157_excited-smiley-excited-emoticon.png",
    #"https://cdn.statically.io/img/i.pinimg.com/originals/2a/7c/39/2a7c3946ac753caf637609f487adeefb.png",
    "https://www.pngkit.com/png/full/286-2868772_angry-frustrated-fight-emoji-fight-emoji.png",
    "http://assets.stickpng.com/thumbs/580b57fcd9996e24bc43c4ba.png",
    "https://pngimage.net/wp-content/uploads/2018/05/angry-smile-png-2.png"
]

GENRE = ["action","adventure","darkmovies","drama","fantasy","musical","romance","sci-fi","thriller","comedy","history"]

def _resolve_name(languages, resource) ->Text:
    for key, value in languages.items():
        if value.get("resource") == resource:
            return value.get("name")
    return ""

class FindLanguageTypes(Action):
    """This action class allows to display buttons for languages to choose."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_language_types"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        
        buttons = []
        for t in LANGUAGES:
            language = LANGUAGES[t]
            payload =  language.get("name")

            buttons.append(
                {"title": "{}".format(language.get("name").title()),
                 "payload": payload})

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_message(template="utter_greet",buttons=buttons)
        return []

class FindMood(Action):
    """This action class allows to display buttons for languages to choose."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_mood"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        
        buttons = []
        for m,smiley in zip(MOOD,SMILIES):
            payload =  m
            k=f"<img class=\"mood-image\" src=\"{smiley}\" alt=\"{payload}\">"

            buttons.append(
                {"title": k,
                 "payload": payload})

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_message(template="utter_select_mood",buttons=buttons)
        return []

class FindGenre(Action):
    """This action class allows to display buttons for languages to choose."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_genre"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        
        buttons = []
        for g in GENRE:
            payload =  g

            buttons.append(
                {"title": "{}".format(g.title()),
                 "payload": payload})

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_message(template="utter_select_genre",buttons=buttons)
        return []