from rest_framework.response import Response
from rest_framework.decorators import api_view
from .ai_model import preprocess_question, generate_text_sampling_top_p_nucleus_22

@api_view(['GET'])
def helloWorld(request):
    return Response({'message': 'Hello, world!'})

@api_view(['POST'])
def getAnswer(request):
    question = request.data.get('question')
    answer = generate_text_sampling_top_p_nucleus_22(question)
    return Response({"answer": answer})

@api_view(['POST'])
def preprocess(request):
    question = request.data.get('question')
    return Response({"preprocessed_question": preprocess_question(question)})