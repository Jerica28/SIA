from django.shortcuts import render, redirect, get_object_or_404
from .models import Food
from .forms import FoodForm


def index(request):
    return redirect('food_list')


def food_list(request):
    foods = Food.objects.all()
    return render(request, 'InvApp/food_list.html', {'foods': foods})


def food_add(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('food_list')

        # If the form is invalid, show the dashboard again.
        foods = Food.objects.all()
        return render(
            request,
            'InvApp/food_list.html',
            {'foods': foods, 'form': form}
        )

    return redirect('food_list')


def food_update(request, food_id):
    food = get_object_or_404(Food, food_id=food_id)

    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)

        if form.is_valid():
            form.save()
            return redirect('food_list')

        foods = Food.objects.all()
        return render(
            request,
            'InvApp/food_list.html',
            {'foods': foods, 'form': form, 'editing_food': food}
        )

    return redirect('food_list')


def food_delete(request, food_id):
    if request.method == 'POST':
        food = get_object_or_404(Food, food_id=food_id)
        food.delete()

    return redirect('food_list')