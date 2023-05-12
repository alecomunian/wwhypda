# README #

This is the `README.md` file of the wwhypda reposotory. It contains the MySQL and the SQLite version of the project database.

Please note that other versions of the database and tools related to
the wwhypda project exists. For more information, please visit
[https://wwhypda.bitbucket.io/](https://wwhypda.bitbucket.io/).
The content of this repository is replicated in both [bitbucket](https://bitbucket.org/wwhypda/wwhypda) and [github](https://github.com/alecomunian/wwhypda).

Many details and the Manifesto of the wwhypda project can be found
in the pubblication by A.Comunian and P.Renard (2009) *Introducing
wwhypda: a world-wide collaborative hydrogeological parameters
database*, Hydrogeology Journal 17(2) DOI:
[10.1007/s10040-008-0387-x](http://dx.doi.org/10.1007/s10040-008-0387-x), that can be downloaded as [PDF here](http://rdcu.be/yGrx).

## What is this repository for? ##

### MySQL version of the database ###

This repository contains the SQL dump (file `MySQL/wwhypda.sql`) of the orinal version of the
database built within the wwhypda project. For more information about
the project, please visit
[https://wwhypda.bitbucket.io/](https://wwhypda.bitbucket.io/).

### SQLite version of the database ###

This repository also contains the SQLite version (file `/SQLite/wwhypda.db`)
obtained from the SQL dump of the original MySQL database built within
the wwhypda project (file `/MySQL/wwhypda.sql`).
The SQLite version provided here was obtained with the conversion
script [mysql2sqlite](https://github.com/dumblob/mysql2sqlite).


## How do I get set up? ##

### MySQL version ###
You need a running MySQL server to import the SQL dump of the provided
wwhypda database.

Alternatively, you can convert the MySQL dump into another SQL
flavour, like we did for example with the script
[mysql2sqlite](https://github.com/dumblob/mysql2sqlite). You can find
the SQLite version of the database in the folder `SQLite`, file
`wwhypda.db`.

### SQLite version ###
The advantage of SQLite over MySQL (or others) is that you do not need a running SQL server to query your database.
Therefore, if you want to consult it, you can use diverse tools like for example
 some scripting languages like Python with the [sql3 module](https://docs.python.org/3/library/sqlite3.html).


## Contribution guidelines ##

If you think you have a consistent bunch of data that could be entered
into wwhypda, or you have some idea to contribute to the project,
please let us know!

## Who do I talk to? ##

The database was conceived by
[A.Comunian](https//sites.unimi.it/alecomunian) and
[P.Renard](https://www.unine.ch/philippe.renard/home/the-team/philippe-renard.html). Please
contact one of them for more information.
