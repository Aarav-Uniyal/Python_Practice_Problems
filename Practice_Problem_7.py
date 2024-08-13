def matching_words(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score


def searcher():
    sentences = ["python is a good programming language", "this is snake",
                 "Aarav is a good boy", "Play Minecraft now"]

    query = input("Please enter the query string\n")
    scores = [matching_words(query, sentence) for sentence in sentences]
    sorted_sent_score = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True) if sentScore[0] != 0]

    print(f"{len(sorted_sent_score)} results found!")
    index = 0
    for score, item in sorted_sent_score:
        index += 1
        print(f"{index}. \"{item}\": with a match of {score} words.")


if __name__ == "__main__":
    searcher()
