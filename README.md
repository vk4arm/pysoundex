pysoundex
=========

Python library for
Multilanguage configurable soundex (with English and Russian)



## Installation


From source:

    $ sudo python setup.py install


## Usage

    >>> import pysoundex
    >>> print pysoundex.soundex("Приветище", lang='ru_RU')
    п613
    >>> print pysoundex.soundex("Hello")
    h400   <--- the same as un mysql!
    >>> print pysoundex.soundex("Halo")
    h400
    
## Languages configuration:

   In lang_soundconfig.py: add dictionary element, similar with "en_US" or "ru_RU":
   
   "en_US": {
  	"vowels": [ 'a', 'e', 'h', 'i', 'o', 'u', 'w', 'y' ],
		"consonants": {
			1: [ 'b', 'f', 'p', 'v'], 
			2: [ 'c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],  
			3: ['d', 't'] ,
			4: ['l'] ,
			5: ['m', 'n'], 
			6: ['r'] 
		}
	  },
   