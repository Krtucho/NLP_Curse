from sklearn.datasets import fetch_20newsgroups
newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

# Example transformation of Top2Vec output to gensim-compatible format
# This is a conceptual step; actual implementation depends on Top2Vec's output structure

def transform_top2vec_output_for_coherence(top2vec_output):
    # Convert Top2Vec output to gensim-compatible format
    # This is highly dependent on the structure of Top2Vec's output
    pass

# Assuming `transformed_topics` is the result of the above function
coherence_scores = []
for transformed_topic in transformed_topics:
    coherence_score = gensim.models.CoherenceModel(model=transformed_topic, texts=newsgroups.data, dictionary=dictionary).get_coherence()
    coherence_scores.append(coherence_score)
average_coherence = sum(coherence_scores) / len(coherence_scores)


def calculate_topic_diversity(top_words_per_topic):
    unique_top_words_count = len(set(word for topic in top_words_per_topic for word in topic))
    total_top_words_count = sum(len(topic) for topic in top_words_per_topic)
    return unique_top_words_count / total_top_words_count

# Example usage
# Assuming `top_words_per_topic` is a list of lists where each sublist contains the top words for a topic
diversity_score = calculate_topic_diversity(top_words_per_topic)
print(f"Topic Diversity Score: {diversity_score}")
