v = c(1, 3, 5, 7, 3, 3, 1, 3, 3)
k = 3
v = sort(v)
print(length(v))
print(sum(v))

while (k > 0){
  z = which.max(v)
  v = v[-z]
  z = which.min(v)
  v = v[-z]
  k = k - 1
}

print(length(v))
print(sum(v))

z = sum(v) / length(v)

print(v)


v = c(1, 4, 3, 5)
v = sort(v)
len = length(v)

if (len %% 2 == 0){
  print("dzia³aj")
  med = ((v[len/2] + v[len/2 + 1])/2)
}

if (len %% 2 == 1){
  med = (v[(len/2) + 1])
}
print(med)




v = c(1, 4, 3, 5, 10)

rozstep =abs((v[which.max(v)] - v[which.min(v)]))
print(rozstep)



v = c(1, 2, 3, 4, 5)

sr = mean(v)
print(sr)


len = length(v)
x = 0

for (i in 1:len){
  x = x + (v[i] - sr)**2
}
wariancja = x / (len - 1)

print(wariancja)
print(var(v))

ods = sqrt(wariancja)
print(ods)
print(sd(v))


v = c(1, 4, 5, 5, 10, 1)
sr = mean(v)
ln = length(v)
sm = 0

for(i in 1:len){
  sm = sm + abs(v[i] - sr)
}
odp = sm / ln
print(odp)


v = c(1, 2, 3, 3, 5)
v = sort(v)

m1 = median(v)
x = which(v<=m1)
Q1 = median(x)

x = which(v>=m1)
Q3 = median(x)
print(Q1)
print(Q3)

print(fivenum(v))


cnt = 0
for (i in 0:1000000){
  A1 = runif(1, 0, 1)
  A2 = runif(1, 0, 1)
  A3 = runif(1, 0, 1)
  
  if (A1 <= A2 && A2 <= A3){
    cnt = cnt + 1
  }
}

print(cnt/1000000)


