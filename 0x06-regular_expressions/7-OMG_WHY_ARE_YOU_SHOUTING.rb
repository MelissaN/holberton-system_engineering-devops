#!/usr/bin/env ruby
# Only match capital letters

puts ARGV[0].scan(/[A-Z]/).join
