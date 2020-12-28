 math.randomseed(os.time())
 
 for g=1, 1 do

number = math.random(1000,10000)

arxeio= math.random(2993566000,99999925500)
     local file = io.open("proxies/" .. arxeio .. ".txt", "w")
  
for i = 1, number do
    
anon1 = math.random(0,255)
 anon2 = math.random(0,255)
 anon3 = math.random(0,255)
 anon4 = math.random(0,255)
  anonport = math.random(1,50009)
    io.write(anon1 .. "." .. anon2 .. "." .. anon3 .. "." .. anon4 .. ":" .. anonport)
    file:write(anon1 .. "." .. anon2 .. "." .. anon3 .. "." .. anon4 .. ":" .. anonport .. "\n")
      
    i = i + 1
      
    end
     file:close()
end