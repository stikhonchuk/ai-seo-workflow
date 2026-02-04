"""
Keyword Extractor for [YOUR-DOMAIN]
Extracts top keywords from text using simple frequency analysis.
"""

import re
from typing import List, Dict, Tuple
from collections import Counter


# Russian stop words - common words to exclude from keyword analysis
RUSSIAN_STOP_WORDS = {
    # Pronouns
    'я', 'мы', 'ты', 'вы', 'он', 'она', 'оно', 'они',
    'мне', 'мной', 'меня', 'нам', 'нас', 'нами',
    'тебе', 'тебя', 'тобой', 'вам', 'вас', 'вами',
    'его', 'ему', 'им', 'её', 'ей', 'ею', 'их', 'ими',
    'себя', 'себе', 'собой', 'свой', 'своя', 'своё', 'свои',
    'этот', 'эта', 'это', 'эти', 'тот', 'та', 'то', 'те',
    'какой', 'какая', 'какое', 'какие', 'который', 'которая', 'которое', 'которые',
    'чей', 'чья', 'чьё', 'чьи', 'кто', 'что', 'весь', 'вся', 'всё', 'все',
    'сам', 'сама', 'само', 'сами', 'самый', 'самая', 'самое', 'самые',

    # Prepositions
    'в', 'во', 'на', 'за', 'из', 'к', 'ко', 'от', 'до', 'по', 'под', 'над',
    'при', 'про', 'без', 'для', 'через', 'между', 'о', 'об', 'обо', 'у', 'с', 'со',

    # Conjunctions
    'и', 'а', 'но', 'да', 'или', 'либо', 'ни', 'если', 'когда', 'чтобы',
    'хотя', 'пока', 'как', 'так', 'потому', 'поэтому', 'также', 'тоже',

    # Particles
    'не', 'ни', 'бы', 'же', 'ли', 'ведь', 'вот', 'вон', 'даже', 'лишь',
    'только', 'уже', 'ещё', 'еще', 'разве', 'неужели',

    # Auxiliary verbs
    'быть', 'есть', 'был', 'была', 'было', 'были', 'будет', 'будут', 'буду',
    'будем', 'будешь', 'будете', 'являться', 'является', 'являются',
    'стать', 'стал', 'стала', 'стало', 'стали', 'станет', 'станут',
    'мочь', 'может', 'могут', 'можно', 'нужно', 'надо', 'нельзя',

    # Common adverbs
    'очень', 'более', 'менее', 'много', 'мало', 'где', 'куда', 'откуда',
    'когда', 'тогда', 'почему', 'зачем', 'как', 'так', 'там', 'тут', 'здесь',
    'сюда', 'туда', 'всегда', 'никогда', 'иногда', 'часто', 'редко',
    'сейчас', 'теперь', 'потом', 'раньше', 'позже', 'сразу', 'давно',

    # Numbers (words)
    'один', 'одна', 'одно', 'одни', 'два', 'две', 'три', 'четыре', 'пять',
    'шесть', 'семь', 'восемь', 'девять', 'десять', 'первый', 'второй', 'третий',

    # Other common words
    'год', 'года', 'году', 'лет', 'день', 'дня', 'дней', 'раз', 'время',
    'человек', 'люди', 'людей', 'другой', 'другая', 'другое', 'другие',
    'новый', 'новая', 'новое', 'новые', 'большой', 'большая', 'большое', 'большие',
    'маленький', 'маленькая', 'маленькое', 'маленькие', 'хороший', 'хорошая', 'хорошее',
    'каждый', 'каждая', 'каждое', 'каждые', 'любой', 'любая', 'любое', 'любые',

    # E-commerce common words (less relevant for SEO)
    'купить', 'цена', 'доставка', 'заказ', 'заказать', 'корзина', 'каталог',
    'магазин', 'интернет', 'онлайн', 'руб', 'рублей', 'рубль',
}

# Common English stop words that might appear
ENGLISH_STOP_WORDS = {
    'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
    'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'be',
    'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
    'would', 'could', 'should', 'may', 'might', 'must', 'shall',
    'this', 'that', 'these', 'those', 'it', 'its', 'they', 'them',
}

ALL_STOP_WORDS = RUSSIAN_STOP_WORDS | ENGLISH_STOP_WORDS


class KeywordExtractor:
    """Extracts top keywords from text using frequency analysis."""

    def __init__(self, stop_words: set = None, min_word_length: int = 3):
        self.stop_words = stop_words or ALL_STOP_WORDS
        self.min_word_length = min_word_length

    def extract(self, text: str, top_n: int = 10) -> List[str]:
        """Extract top N keywords from text."""
        if not text:
            return []

        # Tokenize and clean
        words = self._tokenize(text)

        # Filter stop words and short words
        filtered_words = [
            word for word in words
            if word not in self.stop_words and len(word) >= self.min_word_length
        ]

        # Count frequencies
        word_counts = Counter(filtered_words)

        # Return top N
        top_keywords = [word for word, count in word_counts.most_common(top_n)]
        return top_keywords

    def extract_with_counts(self, text: str, top_n: int = 10) -> List[Tuple[str, int]]:
        """Extract top N keywords with their counts."""
        if not text:
            return []

        words = self._tokenize(text)
        filtered_words = [
            word for word in words
            if word not in self.stop_words and len(word) >= self.min_word_length
        ]

        word_counts = Counter(filtered_words)
        return word_counts.most_common(top_n)

    def _tokenize(self, text: str) -> List[str]:
        """Tokenize text into lowercase words."""
        # Convert to lowercase
        text = text.lower()

        # Extract words (including Cyrillic characters)
        # Match sequences of letters (Latin or Cyrillic)
        words = re.findall(r'[a-zа-яёA-ZА-ЯЁ]+', text, re.UNICODE)

        return words

    def get_word_frequency(self, text: str) -> Dict[str, int]:
        """Get full word frequency dictionary."""
        words = self._tokenize(text)
        filtered_words = [
            word for word in words
            if word not in self.stop_words and len(word) >= self.min_word_length
        ]
        return dict(Counter(filtered_words))


if __name__ == "__main__":
    # Quick test
    extractor = KeywordExtractor()

    test_text = """
    Лоферы — это классическая обувь без шнуровки, которая стала неотъемлемой
    частью гардероба современного человека. Мужские лоферы отлично подходят
    как для делового стиля, так и для повседневной носки. Женские лоферы
    предлагают элегантность и комфорт. Итальянские лоферы Premiata известны
    своим качеством и стилем. Кожаные лоферы — это инвестиция в долговечную обувь.
    """

    keywords = extractor.extract(test_text, top_n=10)
    print("Top 10 keywords:")
    for i, kw in enumerate(keywords, 1):
        print(f"  {i}. {kw}")

    print("\nWith counts:")
    keywords_with_counts = extractor.extract_with_counts(test_text, top_n=10)
    for word, count in keywords_with_counts:
        print(f"  {word}: {count}")
