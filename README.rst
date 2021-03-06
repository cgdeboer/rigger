Rigger: (R)andom (I)dentity (G)eneration
========================================
.. image:: https://travis-ci.org/cgdeboer/rigger.svg?branch=master
    :target: https://travis-ci.org/cgdeboer/rigger

.. image:: https://img.shields.io/pypi/v/rigger.svg
    :target: https://pypi.org/project/rigger/

**Rigger** is a (r)andom (i)dentity (g)enerator implemented in pure python,
inspired by RIG_. **Rigger** creates a name, physical mailing address, phone number,
and email along with a geographically consistent (ie, they all match the same area)
city, state, ZIP code, and area code. Currently it is United States identities only.

.. _RIG: https://www.unix.com/man-page/debian/6/RIG/

.. image:: https://raw.githubusercontent.com/cgdeboer/rigger/master/docs/rigger.png
   :height: 150px

**Example Code:**

.. code-block:: python

    >>> import rigger

    >>> rigger.identity()

    >>> {'name': 'Briella Doyle',
         'given': 'Briella',
         'family': 'Doyle',
         'address': '413 White Mud St',
         'city': 'Richford',
         'state': 'VT',
         'zip_code': '05476',
         'phone': '802-755-1984',
         'email': 'bdoyle@yahoo.com'}

    >>> rigger.identity(gender="f")

    >>> {'name': 'Eve Anderson',
         'given': 'Eve',
         'family': 'Anderson',
         'address': '3756 New Jungle St',
         'city': 'Ohio',
         'state': 'IL',
         'zip_code': '61349',
         'phone': '309-732-7616',
         'email': 'eanderson@icloud.com'}


How It Works
---------------
**Rigger** provides an easy way to generate random identities that look mostly real. Cities,
states, and zip codes are consistent, and phone area codes are valid at the state level.
**Rigger** provides a single function, ``identity()``, which takes an optional `gender` kwarg, for
names that are traditionally male or female.

Originally, *RIG* (authored in the 90s) claimed it was useful for
*"feeding the NY times registration page to fend off junk (snail) mail"*.
*Rigger* has more modern purposes: perhaps to mock identities in unit testing, or anonymize production data,
and other some other creative purpose.

Rigger officially supports Python 3.6+.

Installation
------------

To install Rigger, use `pipenv <http://pipenv.org/>`_ (or pip, or poetry, of course):

.. code-block:: bash

    $ pipenv install rigger


How to Contribute
-----------------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request. Make sure to add yourself to AUTHORS_.

.. _`the repository`: https://github.com/cgdeboer/rigger
.. _AUTHORS: https://github.com/cgdeboer/rigger/blob/master/AUTHORS.rst
