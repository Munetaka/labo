import pickle


with open('sample.pickle', 'wb') as f:
    pickle.dump('Hello, World!', f)
