from django import template

# decorated function enabling the blog posts reverse ordering using pagination

register = template.Library()


@register.simple_tag
def pagination_reverse_numbering(page_obj, loop_count):
    return page_obj.paginator.count - page_obj.start_index() - loop_count + 1
