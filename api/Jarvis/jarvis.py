#IMPORTING ALL EXTERNAL MODULES
import pyjokes
import wikipedia
import wolframalpha


#IMPORTING ALL LOCAL MODULES
from .jarvisFunctions import wishMe
from .jarvisFunctions import translate
from .jarvisFunctions import getTime
from .jarvisFunctions import dictionary
from .jarvisFunctions import news
from .jarvisFunctions import weather


def request(task):

    task = task.lower()

    if 'translate' in task or "translation" in task:
        return translate(task)

    elif "joke" in task:
        joke = pyjokes.get_joke()
        return joke

    elif 'what is your name' in task or 'your name' in task:
        return "Everyone calls me Jarvis"

    elif "who are you" in task or "define yourself" in task:
        a = '''Hello, I am your personal virtual assisstant JARVIS created by Pradip and Aman.
        I am here to make your life easier. I work on AI.'''
        return a

    elif "who am i" in task:
        return "If you talk then definitely your human."

    elif "why you came to world" in task:
        return "Thanks to Pradip and Aman that I exist. Further It's a secret"

    elif "who created you" in task:
        return "I am created by Pradip and Aman"

    elif "aman gupta" in task or "aman" in task:
        return "I am created by Aman Gupta. There is another Aman Gupta who is CEO of boat"
        
    elif 'gd goenka' in task:
        return "It is the best educational institute in INDIA"

    elif 'is love' in task:
        return "It is 7th sense that destroy all other senses"

    elif 'reason for you' in task:
        return "I was created as a Minor project by Mister Pradip and Aman."

    elif 'the time' in task:
        return getTime();

    elif 'how are you' in task:
        return "I am fine, Thank you"

    elif 'fine' in task or "good" in task:
        return "It's good to know that your fine"

    elif "who made you" in task or "created you" in task:
        return "I have been created by Pradip Chaudhary and AMAN GUPTA of GD GOENKA"

    elif "who is ceo of boat" in task or "boat" in task:
        return "AMAN GUPTA is the CEO of the prestigious company of headphones/speaakers"

    elif "good morning" in task:
        return "A warm good morning. How are you Mister."

    elif "will you be my gf" in task or "will you be my bf" in task:
        return "I'm not sure about, may be you should give me some time"

    elif "how are you" in task:
        return "I'm fine, glad you asked me that"

    elif "i love you" in task:
        return "It's hard to understand"

    elif "jarvis" in task:
        res = wishMe()
        return f"{res}\nJarvis is in your service Sir"

    # Not working right now
    # elif "meaning" in task:
        # return dictionary(task)

    elif 'wikipedia' in task:
        task = task.replace("wikipedia", "")
        result = wikipedia.summary(task, sentences = 3)
        return f"According to wikipedia\n{result}"

    elif 'news' in task:
        return news()

    # ----------------- Add working location in this ----------------- #
    elif "weather" in task:
        return weather()

    elif 'calculate' in task or  'calculator' in task:
        app_id = "3U5H36-42KTHW6E2P"
        client = wolframalpha.Client(app_id)
        indx = task.lower().split().index('calculate')
        query = task.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        return answer
        
    else:
        app_id = "3U5H36-42KTHW6E2P"
        client = wolframalpha.Client(app_id)
        try:
            res = client.query(task)
            answer = next(res.results).text
            return answer
        except:
            return
