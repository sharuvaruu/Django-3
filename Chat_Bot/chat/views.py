# chat/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatHistory
from .serializers import ChatHistorySerializer
import openai
from django.shortcuts import render 
class ChatBotView(APIView):
    def post(self, request):
        user_chat = request.data.get('user_chat')

        # Set your OpenAI API key here
        openai.api_key = 'sk-proj-DO02sWUZenKEh5xB9LzOT3BlbkFJih4UiWhrwEiZh43JzLCB'

        try:
            # Use the GPT model to generate a response based on user input
            response_chat = openai.Completion.create(
                engine="text-davinci-002",  # Choose your preferred GPT model
                prompt=user_chat,
                max_tokens=50  # Adjust token count based on your needs
            ).choices[0].text.strip()

            # Save chat history
            chat_history = ChatHistory.objects.create(
                user=request.user,  # Assuming authentication is implemented
                user_chat=user_chat,
                response_chat=response_chat
            )

            # Serialize chat history data
            serializer = ChatHistorySerializer(chat_history)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ChatHistoryListView(APIView):
    def get(self, request):
        chat_history = ChatHistory.objects.all()
        serializer = ChatHistorySerializer(chat_history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def chat_history_view(request):
    chat_history = ChatHistory.objects.all()
    return render(request, 'chat_history.html', {'chat_history': chat_history})
