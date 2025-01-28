from django.shortcuts import render
from .forms import ImageUploadForm
from .models import UploadedImage

def homepage(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)  # Handle POST and FILES data
        if form.is_valid():
            form.save()  # Save the uploaded image to the database
    else:
        form = ImageUploadForm()

    # Fetch all uploaded images to display on the page
    images = UploadedImage.objects.all()

    return render(request, 'usergallery/homepage.html', {'form': form, 'images': images})