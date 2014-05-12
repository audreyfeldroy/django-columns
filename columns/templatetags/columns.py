"""
Template filters to partition lists into columns.

A common use-case is for splitting a list into 2 lists, to fill 2 columns::

    {% load columns %}

    <div class="row">
        {% for col in mylist|columns:3 %}
            <div class="col-md-4">
                {% for item in col %}
                    <div class="item">{{ item }}</div>
                {% endfor %}
            </div><!-- /col-md-4 -->
        {% endfor %}
    </div><!-- /row -->

Code adapted from https://djangosnippets.org/snippets/401/ 

"""

from django.template import Library

register = Library()

def columns(thelist, n):
    """
    Break a list into ``n`` columns, filling up each row to the maximum equal
    length possible. For example::

        >>> l = range(10)

        >>> columns(l, 2)
        [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]

        >>> columns(l, 3)
        [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]

        >>> columns(l, 4)
        [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

        >>> columns(l, 5)
        [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]

        >>> columns(l, 9)
        [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [], [], [], []]

        # This filter will always return `n` columns, even if some are empty:
        >>> columns(range(2), 3)
        [[0], [1], []]
    """
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    list_len = len(thelist)
    split = list_len // n

    if list_len % n != 0:
        split += 1
    return [thelist[split*i:split*(i+1)] for i in range(n)]


register.filter(columns)
