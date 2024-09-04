# 
# 
# 
# 
import requests

parameters = {
    "amount" : 10,
    "category" : 21,
    "type" : "boolean"
}
response = requests.get("https://opentdb.com/api.php?", params = parameters)
response.raise_for_status()
question = response.json()
question_data = question['results']
#question_data = [
#                 {"question":"The word &quot;news&quot; originates from the first letters of the 4 main directions on a compass (North, East, West, South).","correct_answer":"False"},
#                 {"question":"An eggplant is a vegetable.","correct_answer":"False"},
#                 {"question":"Kissing someone for one minute burns about 2 calories.","correct_answer":"True"},
#                 {"question":"Sitting for more than three hours a day can cut two years off a person&#039;s life expectancy.","correct_answer":"True"},
#                 {"question":"The French word to travel is &quot;Travail&quot;","correct_answer":"False"},
#                 {"question":"Albert Einstein had trouble with mathematics when he was in school.","correct_answer":"False"},
#                 {"question":"Francis Bacon died from a fatal case of pneumonia while he was attempting to preserve meat by stuffing a chicken with snow.","correct_answer":"True"},
#                 {"question":"Popcorn was invented in 1871 by Frederick W. Rueckheim in the USA where he sold the snack on the streets of Chicago.","correct_answer":"False"},
#                 {"question":"The commercial UK channel ITV stands for &quot;International Television&quot;.","correct_answer":"False"},
#                 {"question":"Instant mashed potatoes were invented by Canadian Edward Asselbergs in 1962.","correct_answer":"True"}
# ]