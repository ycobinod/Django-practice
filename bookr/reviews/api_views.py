# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Book
# from .serializers import BookSerializer

# @api_view()
# def all_book(request):
#     book=Book.objects.all()
#     book_serializer=BookSerializer(book,many=True)
#     return Response (book_serializer.data)

# from rest_framework import generics
# from .models import Book
# from  .serializers import BookSerializer

# class AllBooks(generics.ListAPIView):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer

