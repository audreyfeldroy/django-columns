========
Usage
========

A common use case is for splitting a list into 2 lists, to fill 2 columns::

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