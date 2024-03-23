from random import choice, randint




def get_responses (user_input : str) -> str :
    lowered : str = user_input.lower()

    if lowered == '' : 
        return "Well, you\'re awfully silent"

    elif 'hello' in lowered : 
        return "Oh hello there!"

    elif 'how are you' in lowered : 
        return 'Good thanks'

    elif 'bye' in lowered : 
        return 'Good bye'

    elif 'roll dice' in lowered : 
        return f'You rolled a {randint(1, 6)}'

    else :
        return choice ([
            'I dont understand',
            'What are talking about',
            'Do you mind rephrasing pls ?'])

   


