from django.shortcuts import render

# view function for the "../" request as defined in the urls.py
def starting_page(request):
    return render(request, "information_base/index.html")
