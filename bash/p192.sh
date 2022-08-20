# Read from the file words.txt and output the word frequency list to stdout.
tr ' ' '\n' < words.txt  | egrep -v '^$' | sort | uniq -c | sort -rn | awk '{print $2 " " $1}'