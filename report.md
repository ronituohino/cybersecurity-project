LINK: https://github.com/ronituohino/cybersecurity-project

Make sure you have Python installed.

FLAW n: exact source link pinpointing flaw n...  
description of flaw n...  
how to fix it...

FLAW 1: ...  
SQL Injection

A database query doesn't handle user input properly, allowing anyone to inject
their own database query.  
...

FLAW 2: ...  
XSS Injection

A user can send a message which isn't properly handled, and instead interpreted
as code if it is valid html.  
...

FLAW 3: ...  
Broken access control

A route is missing an authentication check, allowing anyone to access admin data
manually.  
...

FLAW 4: ...  
Cryptographic failure, password hashing

Passwords are hashed using the MD5 algorithm, which is easily reversable.  
...

FLAW 5: ...  
Cryptographic failure, sensitive information in git

The development database is
[in github](https://github.com/ronituohino/cybersecurity-project/blob/main/db.sqlite3)
containing developer credentials. Some of these could end up in production for
superusers.

The SECRET_KEY used in development is in an
[early git commit](https://github.com/ronituohino/cybersecurity-project/commit/000126a1e16229100606a6681958d8f18db486e1),
which might be the same used in production.  
...
