"""
DeepML Problem #2: Calculate Unigram Probability from Corpus
Difficulty: Easy
Category: NLP

Problem Description:
Implement a function that calculates the unigram probability of a given word in a corpus 
of sentences. Include start <s> and end </s> tokens in the calculation. The probability 
should be rounded to 4 decimal places.

Example:
Input:
corpus = "<s> Jack I like </s> <s> Jack I do like </s>", word = "Jack"
Output:
0.1818

Reasoning:
The corpus has 11 total tokens. 'Jack' appears twice. So, probability = 2 / 11

Test Cases:
1. corpus = "<s> the quick brown fox </s> <s> jumps over the lazy dog </s>", word = "the" -> 0.1538
2. corpus = "<s> I am Jack </s> <s> Jack I am </s> <s> Jack I like </s> <s> Jack I do like </s> <s> do I like Jack </s>", word = "like" -> 0.1111
3. corpus = "<s> hello world </s> <s> hello </s>", word = "hello" -> 0.2857
4. corpus = "<s> the quick brown fox </s> <s> jumps over the lazy dog </s>", word = "the" -> 0.1538
"""

def unigram_probability(corpus: str, word: str) -> float:
    """
    Calculate the unigram probability of a given word in a corpus.
    
    Args:
        corpus (str): The input corpus containing sentences with <s> and </s> tokens
        word (str): The word to calculate probability for
        
    Returns:
        float: The probability of the word rounded to 4 decimal places
    """
    number_of_occurrences = len(corpus.split(word)) - 1
    number_of_words = len(corpus.split(" "))

    if number_of_words == 0:
        return 0
    else:
        probability = number_of_occurrences/number_of_words
        return round(probability, 4)


# Test the function with provided test cases
if __name__ == "__main__":
    # Test case 1
    corpus1 = """<s> the quick brown fox </s> <s> jumps over the lazy dog </s>"""
    result1 = unigram_probability(corpus1, "the")
    print(f"Test 1 - Expected: 0.1538, Got: {result1}")
    
    # Test case 2
    corpus2 = """<s> I am Jack </s> <s> Jack I am </s> <s> Jack I like </s> <s> Jack I do like </s> <s> do I like Jack </s>"""
    result2 = unigram_probability(corpus2, "like")
    print(f"Test 2 - Expected: 0.1111, Got: {result2}")
    
    # Test case 3
    corpus3 = """<s> hello world </s> <s> hello </s>"""
    result3 = unigram_probability(corpus3, "hello")
    print(f"Test 3 - Expected: 0.2857, Got: {result3}")
    
    # Test case 4 (duplicate of test 1)
    corpus4 = """<s> the quick brown fox </s> <s> jumps over the lazy dog </s>"""
    result4 = unigram_probability(corpus4, "the")
    print(f"Test 4 - Expected: 0.1538, Got: {result4}")
    
    # Example from problem description
    corpus_example = "<s> Jack I like </s> <s> Jack I do like </s>"
    result_example = unigram_probability(corpus_example, "Jack")
    print(f"Example - Expected: 0.1818, Got: {result_example}")
