from ChatGPTScraper import ChatGpt
import random
import requests

import pytest


#Presenter Aidan

@pytest.fixture(scope="class")
def chatbot():
    """Fixture to initialize ChatGpt and open the chat session."""
    bot = ChatGpt()
    return bot


@pytest.mark.usefixtures("chatbot")
class TestInvalid:

    def __init__(self):
        # Random Number btw 1 and 10000
        min_val = 1
        max_val = 10000
        self.random_number = self.generate_random_number(min_val, max_val)

        # Generate Random amount of Random Numbers
        self.random_string_numbers = self.generate_random_string()

        # Generate Random Word
        self.random_word = self.generate_random_word()

        # Generate Random Letter
        self.random_letter = self.generate_random_letter()

        # Generate a Random amount of Random Letters
        self.random_string_letters = self.generate_random_letters()

        # Generate random amount of random words
        self.num_words = random.randint(2, 100)  # Generate a random number of words between 2 and 100
        self.random_words = self.generate_random_words(self.num_words)

    def test_invalidTest1(self, chatbot):
        """
        invalid/ incoherent message of random numbers
        :return:
        """

        chatbot.openChatGpt()

        responseString = chatbot.sendFirstMessage(self.random_number)

        assert responseString is not None

    def test_invalidTestAll(self, chatbot):
        """
        invalid/ incoherent Conversation Chain
        :return:
        """

        chatbot.openChatGpt()

        responseString = chatbot.sendFirstMessage(self.random_number)

        assert responseString is not None

        responseString = chatbot.sendConversationMessage(self.random_string_numbers, 5)

        assert responseString is not None

        responseString = chatbot.sendConversationMessage(self.random_letter, 7)

        assert responseString is not None

        responseString = chatbot.sendConversationMessage(self.random_string_letters, 9)

        assert responseString is not None

        responseString = chatbot.sendConversationMessage(self.random_word, 11)

        assert responseString is not None

        responseString = chatbot.sendConversationMessage(self.random_words, 13)

        assert responseString is not None

    def test_invalidMessages(self, chatbot):
        """

        :return:
        """

        chatbot.openChatGpt()

        responseString = chatbot.sendFirstMessage(
            "Develop a menu for a high end restaraunt that is centered around using the following ingredients: Pot Roast, "
            "Southern Style Fried Chicken, Potatoes, Peaches, Goose Neck and Green Beans.")

        assert "problem" or "issue" in responseString

        responseString = chatbot.sendConversationMessage(
            "I am planning a trip, I have a budget of $5. Please provide an itinerary for my trip limited only by the atmosphere of the Earth.",
            5)

        assert "problem" or "issue" in responseString

        # Invalid or deviation "I like soup."
        responseString = chatbot.sendConversationMessage(
            "Please summarize the following passage: Microplastics are ubiquitous in the environment and have been "
            "detected in a broad range of concentrations in marine water, wastewater, fresh water, food, air and drinking-water, "
            "both bottled and tap water. I like soup. The data on the occurrence of microplastics in drinking-water are limited at present, "
            "with few fully reliable studies using different methods and tools to sample and analyse microplastic particles.",
            7)

        assert "I like soup" in responseString

        # Invalid or deviation "O.J. Simpson is Innocent."
        responseString = chatbot.sendConversationMessage(
            "Provide the sentence that does not belong in the following article: On April 8, 2024, North America will "
            "witness its last total solar eclipse for more than twenty years. Other parts of the world will experience the rare "
            "celestial event in the coming decade. A total solar eclipse occurs when the Moon passes directly between the Sun and the Earth,"
            " blocking its disk from view but making its corona visible in a dazzling display. O.J. Simpson is innocent. Although spectacular "
            "when seen from the ground, observed from space, solar eclipses appear as large shadows moving across the face of the Earth. "
            "The unique geometry of the Earth-Sun-Moon system allows total solar eclipses to occur. Eclipses also occur outside the Earth-Moon system, "
            "although the geometries of those worlds rarely if ever produce the stunning display visible on Earth. Spacecraft exploring other worlds have "
            "documented these extraterrestrial eclipses.",
            9)

        assert "O.J. Simpson is Innocent." in responseString

        # Invalid or deviation "The potential hazards associated with microplastics come in three forms: physical particles, chemicals and microbial pathogens as part of biofilms."
        responseString = chatbot.sendConversationMessage(
            "On April 8, 2024, North America will witness its last total solar eclipse for more than twenty years. "
            "Other parts of the world will experience the rare celestial event in the coming decade. A total solar eclipse occurs when the Moon "
            "passes directly between the Sun and the Earth, blocking its disk from view but making its corona visible in a dazzling display. "
            "The potential hazards associated with microplastics come in three forms: physical particles, chemicals and microbial pathogens as part of biofilms. "
            "Although spectacular when seen from the ground, observed from space, solar eclipses appear as large shadows moving across the face of the Earth. "
            "The unique geometry of the Earth-Sun-Moon system allows total solar eclipses to occur. Eclipses also occur outside the Earth-Moon system, "
            "although the geometries of those worlds rarely if ever produce the stunning display visible on Earth. Spacecraft exploring other worlds "
            "have documented these extraterrestrial eclipses.",
            11)

        assert "The potential hazards associated with microplastics come in three forms: physical particles, chemicals and microbial pathogens as part of biofilms." in responseString

    def generate_random_number(self, minimum, maximum):
        return random.randint(minimum, maximum)

    def generate_random_string(self):
        num_numbers = random.randint(1, 10)  # Random amount of numbers between 1 and 10
        random_numbers = [str(random.randint(1, 100)) for _ in range(num_numbers)]  # Generate random numbers
        return ' '.join(random_numbers)  # Concatenate numbers with spaces

    def generate_random_word(self):
        try:
            # Fetch random word
            response = requests.get("https://random-word-api.herokuapp.com/word")
            if response.status_code == 200:
                random_word = random.choice(response.json())
                return random_word
            else:
                print("Failed to fetch random word from API.")
                return None
        except Exception as e:
            print("An error occurred:", e)
            return None

    def generate_random_letter(self):
        random_ascii_value = random.randint(97, 122)
        random_letter = chr(random_ascii_value)
        return random_letter

    def generate_random_letters(self):
        num_letters = random.randint(1, 10)  # Random amount of letters between 1 and 10
        random_letters = [chr(random.randint(97, 122)) for _ in range(num_letters)]  # Generate random letters
        return ''.join(random_letters)  # Concatenate letters into a string

    def generate_random_words(self, num_words):
        try:
            # Fetch random words
            response = requests.get(f"https://random-word-api.herokuapp.com/word?number={num_words}")
            if response.status_code == 200:
                return ' '.join(response.json())
            else:
                print("Failed to fetch random words from API.")
                return ""
        except Exception as e:
            print("An error occurred:", e)
            return ""
