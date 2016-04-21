from urllib.request import urlopen
with urlopen('http://www.imdb.com/movies-in-theaters/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2446567422&pf_rd_r=1KTGHG28EYZXV39Y5835&pf_rd_s=right-3&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_otw_hd') as story:
    story_words=[]
    for line in story:
        line_words = line.split()
        for word in line_words:
            story_words.append(word)
            
print(story_words)
