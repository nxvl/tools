#!/usr/bin/python
""" Takes the output of mysql 'select * from `information_schema`.`tables`' and
build a tree that describes the databases and tables

Usage:
* On you server:
 - echo 'select * from `information_schema`.`tables`' > db_schema.sql
 - mysql --password < db_schema.sql > db_schema.txt
 - python build_db_tree.py

Nicolas Valcarcel <nvalcarcel@gmail.com>
"""


def parse_file(filename):
    """Parses the file containing the db schema

    Key Arguments:
    filename - the file to parse"""
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    db = {}
    for line in lines:
        s_line = line.split('\t')
        if s_line[0] == 'TABLE_CATALOG':
            continue
        if s_line[1] in db:
            db[s_line[1]].append(s_line[2])
        else:
            db[s_line[1]] = [s_line[2]]
    return db


def print_tree(db_dict):
    """Prints the db tree

    Key arguments:
    db_dict - the doctionary build by parse_file to print"""
    for db in db_dict.keys():
        print "\n%s" % db
        print "%s\n" % ("=" * len(db))
        for table in db_dict[db]:
            print " * %s" % table


if __name__ == '__main__':
    import os
    import sys
    filename = "%s/db_schema.txt" % \
        os.path.abspath(os.path.dirname(sys.argv[0]))
    db = parse_file(filename)
    print_tree(db)
