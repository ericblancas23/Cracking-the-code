def palinPerm(string):
  array = string.split(//)
  hash = Hash.new(0)

  array.each do |char|
    has.include? char ? hash[char]+=1 : hash[char = 1]
  end

  odd = 0
  hash.each_value do |v|
    odd += 1 if v % 2 != 0
  end 
  odd > 1 ? false : true
end 

p palinPerm("never odd or even")