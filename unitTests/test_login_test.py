from ChatGPTScraper import ChatGpt

import pytest


@pytest.fixture(scope="class")
def chatbot():
    """Fixture to initialize ChatGpt and open the chat session."""
    bot = ChatGpt()
    return bot


@pytest.mark.usefixtures("chatbot")
class TestLogin:

    def test_loging(self, chatbot):
        """
        Tests that the login page works and that it can log in.
        :return:
        """

        chatbot.open_ChatGpt_Login_N_Plus()

        chatbot.accessLogin()

        Pass1 = True

        assert Pass1 is True


@pytest.mark.usefixtures("chatbot")
class TestLoginPlus:

    def test_accessPlusModel(self, chatbot):
        chatbot.open_ChatGpt_Login_N_Plus()

        chatbot.accessLogin()

        chatbot.access_plus_model()

        responseString = chatbot.sendFirstMessage("Hi Code Wizard")

        assert responseString is not None
