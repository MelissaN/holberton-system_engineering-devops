#!/usr/bin/env ruby
# Match "hbtn, htn" not "hbbtn"

puts ARGV[0].scan(/hb?tn/).join
