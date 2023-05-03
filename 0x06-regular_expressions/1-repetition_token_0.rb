#!/usr/bin/env ruby

matches = ARGV[0].scan(/hbtt+n/)
for i in matches do
  print i
end
puts ''
