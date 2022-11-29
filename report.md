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
as code if it is valid html. An attacker could send a message with a script -tag
and a nasty JS program with it. This way the attacker could fish out user
messages, or other sensitive information from alice's computer when she loades
the page.

This flaw can be fixed by removing the "|safe" part from the variable in the
html. This way the message contents are interpreted just as text.

FLAW 3: ...  
Broken access control

A route is missing an authentication check, allowing anyone to access admin data
manually.  
...

FLAW 4:
[Weak password hashing](https://github.com/ronituohino/cybersecurity-project/blob/main/config/settings.py#L114)

Passwords in the database stored as hashes. However, they have been hashed using
the MD5 algorithm, which is easily reversable. If attackers were to gain access
to the database, they could easily find valid user credentials by reversing the
hashes.

To fix this issue, one should just remove the explicitly defined hasher in the
settings file. This would make Django default to SHA256 hashing, which is way
more secure.

FLAW 5:
[Possibly sensitive info in git](https://github.com/ronituohino/cybersecurity-project/blob/main/db.sqlite3)

The development database is
[in github](https://github.com/ronituohino/cybersecurity-project/blob/main/db.sqlite3)
containing developer credentials. Some of these could end up in production for
superusers, and possibly free access to the production server for the attackers.

The SECRET_KEY used in development is in an
[early git commit](https://github.com/ronituohino/cybersecurity-project/commit/898fba165ad779d2ba5ba9d3445314dea535c4bc),
which might be the same used in production. Leaking this, according to Django,
"can lead to privilege escalation and remote code execution vulnerabilities."

To fix these issues, either the information has to be removed from the git
history, or it has to be made sure none of it is used in production. To remove
this information, the git history has to be deleted, which could be achieved by
creating a new repository.
