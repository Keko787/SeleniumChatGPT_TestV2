import pytest
from ChatGPTScraper import ChatGpt

# Kevin or Jonathan

@pytest.fixture(scope="class")
def chatbot():
    """Fixture to initialize ChatGpt and open the chat session."""
    bot = ChatGpt()
    return bot


@pytest.mark.usefixtures("chatbot")
class TestLongMemory:
    def test_arithmetic_chain(self, chatbot):
        chatbot.openChatGpt()
        responseString = chatbot.sendFirstMessage("What is 2 + 2")
        assert "4" in responseString

        responseString = chatbot.sendConversationMessage("square it", 5)
        assert "16" in responseString

        responseString = chatbot.sendConversationMessage("divide it by 2", 7)
        assert "8" in responseString

        responseString = chatbot.sendConversationMessage("find the square root of that value", 9)
        assert "8" in responseString

        responseString = chatbot.sendConversationMessage("multiply that by one billion", 11)
        assert "2" in responseString
        chatbot.stopScraper()

    def test_conversation(self, chatbot):
        chatbot.openChatGpt()
        responseString = chatbot.sendFirstMessage("Hi, My name is Joe")
        assert "Joe" in responseString, "The response should include the name."

        responseString = chatbot.sendConversationMessage("What is my name?", 5)
        assert "Joe" or "joe" in responseString, "The response should include Joe."

        responseString = chatbot.sendConversationMessage("That's nice, what is your favorite song?", 7)
        assert "music" in responseString, "The response should include a type of music."

        responseString = chatbot.sendConversationMessage("Awesome, do you know where I can find the nearest pharmacy?",
                                                         9)
        assert "go" or "pharmacy" in responseString, "The response should include a location."

        responseString = chatbot.sendConversationMessage("Cool, see you later!", 11)

        assert "goodbye" or "later" in responseString, "The response should include a goodbye."

        chatbot.stopScraper()

