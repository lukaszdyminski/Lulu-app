# Lulu-app
My first django project 'lulu_project' is basic blog/social site, create entirely of Django technology and 'raw' HTML/CSS made-by-beginner code. No frontend framework was used (with exception of a few Bootstrap code lines).

App in 'lulu_project': Blog app part is about adding admin posts, which are short stories about his dog named Lulu. Social media app part lets external blog users add their own posts about Lulu or create separate posts about their own pet. The user can add posts both logged in and not logged in. In logged in mode, he has the ability to edit posts, delete them, add comments, etc.

App structure: The blog is based on 2 models: posts about Lulu and posts about the user's pet. The "user" instance is added to both models as ForeignKey. It was used as the generic User model here. In addition, I created a list of posts - separate for each model, as well as filters, filtering individual instances of models: date, author, pet name or animal species.

