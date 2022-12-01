LINK: https://github.com/ronituohino/cybersecurity-project  
Make sure you have Python and Django installed.

FLAW 1: CSRF - https://github.com/ronituohino/cybersecurity-project/blob/main/pages/views.py#L11

The `addMessage` route is not properly protected from a CSRF attack: it does not
need a CSRF token to validate the request. Now, attackers could bait the user
into executing a malicious script, and that script could send a valid POST
request for sending a message in the application, impersonating the user. In
this context, it might not be such a damaging vulnerability, but for example, in
a banking application, the possibility of a CSRF attack could have tremendous
impact.

To fix the vulnerability, you need to do two things:

- Remove the @csrf_exempt decorator from the route - https://github.com/ronituohino/cybersecurity-project/blob/main/pages/views.py#L11
- Add a {% csrf_token %} in the html form - https://github.com/ronituohino/cybersecurity-project/blob/main/pages/templates/pages/index.html#L33

This makes Django add a CSRF token to the request, and the backend also requires
and validates the token on a request. It's pretty difficult to screw this one up
when you're making Django apps, since all routes with @login_required require a
CSRF token by default.

FLAW 2: XSS Injection -
https://github.com/ronituohino/cybersecurity-project/blob/main/pages/templates/pages/index.html#L23

A user can send a message which isn't properly handled, and instead interpreted
as code if it is valid html. An attacker could send a message with a script -tag
and a nasty JS program with it. This way the attacker could fish out user
messages, or other sensitive information from alice's computer when she loades
the page.

This flaw can be fixed by removing the "|safe" part from the variable in the
html. This way the message contents are interpreted just as text. It could also
be fixed by implementing some sort of validation in the `addMessage` function in
`views.py`.

In Django it's also quite difficult to naturally introduce an XSS vulnerability,
since the you need to manually tell Django that the input will be "|safe". In
other frameworks, you should pay more attention to this though.

FLAW 3: Broken access control -
https://github.com/ronituohino/cybersecurity-project/blob/main/pages/views.py#L51

The messages route uses the userid that is passed onto it through the GET
request. This makes it possible for other logged in users to go to their
messages page, and change the id in the url to someone else's and view their
messages. This could be easily achieved since the id is just an increasing
number.

To fix this issue, the messages route should get the userid from the request
object, and not from the url.

This is a pretty difficult issue, since frameworks can't enforce secure design.
I guess this explains why this flaw is #1 in the OWASP Top Ten for 2021.
Developers need to learn not to trust user input, wherever it may be.

FLAW 4: Weak password hashing -
https://github.com/ronituohino/cybersecurity-project/blob/main/config/settings.py#L114

Passwords in the database are stored as hashes. However, they have been hashed
using the MD5 algorithm, which is easily reversable. If attackers were to gain
access to the database, they could trivially get valid user credentials by
reversing the hashes.

To fix this issue, one should just remove the explicitly defined hasher in the
settings file. This would make Django default to SHA256 hashing, which is much
more secure.

This issue is not that common, because most sources recommend secure hashing
algorithm nowadays. Also most frameworks use secure hashing algorithms by
default. Storing passwords as hashes could become a problem though now that
quantum computing is being developed. Passwords can be made stronger by using a
salt, which is essentially a unique addon to the hashing key per-user. This
means that if a hacker were to gain access to a database, they couldn't attempt
to break all the passwords in the database at once, since the salt values are
different for each user.

FLAW 5: Possibly sensitive info in git -
https://github.com/ronituohino/cybersecurity-project/blob/main/db.sqlite3

The development database is in Github containing developer credentials. Some of
these could end up in production for superusers, and possibly free access to the
production server for the attackers.

https://github.com/ronituohino/cybersecurity-project/blob/main/db.sqlite3

The SECRET_KEY used in development is in an early git commit, which might be the
same used in production. Leaking this, according to Django, "can lead to
privilege escalation and remote code execution vulnerabilities."

https://github.com/ronituohino/cybersecurity-project/commit/898fba165ad779d2ba5ba9d3445314dea535c4bc

To fix these issues, either the information has to be removed from the git
history, or it has to be made sure none of it is used in production. To remove
this information, the git history has to be deleted, which could be achieved by
creating a new repository.

This issue is quite common, since it's not obvious that attackers could find
these keys in version control (because it doesn't feel like a part of the
application). Also, sometimes it's difficult to configure environment variables,
which increases the risk of lazy developers uploading their .env settings to
version control.
