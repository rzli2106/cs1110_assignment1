"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: Joon Lee (jl4875) and Richard Li (rl998)
Date: September 12, 2026
"""

import introcs


def before_space(s):
    """
    Returns a copy of s up to (but not including) the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    space = s.index(' ')
    return s[:space]


def after_space(s):
    """
    Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    space = s.index(' ')
    return s[space+1:]


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that
    delimits it. We typically use single quotes (') to delimit a
    string if want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C',
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes
    """
    first_quote = s.index('"')
    substring = s[first_quote+1:]
    second_quote = substring.index('"')
    return substring[:second_quote]


def get_old(json):
    """
    Returns the original value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "old". For example, if the JSON is

    '{ "err":"", "old":"1 Bitcoin", "new":"69190.992850277 Euros",
    "valid":true }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    start = json.index('"old":')
    old = json[start+6:]
    return first_inside_quotes(old)


def get_new(json):
    """
    Returns the converted value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "new". For example, if the JSON is

    '{ "err":"", "old":"1 Bitcoin", "new":"69190.992850277 Euros",
    "valid":true }'

    then this function returns '69190.992850277 Euros' (not
    '"69190.992850277 Euros"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    start = json.index('"new":')
    new = json[start+6:]
    return first_inside_quotes(new)


def has_error(json):
    """
    Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the
    opposite of the value following the keyword "valid". For example,
    if the JSON is

    '{ "err":"Currency amount is invalid.", "old":"", "new":"",
    "valid":false }'

    then the query is not valid, so this function returns True (It
    does NOT return the message 'Source currency code is invalid').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    return json.find('"valid":false') >= 0

def query_website(src, dst, amt):
    """Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the 
    currency dst. The response should be a string of the form    

    '{ "err":"", "old":"<old-amt>", "new":"<new-amt>", "valid":true }'

    where the values old-amount and new-amount contain the value 
    and name for the original and new currencies. If the query is 
    invalid, both old-amount and new-amount will be empty, while 
    "valid" will be followed by the value false (and "err" will have 
    an error message).

    Parameter src: the currency on hand
    Precondition: src is a string with no spaces or non-letters
        
    Parameter dst: the currency to convert to
    Precondition: dst is a string with no spaces or non-letters
        
    Parameter amt: amount of currency to convert
    Precondition: amt is a float""" 
    url = "http://cs1110.cs.cornell.edu/2026fa/a1?src=" + src + "&dst=" + dst + "&amt=" + str(amt)
    return introcs.urlread(url)
