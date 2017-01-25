Given an array containing hashes of names
Return a string formatted as a list of names separated by commas except for
the last two names, which should be separated by an ampersand.

Input : [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
Output: 'Bart, Lisa & Maggie'

Input : [{'name': 'Bart'}, {'name': 'Lisa'}]
Output: 'Bart & Lisa'

Input : [{'name': 'Bart'}]
Output: 'Bart'

Input : []
Output: ''
