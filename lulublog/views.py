from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from .forms import *
from itertools import chain
from operator import attrgetter
from django.views.generic import ListView
from .filters import *
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from .models import *


# Create your views here


def all_posts_index(request):
    lulu_post = LuluPost.objects.all()
    pet_post = PetPost.objects.all()
    result_list = list(reversed(sorted(
        chain(lulu_post, pet_post),
        key=attrgetter('publ_date'))))
    paginator = Paginator(result_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    post_count = len(result_list)
    return render(request, "index.html", {'post_count': post_count, 'page_obj': page_obj})


def lulu_posts_list(request):
    lulu_qs = LuluPost.objects.all()
    lulu_filter = LuluFilter(request.GET, queryset=lulu_qs)
    lulu_qs = lulu_filter.qs
    return render(request, 'lulu_posts_list.html', {'lulu_qs': lulu_qs, 'lulu_posts_list': lulu_filter})


def pet_posts_list(request):
    pet_qs = PetPost.objects.all()
    pet_filter = PetFilter(request.GET, queryset=pet_qs)
    pet_qs = pet_filter.qs
    return render(request, 'pet_posts_list.html', {'pet_qs': pet_qs, 'pet_posts_list': pet_filter})


def lulu_single_post(request, pk):
    specific_lulu_post = get_object_or_404(LuluPost, pk=pk)
    return render(request, 'lulu_single_post.html', {'lulu_single_post': specific_lulu_post})


@login_required
def add_comment_to_lulu_post(request, pk):
    lulu_post = get_object_or_404(LuluPost, pk=pk)
    if request.method == "POST":
        form = LuluPostCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = lulu_post
            new_comment.save()
            return redirect('lulu_single_post', pk=lulu_post.pk)
    else:
        form = LuluPostCommentForm()
    return render(request, 'add_comment_to_lulu_post.html', {'form': form, 'lulu_post': lulu_post})


def pet_single_post(request, pk):
    specific_pet_post = get_object_or_404(PetPost, pk=pk)
    return render(request, 'pet_single_post.html', {'pet_single_post': specific_pet_post})


@login_required
def add_comment_to_pet_post(request, pk):
    pet_post = get_object_or_404(PetPost, pk=pk)
    if request.method == "POST":
        form = PetPostCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = pet_post
            new_comment.save()
            return redirect('pet_single_post', pk=pet_post.pk)
    else:
        form = PetPostCommentForm()
    return render(request, 'add_comment_to_pet_post.html', {'form': form, 'pet_post': pet_post})


def create_lulu_story(request):
    if request.method == 'POST':
        lulu_form = LuluForm(request.POST or None)
        if lulu_form.is_valid():
            subject = "Lulu Story"
            body = {
                'lulu_form_sender': lulu_form.cleaned_data['lulu_form_sender'],
                'lulu_form_title': lulu_form.cleaned_data['lulu_form_title'],
                'lulu_form_content': lulu_form.cleaned_data['lulu_form_content'],
                'lulu_form_mail': lulu_form.cleaned_data['lulu_form_mail'],
            }
            message = "\n".join(body.values())
            send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            return render(request, "lulu_thanks.html", {})
        else:
            messages.error(request, 'Formularz zawiera błędy! Lulu prosi o korektę!')
    else:
        lulu_form = LuluForm()
    return render(request, 'your_lulu_story.html', {'lulu_form': lulu_form})


def create_pet_story(request):
    if request.method == 'POST':
        pet_form = PetForm(request.POST, request.FILES)
        if pet_form.is_valid():
            pet_form.save()
            return render(request, "lulu_thanks.html", {})
        else:
            messages.error(request, 'Formularz zawiera błędy! Lulu prosi o korektę!')
    else:
        pet_form = PetForm()
    return render(request, 'your_pet.html', {'pet_form': pet_form})


def display_lulu_thanks(request):
    return render(request, 'lulu_thanks.html', {})


def show_search(request):
    search_post = request.GET.get('search')
    if search_post:
        lulu_posts = LuluPost.objects.filter(Q(title__icontains=search_post) | Q(content__icontains=search_post)
                                             | Q(author__icontains=search_post) | Q(user__username__icontains=search_post))
        pet_posts = PetPost.objects.filter(Q(title__icontains=search_post) | Q(content__icontains=search_post)
                                           | Q(author__icontains=search_post) | Q(pet_name__icontains=search_post)
                                           | Q(pet_species__icontains=search_post) | Q(pet_species_other__icontains=search_post)
                                           | Q(user__username__icontains=search_post))
        lulu_posts_comments = LuluPostComment.objects.filter(Q(content__icontains=search_post)
                                                             | Q(user__username__icontains=search_post))
        pet_posts_comments = PetPostComment.objects.filter(Q(content__icontains=search_post)
                                                           | Q(user__username__icontains=search_post))
        all_posts = sorted(chain(lulu_posts, pet_posts, lulu_posts_comments, pet_posts_comments),
                           key=attrgetter('publ_date'))
    else:
        all_posts = None
    all_posts_count = len(all_posts)
    return render(request, 'search_result.html',
                  {'posts': all_posts, 'search_post': search_post, 'posts_count': all_posts_count})


class UserPostsList(ListView):
    template_name = 'user_posts_list.html'

    def get_queryset(self):
        user_id = self.request.user
        lulu_user_qs = LuluPost.objects.filter(user=user_id)
        pet_user_qs = PetPost.objects.filter(user=user_id)
        qs = sorted(chain(lulu_user_qs, pet_user_qs), key=attrgetter('publ_date'))
        return qs


class AnonymousUserPostsList(ListView):
    template_name = 'anonymous_user_posts_list.html'

    def get_queryset(self):
        lulu_author_id = self.kwargs['user_id']
        pet_author_id = self.kwargs['user_id']
        lulu_author_qs = LuluPost.objects.filter(user_id=lulu_author_id)
        pet_author_qs = PetPost.objects.filter(user_id=pet_author_id)
        qs = sorted(chain(lulu_author_qs, pet_author_qs), key=attrgetter('publ_date'))
        return qs


class AuthorPostsList(ListView):
    template_name = 'author_posts_list.html'

    def get_queryset(self):
        lulu_author_id = self.kwargs['author']
        pet_author_id = self.kwargs['author']
        lulu_author_qs = LuluPost.objects.filter(author=lulu_author_id)
        pet_author_qs = PetPost.objects.filter(author=pet_author_id)
        qs = sorted(chain(lulu_author_qs, pet_author_qs), key=attrgetter('publ_date'))
        return qs


class PetList(ListView):
    template_name = 'pet_list.html'
    context_object_name = 'pet_list'

    def get_queryset(self):
        pet_id = self.kwargs['pet_name']
        qs = PetPost.objects.filter(pet_name=pet_id)
        return qs


class SpeciesList(ListView):
    template_name = 'species_list.html'
    context_object_name = 'species_list'

    def get_queryset(self):
        species_id = self.kwargs['pet_species']
        qs = PetPost.objects.filter(pet_species=species_id)
        return qs


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('all_posts_index')
    template_name = 'delete_account.html'
    success_message = "Twoje konto zostało pomyślnie usunięte."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(UserDelete, self).delete(request, *args, **kwargs)


@login_required
def display_dashboard(request):
    current_user = request.user
    user_lulu_posts = LuluPost.objects.filter(user=current_user)
    user_pet_posts = PetPost.objects.filter(user=current_user)
    all_posts = sorted(chain(user_lulu_posts, user_pet_posts), key=attrgetter('publ_date'))
    return render(request, 'dashboard.html', {'all_posts': all_posts})


@login_required
def create_logged_lulu_story(request):
    if request.method == 'POST':
        lulu_logged_form = LoggedLuluForm(request.POST)
        if lulu_logged_form.is_valid():
            username = lulu_logged_form.save(commit=False)
            username.user = request.user
            username.save()
            return render(request, "lulu_thanks.html", {})
        else:
            messages.error(request, 'Formularz zawiera błędy! Lulu prosi o korektę!')
    else:
        lulu_logged_form = LoggedLuluForm()
    return render(request, 'logged_lulu_story.html', {'lulu_logged_form': lulu_logged_form})


@login_required
def create_logged_pet_story(request):
    if request.method == 'POST':
        pet_username = PetPost(user=request.user)
        pet_logged_form = LoggedPetForm(request.POST, request.FILES, instance=pet_username)
        if pet_logged_form.is_valid():
            pet_username.save()
            return render(request, "lulu_thanks.html", {})
        else:
            messages.error(request, 'Formularz zawiera błędy! Lulu prosi o korektę!')
    else:
        pet_logged_form = LoggedPetForm()
    return render(request, 'logged_pet_story.html', {'pet_logged_form': pet_logged_form})


def edit_lulu_story(request, pk):
    lulu_logged_post = get_object_or_404(LuluPost, pk=pk)
    lulu_logged_form = LoggedLuluForm(request.POST or None, instance=lulu_logged_post)
    if lulu_logged_form.is_valid():
        lulu_logged_form.save()
        return redirect('dashboard')
    return render(request, 'logged_lulu_story.html', {'lulu_logged_form': lulu_logged_form})


def edit_pet_story(request, pk):
    pet_logged_post = get_object_or_404(PetPost, pk=pk)
    pet_logged_form = LoggedPetForm(request.POST or None, request.FILES or None, instance=pet_logged_post)
    if pet_logged_form.is_valid():
        pet_logged_form.save()
        return redirect('dashboard')
    return render(request, 'logged_pet_story.html', {'pet_logged_form': pet_logged_form})


def delete_lulu_story(request, pk):
    lulu_logged_post = get_object_or_404(LuluPost, pk=pk)
    if request.method == 'POST':
        lulu_logged_post.delete()
        messages.success(request, 'Lulu niechętnie wyraziła zgodę i post został usunięty.')
        return redirect('dashboard')
    return render(request, 'delete_confirmation.html', {'lulu_logged_post': lulu_logged_post})


def delete_pet_story(request, pk):
    pet_logged_post = get_object_or_404(PetPost, pk=pk)
    if request.method == 'POST':
        pet_logged_post.delete()
        messages.success(request, 'Lulu niechętnie wyraziła zgodę i post został usunięty.')
        return redirect('dashboard')
    return render(request, 'delete_confirmation.html', {'pet_logged_post': pet_logged_post})


@login_required
def delete_lulu_post_comment(request, pk):
    lulu_comment = get_object_or_404(LuluPostComment, pk=pk)
    if request.method == 'POST':
        lulu_comment.delete()
        messages.success(request, 'Lulu niechętnie wyraziła zgodę i komentarz został usunięty.')
        return redirect('dashboard')
    return render(request, 'comment_delete_confirmation.html', {'lulu_comment': lulu_comment})


@login_required
def delete_pet_post_comment(request, pk):
    pet_comment = get_object_or_404(PetPostComment, pk=pk)
    if request.method == 'POST':
        pet_comment.delete()
        messages.success(request, 'Lulu niechętnie wyraziła zgodę i komentarz został usunięty.')
        return redirect('dashboard')
    return render(request, 'comment_delete_confirmation.html', {'pet_comment': pet_comment})
