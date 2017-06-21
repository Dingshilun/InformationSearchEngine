stopset = ["is", "a", "he", "she", "and", "are", "am", "of", "for", "were", "in", "it", "them", "its", "would", "share",
           "The", "an", "him", "her", "what", "be", "now", "good", "I'm", "No", "not", "It", "TO", "about", "also",
           "as", "at", "been", "but", "by", "from", "had", "has", "have", "last", "on", "one", "or", "said", "that",
           "the", "this", "to", "up", "vs", "was", "which", "will", "with", "I"]
deleteset= ['\n', '\r', '>', '<', ')', '(', '\"', "\'", '&lt', '-', '+', '@', '%', '^', '*', ':', ';', '&amp']


def wordProcess(aString):
    words = aString.replace('.','')
    words = words.replace(',','')
    words = words.replace('\n','')
    words = words.lower()
    word = words.split(' ')
    return word
