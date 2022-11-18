# Input-Flask-Form
>>>>    Basic Flask Form to Collect Input Data

To run it,

first, in the terminal clone the repository and "cd" to directory "12-Input-Flask-Form"

    $ git clone https://github.com/vi-u/12-Input-Flask-Form.git   

then

    $ cd 12-Input-Flask-Form

second, in the terminal run command to start web server in your browser

    $ python flaskInputForm.py

third, in your browser open this page:

    localhost:5000/input


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
