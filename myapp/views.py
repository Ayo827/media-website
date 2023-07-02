from django.shortcuts import render
from .forms import MultiImageUploadForm
import cloudinary.uploader
import psycopg2
import numpy as np

conn = psycopg2.connect(
    host="lallah.db.elephantsql.com",
    database="suhfcwhc",
    user="suhfcwhc",
    password="PCI5pl30tB8prgMHDRUvCjBKrLxR8E9v"
)

cur = conn.cursor()
# Create your views here.
from django.http import HttpResponse
from django.template import loader



def hello(request):
    array = []
    sql = "SELECT imagename FROM images"
    cur.execute(sql)
    images = cur.fetchall()
    for image in images:
        for i in image:
            print(i)
            array.append(i)
    return render(request, 'myapp/index.html', {'imagesArray': str(array)})


def upload_images(request):
    if request.method == 'POST':
        form = MultiImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('images')
            for image in images:
                # Process each uploaded image (e.g., save to a model or perform image processing)
                # Example: save the image to a model
                # YourModel.objects.create(image_field=image)
                result = cloudinary.uploader.upload(image)
                print(result)
                print(result['url'])
                url = (result['url'])
                cur.execute("INSERT INTO images (imagename) VALUES (%s);", [url])
                # Commit the changes
                conn.commit()

            return render(request, 'myapp/success.html')

        # Close the cursor and connection
        cur.close()
        conn.close()
    else:
        form = MultiImageUploadForm()

    return render(request, 'myapp/upload_images.html', {'form': form})


