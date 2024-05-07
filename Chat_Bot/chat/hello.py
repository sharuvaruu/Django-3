import openai

# Assuming you have your OpenAI API key set up (replace with your actual key)
openai.api_key = "sk-proj-jiPk74FkVm1Yum954yb2T3BlbkFJkITFzhZ6Cknsmw4c5AZh"

# Choose a suitable model based on your needs (replace with a valid model name)
model_name = "gpt-3.5-turbo-instruct"  # Example: Creative text generation

try:
  # Reduce max_tokens initially to limit API usage per request
  response = openai.Completion.create(
      engine=model_name,
      prompt="Your prompt here",
      max_tokens=500,  # Adjust based on your needs
      n=1,
      stop=None,
      temperature=0.7,
  )
  print(response.choices[0].text)
except openai.error.Error as e:
  # Handle different error types (e.g., AuthenticationError, RateLimitError)
  if isinstance(e, openai.error.AuthenticationError):
      print("Authentication Error: Check your API key.")
  elif isinstance(e, openai.error.RateLimitError):
      print("Rate Limit Error: Exceeded quota. Consider monitoring usage or upgrading plan.")
  else:
      print(f"API error: {e}")
