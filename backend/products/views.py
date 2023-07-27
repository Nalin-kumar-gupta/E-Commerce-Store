from rest_framework import generics, status, filters
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

from rest_framework.views import APIView


class ProductSearchAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('q', '')
        return Product.objects.filter(name__icontains=search_query)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        # Get the quantity of products to be bought (assuming it's passed in the request data)
        quantity = self.request.data.get('quantity', 1)

        # Get the current product instance
        product = self.get_object()

        # Check if there are enough products in stock
        if product.stock >= quantity:
            product.stock -= quantity
            product.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Not enough stock available."}, status=status.HTTP_400_BAD_REQUEST)

class ProductRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
