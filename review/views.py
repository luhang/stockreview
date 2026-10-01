from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Review, ReviewImage
from .forms import ReviewForm


def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'review/create.html', {'form': form})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review/list.html', {'reviews': reviews})


def review_detail(request, pk):
    review = get_object_or_404(Review.objects.prefetch_related('images'), pk=pk)
    return render(request, 'review/detail.html', {'review': review})
