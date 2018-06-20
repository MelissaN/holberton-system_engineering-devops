## Regular Expression
> Each file in this repository holds code that illustrates an essential concept of programming,
> specific to regular expressions. Resources to learn topic:
> [rubular](http://rubular.com/), [regex101.com](https://regex101.com/r/cO8lqs/2),
> [blog](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)

### Environment
* Language: Ruby
* OS: Ubuntu 14.04 LTS
* Usage: Run each file with ```./[filename] "pattern to test if match" | cat -e```
* Each file has the following format:
```
#!/usr/bin/env ruby
puts ARGV[0].scan(/ regex here /).join
```

---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)

