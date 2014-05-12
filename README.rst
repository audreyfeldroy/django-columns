=============================
django-columns
=============================

.. image:: https://badge.fury.io/py/django-columns.png
    :target: https://badge.fury.io/py/django-columns

.. image:: https://travis-ci.org/audreyr/django-columns.png?branch=master
    :target: https://travis-ci.org/audreyr/django-columns

.. image:: https://coveralls.io/repos/audreyr/django-columns/badge.png?branch=master
    :target: https://coveralls.io/r/audreyr/django-columns?branch=master

Django template filter for splitting a list into columns.

Documentation
-------------

The full documentation is at https://django-columns.readthedocs.org.

Quickstart
----------

1. Install the package. At the command line::

    $ pip install django-columns

2. Add `columns` to `INSTALLED_APPS`.

3. Split a list into 2 lists, to fill 2 columns::

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
