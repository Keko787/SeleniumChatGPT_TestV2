import pytest
from ChatGPTScraper import ChatGpt

#Presenter Aidan/Kevin

@pytest.fixture(scope="class")
def chatbot():
    """Fixture to initialize ChatGpt and open the chat session."""
    bot = ChatGpt()
    return bot


@pytest.mark.usefixtures("chatbot")
class TestCalculation:
    def test_arithmetic(self, chatbot):
        chatbot.openChatGpt()
        responseString = chatbot.sendFirstMessage("What is 4 * 4")
        assert "16" in responseString

        responseString = chatbot.sendConversationMessage(
            "Allen finds $109.43 while visiting Nevada. He wants to distribute his money evenly to his 4 friends. If $10.51 is lost on the way back to Denver, how much money will each of his friends receive when he returns?",
            5)
        assert "24.73" in responseString

        responseString = chatbot.sendConversationMessage("Which of these is a monomial?: 3x^2 or 5x^-3", 7)
        assert "\n3x\n2\n" in responseString

        responseString = chatbot.sendConversationMessage("5/x+8 < 0 in interval notation", 9)
        assert "(-5/8, 0)" in responseString

        responseString = chatbot.sendConversationMessage("log base 2, 16", 11)
        assert "4" in responseString

        chatbot.stopScraper()

    def test_wordProblems(self, chatbot):
        chatbot.openChatGpt()
        responseString = chatbot.sendFirstMessage("An airplane accelerates down a runway at 3.20 m/s2 for 32.8 s until is finally lifts off the ground. Determine the distance traveled before takeoff.")
        assert "1720" in responseString

        responseString = chatbot.sendConversationMessage(
            "A car starts from rest and accelerates uniformly over a time of 5.21 seconds for a distance of 110 m. Determine the acceleration of the car.",
            5)
        assert "8.10" in responseString

        responseString = chatbot.sendConversationMessage("Upton Chuck is riding the Giant Drop at Great America. If Upton free falls for 2.60 seconds, what will be his final velocity and how far will he fall?", 7)
        assert "33.1" or "25.5" in responseString

        responseString = chatbot.sendConversationMessage("A race car accelerates uniformly from 18.5 m/s to 46.1 m/s in 2.47 seconds. Determine the acceleration of the car and the distance traveled.", 9)
        assert "11.2" or "79.8" in responseString

        responseString = chatbot.sendConversationMessage("A feather is dropped on the moon from a height of 1.40 meters. The acceleration of gravity on the moon is 1.67 m/s2. Determine the time for the feather to fall to the surface of the moon.", 11)
        assert "1.29" in responseString

        chatbot.stopScraper()