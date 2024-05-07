from django.contrib import admin
from django.urls import path
from chat.views import ChatBotView, ChatHistoryListView, chat_history_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chat_history_view, name='home'),  # Define root URL pattern
    path('api/chat/', ChatBotView.as_view(), name='chatbot'),
    path('api/chat-history/', ChatHistoryListView.as_view(), name='chat-history'),
    # Add other URL patterns here if needed
]
