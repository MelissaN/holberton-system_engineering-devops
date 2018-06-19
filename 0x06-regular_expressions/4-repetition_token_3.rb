#!/usr/bin/env ruby
# Match "hbn, hbtn, hbtttttn" not "hbon"

puts ARGV[0].scan(/hbt*n/).join
