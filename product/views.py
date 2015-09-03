from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, authentication
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.conf import settings
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from models import product
from serializers import product_serializer, user_serializer, address_serializer, user_product_serializer,image_serializer,complete_profile
from rest_framework_expiring_authtoken.authentication import ExpiringTokenAuthentication
from django.http.request import QueryDict
# Create your views here.



@api_view(['POST'])
def signup(request):


    arranged_data=dict(request.data.dict())
    arranged_data['phone']={'phone':request.data['phone']}
    user = user_serializer(data=arranged_data)
    if user.is_valid():
        new_user = user.save()
        user.data['id'] = new_user.id
        return Response(user.data, status=status.HTTP_201_CREATED)
    else:
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def products(request):
    if request.method == 'POST':
        form = product_serializer(data=request.data)
        if (form.is_valid()):
            form.save()
            return Response(form.data, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        objects = product_serializer(product.objects.all(), many=True)
        return Response(objects.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def delete_product(request, id):
    try:
        object = product.objects.get(pk=id)
        object.delete()
    except product.DoesNotExist as error:
        return Response(error.message, status=status.HTTP_404_NOT_FOUND)
    except BaseException as error:
        return Response(error.message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    return Response({"success": "1"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def user_products(request):
    id=request.user.id
    if request.method == "GET":
        try:
            objects = User.objects.get(pk=id).user_product_set.all()
        except User.DoesNotExist as error:
            return Response(error.message, status=status.HTTP_404_NOT_FOUND)
        list = []
        for object in objects:
            list.append(object.product)
        objects = product_serializer(list, many=True)
        return Response(objects.data, status=status.HTTP_200_OK)
    else:
        customized_data=request.data
        customized_data['user']=id
        new_product = user_product_serializer(data=customized_data)
        if new_product.is_valid():
            new_product.save()
            return Response({"success": "1"}, status=status.HTTP_201_CREATED)
        else:
            return Response(new_product.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def Edit_product(request, id):
    try:
        object = product.objects.get(pk=id)
    except product.DoesNotExist as error:
        return Response(error.message, status=status.HTTP_404_NOT_FOUND)
    form = product_serializer(object, data=request.data);
    if (form.is_valid()):
        form.save();
        return Response(form.data, status=status.HTTP_200_OK)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def addres(request):
    if request.method == 'POST':
        customized_data=request.data
        customized_data['user']=request.user.id
        new_address = address_serializer(data=customized_data)
        if new_address.is_valid():
            new_address.save()
            return Response(new_address.data, status.HTTP_201_CREATED)
        else:
            return Response(new_address.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        try:
            objects = address_serializer(request.user.address_set.all(), many=True)
        except addres.DoesNotExist as error:
            return Response(error.message, status=status.HTTP_404_NOT_FOUND)
        return Response(objects.data, status=status.HTTP_200_OK)



def handle_uploaded_file(f):
    with open(settings.BASE_DIR+settings.MEDIA_URL+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@api_view(['POST'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def upload_image(request):
    image=image_serializer(data=request.data)
    if image.is_valid():
        handle_uploaded_file(request.FILES['image'])
        request.user.phone.image=settings.MEDIA_URL+request.FILES['image'].name
        request.user.phone.save()
        return Response({"success":"success"},status=status.HTTP_200_OK)
    else:
        return Response(image.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def profile(request):

    profile_data=complete_profile(request.user.phone)
    temp=profile_data.data
    temp['image']=settings.BASE_DIR + temp['image']
    return  Response(temp,status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes((ExpiringTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def logout(request):
    try:
        request.user.auth_token.delete()
    except Exception as error:
        return Response(error.message,status=status.HTTP_400_BAD_REQUEST)
    return Response({"Message":"User has been logged out"},status=status.HTTP_200_OK)