from translator import translate
from train_HMM import train

tests = [
	'EU rejects Egypt call to boycott British lamb',
    'The teacher gave the brilliant student a book.',
    'The boys ran',
    'The teacher gave the student a book',
    'Ahmed came quickly',
    'The small house',
    'They elected him president',
    'Ahmed lives a good life',
]

log = open('log.txt', 'w')

model = train()

for test in tests:
    translate(test, model, log)