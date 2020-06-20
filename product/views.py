from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, authentication
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.conf import settings
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from models import Product, Address
from serializers import ProductSerializer, UserSerializer, AddressSerializer, UserProductSerializer, ImageSerializer, \
    CompleteProfile, CoverSerializer
from rest_framework_expiring_authtoken.authentication import ExpiringTokenAuthentication
from rest_framework_expiring_authtoken import views as rest_views
from helpers import append_base_path,image_processing,handle_uploaded_file
# Create your views here.



@api_view(['POST'])
def signup(request):
    try:
        arranged_data = dict(request.data.dict())
        arranged_data['phone'] = {'phone': request.data['phone']}
        user = UserSerializer(data=arranged_data)
        if user.is_valid():
            new_user = user.save()
            return rest_views.obtain_expiring_auth_token(request)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.message, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def products(request):
    try:
        bought = User.objects.get(pk=request.user.id).userproduct_set.all()
        list = set()
        for object in bought.select_related('product').distinct():
            list.add(object.product)
        products = Product.objects.all().exclude(id__in=bought.values_list('product_id'))
        products = ProductSerializer(products, many=True)
        bought = ProductSerializer(list, many=True)
        customized_data = {'bought': append_base_path(bought.data, 'image', True),
                           'products': append_base_path(products.data, 'image', True), 'staff': request.user.is_staff}
        return Response(customized_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e.message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated, IsAdminUser))
def delete_product(request, id):
    try:
        object = Product.objects.get(pk=id)
        object.delete()
        return Response({"Result": "Product has been deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response(e.message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def user_products(request):
    id = request.user.id
    if request.method == "GET":
        try:
            objects = User.objects.get(pk=id).userproduct_set.all()
            list = []
            for object in objects.select_related('product'):
                list.append(object.product)
            objects = ProductSerializer(list, many=True)
            return Response(append_base_path(objects.data, 'image', True), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            customized_data = request.data
            customized_data['user'] = id
            new_product = UserProductSerializer(data=customized_data)
            if new_product.is_valid():
                new_product.save()
                return Response({"Congratulations": "product has been added successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response(new_product.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes((ExpiringTokenAuthentication, IsAdminUser))
@permission_classes((IsAuthenticated,))
def add_product(request):
    try:
        form = ProductSerializer(data=request.data)
        if form.is_valid():
            form.save()

            return Response(append_base_path(form.data, 'image'), status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes((ExpiringTokenAuthentication, IsAdminUser))
@permission_classes((IsAuthenticated,))
def edit_product(request, id):
    try:
        object = Product.objects.get(pk=id)
        form = ProductSerializer(object, data=request.data);
        if form.is_valid():
            form.save();
            return Response(form.data, status=status.HTTP_200_OK)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def user_address(request):
    if request.method == 'POST':
        try:
            customized_data = request.data
            customized_data['user'] = request.user.id
            new_address = AddressSerializer(data=customized_data)
            if new_address.is_valid():
                new_address.save()
                return Response(new_address.data, status.HTTP_201_CREATED)
            else:
                return Response(new_address.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        try:
            objects = AddressSerializer(request.user.address_set.all(), many=True)
        except Address.DoesNotExist as error:
            return Response(error.message, status=status.HTTP_404_NOT_FOUND)
        return Response(objects.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def upload_image(request):
    try:
        image = ImageSerializer(data=request.data)
        if image.is_valid():
            request.user.phone.image = image_processing(request, 'image', 'profile-' + request.user.username)
            request.user.phone.save()
            return Response({"image": settings.BASE_DIR + request.user.phone.image}, status=status.HTTP_200_OK)
        else:
            return Response(image.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def upload_cover(request):
    try:
        cover = CoverSerializer(data=request.data)
        if cover.is_valid():
            request.user.phone.cover = image_processing(request, 'cover', 'cover-' + request.user.username)
            request.user.phone.save()
            return Response({"cover": settings.BASE_DIR + request.user.phone.cover}, status=status.HTTP_200_OK)
        else:
            return Response(cover.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated, IsAdminUser))
def product_image(request):
    try:
        image = ImageSerializer(data=request.data)
        if image.is_valid():
            product = Product.objects.get(pk=request.data['id'])
            product.image = image_processing(request, 'image', 'product-' + str(product.id))
            product.save()
            return Response({"image": settings.BASE_DIR + str(product.image), "id": product.id}, status=status.HTTP_200_OK)
        else:
            return Response(image.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def profile(request):
    try:
        profile_data = CompleteProfile(request.user.phone)
        customized_data = profile_data.data
        customized_data['image'] = settings.BASE_DIR + customized_data['image']
        customized_data['cover'] = settings.BASE_DIR + customized_data['cover']
        return Response(customized_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e.message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def logout(request):
    try:
        request.user.auth_token.delete()
    except Exception as error:
        return Response(error.message, status=status.HTTP_400_BAD_REQUEST)
    return Response({"Message": "User has been logged out"}, status=status.HTTP_200_OK)