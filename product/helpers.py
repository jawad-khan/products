from datetime import datetime
from django.conf import settings


def handle_uploaded_file(f, file_name):
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def append_base_path(data, key, many=False):
    if many:
        for item in data:
            item[key] = settings.BASE_DIR + item[key]
        return data;
    else:
        data[key] = settings.BASE_DIR + data[key]
        return data

def image_processing(request, key, store_key):
    image_file = request.FILES[key]
    image_extension = image_file.name.split(".")[-1].lower()
    file_name = settings.MEDIA_URL + datetime.now().isoformat() + "-" + store_key + "." + image_extension
    handle_uploaded_file(image_file, settings.BASE_DIR + file_name)
    return file_name
