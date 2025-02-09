texts = input().split()
texts_even_length = [text for text in texts if len(text) % 2 == 0]

print('\n'.join(texts_even_length))