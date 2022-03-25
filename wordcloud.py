import wordcloud
from matplotlib import pyplot as plt

def calculate_frequencies(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just", "in"]

    file_contents = file_contents.lower()
    file_contents = ' ' + file_contents + ' '
    file_contents = file_contents.replace('\r\n',' \r\n ')
    for letter in punctuations:
        file_contents = file_contents.replace(letter, '')
    for word in uninteresting_words:
        w = ' ' + word + ' '
        file_contents = file_contents.replace(w, ' ')

    result = {}
    for word in file_contents.split():
        if word not in result:
            result[word] = 0
        result[word] += 1
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(result)
    return cloud.to_array()


file_contents = open('doc.txt', 'r')
file_contents = file_contents.read()
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()