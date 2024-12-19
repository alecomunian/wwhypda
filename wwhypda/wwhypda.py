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

import anytree as at 



class Rt(object):
    pass

class Rock_type(Rt, at.NodeMixin):  # Add Node feature
    def __init__(self, name, id=0, parent=None, parent_id=None, children=None):
        super(Rock_type, self).__init__()
        self.name = name
        self.id = id
        self.parent = parent
        self.parent_id = parent_id
        if children:
            self.children = children
        
        




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
    # print(queryres.fetchall())

    queryres = cur.execute("SELECT rt_name, rt_id, rt_id_parent FROM Rock_type ORDER BY rt_id_parent")
    df_rt = pd.DataFrame(queryres.fetchall())
    df_rt.columns = [h[0] for h in queryres.description]
    
    # #
    # # Initialize all the rock types
    # #
    Rock_types_tree  = Rock_type(name) 
    for index, row in df_rt.iterrows():
        # print(row)
        # Look for the parent, if available
        parent = df_rt[df_rt["rt_id"]==row["rt_id_parent"]]
        # print(parent)
        Rock_types.append(Rock_type(name=row["rt_name"], id=row["rt_id"],
                                    parent_id=row["rt_id_parent"]))
        
        # for rt in Rock_types:        

    
    

    