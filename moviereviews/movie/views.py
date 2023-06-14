from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from .models import Movie, Review
from .forms import ReviewForm
from rest_framework import generics
from .serializers import MovieSerializer
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def base_page(request) -> None:
    return render(
            request,
            'movie/basepage.html'
    )


def home(request: HttpRequest) -> None:
    if search_term := request.GET.get('searchMovie'):
        movies = Movie.objects.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()
    return render(
        request, 'movie/home.html',
        {'searchTerm': search_term, 'movies': movies}
    )


def detail(request: HttpRequest, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    return render(request, 'movie/detail.html',
                  {'movie': movie, 'reviews': reviews})


@csrf_exempt
@login_required
def createreview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        return render(
            request, 'movie/createreview.html',
            {'form': ReviewForm(), 'movie': movie}
        )
    else:
        try:
            form = ReviewForm(request.POST)
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.movie = movie
            new_review.save()
            return redirect('detail', new_review.movie.id)
        except ValueError:
            return render(
                request, 'movie/createreview.html',
                {'form': ReviewForm(), 'error': 'bad data passed in'}
            )


@login_required
def updatereview(request, review_id):
    review = get_object_or_404(
        Review, pk=review_id, user=request.user)

    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'movie/updatereview.html',
                      {'review': review, 'form': form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.movie.id)
        except ValueError:
            return render(
                            request,
                            'movie/updatereview.html',
                            {
                                'review': review, 'form': form,
                                'error': 'Bad data in form'
                            }
                          )


@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.movie.id)


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
