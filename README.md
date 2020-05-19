# RE
### Regular Expression in Python

#### Performing matches with compiled objects

* match(): Determine if the RE matches at the beginning of the string.
* search(): Scan through a string, looking for any location where this RE matches.
* findall(): Find all substrings where the RE matches, and returns them as a list.
* finditer(): Find all substrings where the RE matches, and returns them as an iterator.

#### Modification methods

* split(): Returns a list where the string has been split at each match.
* sub(): Replaces one or many matches with a string.

#### Methods on a Match object
* group(): Return the string matched by the RE.
* start(): Return the starting position of the match.
* end(): Return the ending position of the match.
* span(): Return a tuple containing the (start, end) positions of the match.
