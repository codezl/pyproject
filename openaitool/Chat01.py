import os
import openai




def getAiResponse() -> object:
    """

    :rtype: object
    """
    openai.api_key = "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"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="You: How do I combine arrays?\nJavaScript chatbot: You can use the concat() method.\nYou: How do you make an alert appear after 10 seconds?\nJavaScript chatbot",
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
    )


if __name__ == '__main__':
    print(getAiResponse())
