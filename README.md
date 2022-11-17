# Input-Flask-Form
>>>>    Basic Flask Form to Collect Input Data

To run it,

first, clone it and "cd" to directory "Input-Flask-Form"

    $ git clone https://github.com/vi-u/Input-Flask-Form.git   

then

    $ cd Input-Flask-Form

second, run command to start web server in your browser

    $ python flaskInputForm.py

third, open this page in your browser:

    localhost/5000/input


****

The request.form has a dictionary structure:

    form_data = {
    'key1(field1_name)' : 'value1(field1_value)',
    'key2(field2_name)' : 'value2(field2_value)',
    .
    .
    }


*****

templates use Jinja2 Templating Language

Types	                Syntax

1) Statement Tags	{% %}: {% if…..else %} – {% endif %}
2) Variable Tags	{{ }}: {{ variable }}
3) Commenting Tags	{#…..#}: {# comment ….para #}
4)Line Comment Tags	#: #comment line
