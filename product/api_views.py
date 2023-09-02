from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from order.models import OrderDetail
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer
from utils.paginator import StandardResultsSetPagination


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        category = request.GET.get('category', None)
        queryset = self.get_queryset()
        if category:
            queryset = queryset.filter(category=category)

        page = self.paginate_queryset(queryset)
        if page is not None:
            data = []
            for obj in page:
                data.append({
                    "id": obj.id,
                    "name": obj.name,
                    "price": obj.price,
                    "image": 'http://127.0.0.1:8000' + obj.imageURL,
                    "quantity": obj.quantity,
                    "category": obj.category.id
                })
            return Response(data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print(request.data)
        product = Product.objects.create(
            name=request.data.get('name'),
            price=request.data.get('price')
        )
        return Response(data={'data': 'Yaratildi'}, status=201)

    def destroy(self, request, *args, **kwargs):
        print('destroy................', args, kwargs)
        return Response(status=202)


class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CartViewSet(ModelViewSet):
    queryset = OrderDetail.objects.all()
    permission_classes = [IsAuthenticated,]
    def list(self, request, *args, **kwargs):
        user = request.user
        order_details = OrderDetail.objects.filter(order__customer=user)
        return Response({'items':[
            {
                'item_id':item.id,
                'order_id':item.order.id,
                'product':item.product.name,
                'quantity':item.quantity,
                'price':item.total_price()
            }
            for item in order_details
        ]})