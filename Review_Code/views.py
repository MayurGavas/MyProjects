from django.shortcuts import render

<<<<<<< HEAD
load_dotenv()  # Loads variables from .env
api_key = os.getenv("OPENAI_API_KEY")
class codeReviewerView(APIView):
    def post(self,request):
        function_code = request.data.get("code","")

        if not function_code:
            return Response({"error" : "No code provided"},status=status.HTTP_400_BAD_REQUEST)

        try:
            client = openai.OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = [
                    {
                        "role": "system",
                        "content": "You are an expert software engineer and code reviewer. Provide inline comments for the given Python function. Focus on best practices, performance, readability, and security."
                    },
                    {
                        "role": "user",
                        "content": f"Please review the following function and provide inline comments:\n\n{function_code}"
                    }
                ]
            )
            suggessions = response[0].message.content
            return Response({"comments" : suggessions},status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
=======
# Create your views here.
>>>>>>> parent of 3705a89 (made changes)
