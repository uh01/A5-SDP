# from django.shortcuts import render
# from cars.models import CarsModel
# from brands.models import BrandsModel

# def base(request):
#     return render(request, 'base.html')

# def home(request, brands_slug=None):
#     cars = CarsModel.objects.all()
#     if brands_slug is not None:
#         brands = BrandsModel.objects.get(slug = brands_slug)
#         cars = CarsModel.objects.filter(brands = brands)
#     brands = BrandsModel.objects.all()
#     return render(request, 'home.html', {'cars' : cars, 'brands' : brands})


from django.shortcuts import render
from cars.models import CarsModel
from brands.models import BrandsModel

def base(request):
    return render(request, 'base.html')

def home(request, brands_slug=None):
    cars = CarsModel.objects.all()
    if brands_slug is not None:
        brands = BrandsModel.objects.get(slug = brands_slug)
        cars = CarsModel.objects.filter(brands = brands)
    brands = BrandsModel.objects.all()
    return render(request, 'home.html', {'cars' : cars, 'brands' : brands})






# from django.shortcuts import render, get_object_or_404, redirect
# from cars.models import CarsModel
# from brands.models import BrandsModel

# def base(request):
#     return render(request, 'base.html')

# def home(request, brands_slug=None):
#     cars = CarsModel.objects.all()
#     brands = BrandsModel.objects.all()

#     if brands_slug == "None":
#         # Handle the case where brands_slug is "None"
#         return redirect('home')  # Redirect to the home page or another appropriate URL

#     if brands_slug:
#         brand = get_object_or_404(BrandsModel, slug=brands_slug)
#         cars = CarsModel.objects.filter(brands=brand)

#     return render(request, 'home.html', {'cars': cars, 'brands': brands})