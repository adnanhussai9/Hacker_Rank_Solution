''' https://www.hackerrank.com/challenges/apple-and-orange/problem '''
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    for i in range(len(apples)):
        apples[i]+=a
    for j in range(len(oranges)):
        oranges[j]+=b
    ap=0
    ora=0
    for k in apples:
        if k>=s and k<=t:
            ap+=1
    for l in oranges:
        if l>=s and l<=t:
            ora+=1
    print(ap)
    print(ora)