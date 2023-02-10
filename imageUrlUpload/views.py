from django.shortcuts import render,redirect
from .forms import DocumentForm

from django.core.files.storage import FileSystemStorage
# from django import render
def fileStorageImage(request):
    if request.method == "POST":
        # if the post request has a file under the input name 'document', then save the file.
        request_file = request.FILES['document'] if 'document' in request.FILES else None
        if request_file:
                # save attached file

                # create a new instance of FileSystemStorage
                fs = FileSystemStorage()
                print(fs)
                file = fs.save(request_file.name, request_file)
                print(file)
                # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
                file_url = fs.url(file)
                print(file_url)
        
                return render(request, "upload.html",{'fileurl':file_url})
    return render(request, "upload.html")



