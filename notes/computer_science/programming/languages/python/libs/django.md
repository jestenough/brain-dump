# Django


## **Project structure and layout**

### App modules

**Common** app modules

- `__init__.py`
- `admin.py`
- `forms.py`
- `management/`
- `migrations/`
- `models.py`
- `templatetags/`
- `tests/`
- `urls.py`
- `views.py`

**Uncommon** app modules

- `api/`
- `behaviors.py` - option for locating model mixins
- `constants.py` - app-level settings
- `context_processors.py`
- `decorators.py`
- `db/` - custom model fields or components
- `exceptions.py`
- `fields.py` - form fields (sometimes used for model fields when there isn’t enough field code to justify creating a `db/` package
- `factories.py` - our test data factories
- `helpers.py` - small helper functions (like calculate something) not bigger utils like Logger, workers, etc.
- `managers.py` - when `models.py` too large a common remedy is to move any custom model managers to this model
- `middleware.py`
- `schema.py` - for **GraphQL** APIs
- `signals.py`
- `utils.py` - synonymous with `helpers.py` but for something ***big***
- `viewmixins.py`

### Settings

Instead o having one `settings.py` file with this setup you have a `settings/` directory containing your settings files:

- `__init__.py`
- `base.py` - all instances of the project
- `local.py` - when you’re working on the project locally. Local development-specific settings include ***DEBUG*** mode, log level, and activation of developer tools like [***django-debug-toolbar***](https://github.com/jazzband/django-debug-toolbar)
- `staging.py` - staging version for running a semi-private version o the site on a production server. This is where managers and clients should be looking before your work is modes to production.
- `test.py` - for running tests including test runners, in-memory database definitions, and log settings
- `production.py` - used by your live production server. That is the servers that host the real live website (sometimes called `prod.py`)

You’ll have to use the `--setings` command line option, so you’ll be entering the following at the command-line

```bash
python manage.py shell --setings=config.settings.local
```

```bash
python manage.py runserver --settings=config.settings.local
```

- **Tip: Django settings module and PYTHONPATH**

    A great alternative to using the --settings command line option everywhere
    is to set the DJANGO_SETTINGS_MODULE and PYTHONPATH environment vari-
    able to your desired settings module path. To accomplish this, you’ll need to set
    DJANGO_SETTINGS_MODULE to the corresponding settings module for each envi-
    ronment.
    For those with a more comprehensive understanding of virtualenvwrapper, an-
    other alternative is to set DJANGO_SETTINGS_MODULE and PYTHONPATH in the
    postactivate script and unset them in the postdeactivate script.


```python
# settings/local.py

from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
		'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'testapp',
		'HOST': 'localhost',
	}
}

INSTALLED_APPS += ['debug_toolbar', ]
```

## Code style

### Naming convention


#### App name

Its like a module that means it should have **short**, **all-lowercase name**. Underscores can be used in the module name if it improves readability.
Name Django apps **plural** (if possible)
Examples: polls, users, orders

#### Model

- *naming*: singular nouns, e.g.: Book, Paper, Article, etc.
- *attributes*: use snake_case, singular for One-to-Many relationship, plural for Many-to-Many.
- *related name*: plural in a One-to-Many or Many-to-Many relationship

> dont add model names to fields if there is no need to do, e.g. if table User has field user_status - you should rename the field into status

#### Urls

todo


### Model

_The order of model inner classes and standard methods should be as follows (noting that these are **not all required**):_

1. _Constants (choices, etc.)_
2. _All database fields_
3. _Custom manager attributes_
4. _class Meta_
5. _def __str__()_
6. _def save()_
7. _Any custom methods_
8. _**WHAT ABOUT PROPERTY ??????**_



## **Handling HTTP requests**

### URL dispatcher

> The order of our urls matters




## Testing

### Setup data

Recall that `unittest.TestCase` provides two setup hooks:

- `setUpClass()` - a class method that runs once at the start of the test case class
- `setUp()` - an instance method that runs at the start of each test

Django's *TestCase* adds another hook: the class method `setUpTestData()`. Django runs this as part of the base `setUpClass()`, inside a class-level database `transaction.setUpTestData()` can create data that’s used in all tests, with changes rolled back between tests.

### TestCase Classes

As you know Django provides four (4) test case classes. They have different performance profiles so you need to check to use the right one in each situation. They are list of them _order - fastest first:_

1. `SimpleTestCase` - blocks all database access, so use it when you not need to get access to the database, e.g. for testing some helper function like formating date, etc.
2. `TestCase` - Rolls back database changes using **transactions**.
3. `TransactionTestCase` - Rolls back database changes by flushing each table in the database. Use it when your tests perfom a lot of database operations and data isolations between tests is important to you. _Note. you need to use it when it's necessary to check the work with the database. e.g. if you just create some models to test your views you not need to use it, use **TestCase** instead._
4. `LiveServerTestCase` - Based on _`TransactionTestCase`_ for database rollback. It also launches a live server thread, and is mainly intended for testing with a browserbased tool like _**Selenium**._

Strongly recommended **split** your tests, e.g. if you want to test your model in some places you need to get acces to the database and in others isn't (like constraint check and simple property check). Therefore you could split its tests in two appropriate cases.

### Factories

Factories are functions or classes that provide shorcuts for creating data in yout tests. They can take a lot of pain out of creating data.

For your own factories you can create factory functions.

```python
from django import test
from example.core.models import Author, Book

class ExampleTestMixin:
    def make_author(self, *, name="Leo Tolstoy"):
        author, _created = Author.objects.get_or_create(name=name)
		return author

	def make_book(self, *, author=None, title="War and Peace"):
		if author is None:
			author = self.make_author()
			return Book.objects.create(author=author, title=title)
```

### Unit Tests for a View

## Analyzing
### Count of connection queries

We need only `connection` and `reset_queires` that’s all. Use `reset_queries` each time when do you want to find out the number of requests again.

Make sure your Django `[DEBUG](<https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-DEBUG>)` setting is set to `True`. Then do this:

```python
from django.db import connection, reset_queries

from .models import Test

reset_queries()

Test.objects.get(id=1)
len(connection.queries) # => 1

reset_queries()

Test.objects.get(id=1).foreign.name
len(connection.queries) # => 2

```
