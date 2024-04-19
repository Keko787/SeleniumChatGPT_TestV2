from ChatGPTScraper import ChatGpt

import pytest

# Presenter Kevin

@pytest.fixture(scope="class")
def chatbot():
    """Fixture to initialize ChatGpt and open the chat session."""
    bot = ChatGpt()
    return bot


@pytest.mark.usefixtures("chatbot")
class TestChatGpt:
    def test_single(self, chatbot):
        chatbot.openChatGpt()
        responseString = chatbot.sendFirstMessage("Hello ChatGPT")
        print("\n", responseString)
        assert "Hello" or "Hi" in responseString, "The response should include a greeting."
        chatbot.stopScraper()

    def test_multiple(self, chatbot):
        chatbot.openChatGpt()
        responseString = chatbot.sendFirstMessage("Hello ChatGPT")
        print("\n", responseString)

        responseString = chatbot.sendConversationMessage("Hello ChatGPT Again", 5)
        print("\n", responseString)

        assert len(responseString) > 0, "Expected a non-empty response."
        chatbot.stopScraper()


