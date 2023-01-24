from django.urls import path
from . import views

# lulublog non-registration content urls

urlpatterns = [
    path('home/', views.all_posts_index, name='all_posts_index'),
        # home url with all lulublog posts paginated list
    path('lulu_stories_list/', views.lulu_posts_list, name='lulu_posts_list'),
        # LuluPost model queryset list url with filters
    path('pet_stories_list/', views.pet_posts_list, name='pet_posts_list'),
        # PetPost model queryset list url with filters
    path('lulu_post/<int:pk>/', views.lulu_single_post, name='lulu_single_post'),
        # LuluPost model single post url with whole story
    path('lulu_post/<int:pk>/comment/', views.add_comment_to_lulu_post, name='add_comment_to_lulu_post'),
        # LuluPost comment form url - user may input a comment to Lulu Story in here including post rate
    path('pet_post/<int:pk>/', views.pet_single_post, name='pet_single_post'),
        # PetPost model single post url with whole story
    path('pet_post/<int:pk>/comment/', views.add_comment_to_pet_post, name='add_comment_to_pet_post'),
        # PetPost comment form url - user may input a comment to Pet Story in here including post rate
    path('your_lulu_story/', views.create_lulu_story, name='create_lulu_story'),
        # LuluForm url - user may input a Lulu Story in here
    path('your_pet_story/', views.create_pet_story, name='create_pet_story'),
        # PetForm url - user may input a Pet Story in here
    path('lulu_thanks/', views.display_lulu_thanks, name='display_lulu_thanks'),
        # Post-submitting PetForm confirmation url
    path('your_dashboard/', views.display_dashboard, name='dashboard'),
        # Welcome url displayed when account login is successful
    path('search_results/', views.show_search, name='show_search'),
        # Search-toolbar results url
    path('author_posts_list/<str:author>/', views.AuthorPostsList.as_view(), name='author_posts_list'),
        # Particular non-registered author stories list url
    path('user_posts_list/<str:user>/', views.UserPostsList.as_view(), name='user_posts_list'),
        # Particular user stories list url
    path('anonymous_user_posts_list/<int:user_id>/', views.AnonymousUserPostsList.as_view(), name='anonymous_user_posts_list'),
        # Particular non-logged-in user stories list url
    path('post_pet_list/<str:pet_name>/', views.PetList.as_view(), name='display_pet_list'),
        # Particular pet name stories list url
    path('post_species_list/<str:pet_species>/', views.SpeciesList.as_view(), name='display_species_list'),
        # Particular pet species stories list url
    path('<int:pk>/delete', views.UserDelete.as_view(), name='delete_account'),
        # Particular user account deleting url
    path('your_dashboard/lulu_story/', views.create_logged_lulu_story, name='create_logged_lulu_story'),
        # Logged-in user may input a Lulu Story in here
    path('your_dashboard/pet_story/', views.create_logged_pet_story, name='create_logged_pet_story'),
        # Logged-in user may input a Pet Story in here
    path('your_dashboard/edit_lulu_story/<int:pk>/', views.edit_lulu_story, name='edit_lulu_story'),
        # Logged-in user may edit a Lulu Story in here
    path('your_dashboard/edit_pet_story/<int:pk>/', views.edit_pet_story, name='edit_pet_story'),
        # Logged-in user may edit a Pet Story in here
    path('your_dashboard/delete_lulu_story/<int:pk>/', views.delete_lulu_story, name='delete_lulu_story'),
        # Logged-in user may delete a Lulu Story in here
    path('your_dashboard/delete_pet_story/<int:pk>/', views.delete_pet_story, name='delete_pet_story'),
        # Logged-in user may delete a Pet Story in here
    path('your_dashboard/delete_lulu_comment/<int:pk>/', views.delete_lulu_post_comment, name='delete_lulu_post_comment'),
        # Logged-in user may delete a Lulu Story comment in here
    path('your_dashboard/delete_pet_comment/<int:pk>/', views.delete_pet_post_comment, name='delete_pet_post_comment'),
        # Logged-in user may delete a Pet Story comment in here
    path('about_lulu_stories/', views.display_lulu_stories_info, name='lulu_stories_info'),
        # url with Lulu Stories blog info
]
