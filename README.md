

## Code description

* median_unique.py
  + Use library"bisect" to maintain a list in sorted order without having to call sort each time an item is added to the list.
  + library required: argparse, bisect

* words_tweeted.py
  + In order to decrease the running time, I break the input tweets file into chunks and save them separately into one list. 
    Then use map() built-in function to process the sub-lists parallelly in different cores.
  + set each chunck size = 1 GB
  + library required: argparse, re, collections, functools
   
