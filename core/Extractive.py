import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords


class Extractive:
    def __init__(self) -> None:
        pass

    def summarize(self, data) -> str:
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(data)
        frequencyTable = dict()
        for word in words:
            word = word.lower()
            if word in stopWords:
                continue
            if word in frequencyTable:
                frequencyTable[word] += 1
            else:
                frequencyTable[word] = 1

        sentences = sent_tokenize(data)
        sentenceValue = dict()
        for sentence in sentences:
            for word, freq in frequencyTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq
        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]

        avg = sumValues / len(sentenceValue)
        summary = ""
        for sentence in sentences:
            if(sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * avg)):
                summary += " " + sentence
        return summary


if __name__ == "__main__":
    pass
