========
Helpline
========

Django helpline is a simple helpline app.
The app handles simple call dashboard display. User management and queue managemement.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "dboard" and its dependencies to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'avatar',
        'crispy_forms',
        'django_tables2',
        'django_tables2_reports',
        'debug_toolbar',
        'selectable',
        'faq',
        'dboard',
    ]

2. Include the dboard URLconf in your project urls.py like this::

    from dboard import urls as dboard_urls
    from faq import urls as faq_urls
    ...
    url(r'^dboard/',include(dboard_urls)),
    url(r'^faq/',include(faq_urls)),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to login (you'll need the Admin app enabled).

5. Import fixtures::

    python manage.py loaddata dboard