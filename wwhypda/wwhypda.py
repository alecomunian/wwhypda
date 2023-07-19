#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:This file:

    `template.py`

:Purpose:

    Purpose of the script/module

:Usage:

    Explain here how to use it.

:Parameters:

:Version:

    Wed Jul 19 21:25:37 2023

:Authors:

    Alessandro Comunian

.. notes::

.. warning::

.. limitations::
"""


import sqlite3
import pandas as pd


if __name__ == '__main__':
    # Create a connection
    con = sqlite3.connect("../SQLite/wwhypda.db")
    # Create a cursor
    cur = con.cursor()
    
    # Print all the tables
    for row in cur.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND "
                "name NOT LIKE 'sqlite_%';"):
        print(row)
        
    # Show the info about  of one table
    for row in cur.execute("PRAGMA table_info(Rock_type);"):
        print(row)
        
    for row in cur.execute("SELECT rt_name FROM Rock_type;"):
        print(row)

    print("\n********* Cerco Sand *************")
    searchstr = "Sand"
    for row in cur.execute("SELECT rt_name FROM Rock_type WHERE rt_name like ?",('%'+searchstr+'%',)):
        print(row[0])
        
    # Return the output of a query as a pandas DataFrame
    queryres = cur.execute("SELECT rt_name FROM Rock_type WHERE rt_name like ?",('%'+searchstr+'%',))
    df = pd.DataFrame(queryres.fetchall())
    # df.columns = queryres.description
    
    

    