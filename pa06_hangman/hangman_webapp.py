"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

#global state
state = {'guesses':[],
		 'word':"interesting",
		 'word_so_far':"-----------",
		 'done':False,
		 'letters_in_word': [],
		 'guess_all': [],
		 'blank':'',
		 'message':'',
		 'guesses_left':6
		 } #this defines the variables

@app.route('/')
@app.route('/main')
def main():
	return render_template('hangman.html')

@app.route('/start')
def play():
	global state
	state['word']=hangman_app.generate_random_word() #calls a function in hangman_app.py
	state['blank']=list(len(state['word'])*'_')
	state['guesses'] = []
	return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST']) #GET means typed in address, post is clicked a button
def hangman():
	""" plays hangman game """
	global state
	if request.method == 'GET':
		return play()

	elif request.method == 'POST':
		letter = request.form['guess']
		if letter in state['guesses']:
			state['guesses_left'] = state['guesses_left'] - 1
			state['message'] = ("You already guessed "+letter)
		elif letter not in state['word']:
			state['guesses_left'] = state['guesses_left'] - 1
			state['guesses'].append(letter)
			state['message']=letter+' is not in the word.'
		else:
			state['guesses'].append(letter)
			state['message'] = letter+' is in the word!'
		state['word_so_far'] = hangman_app.print_word(state['word'], letter, state['blank'])

		def letters_in_word():
			letters_in_word = []
			for i in range(0,len(state['word'])):
				letters_in_word.append(state['word'][i])
			return letters_in_word

		state['letters_in_word'] = letters_in_word()

		state['guess_all'] = []

		for i in range(0,len(state['word'])):
			if state['word'][i] in state['guesses']:
				state['guess_all'].append(state['word'][i])

		#if all the letters in the word have been guessed, then you win
		#else if there are no more guesses left then you lose
		#the else statement lets you guess another letter if you haven't won yet and you still have guesses remaining
		if state['guess_all'] == state['letters_in_word']:
			state['word_so_far'] = state['word']
			state['message'] = 'You win!'
			#done=True
		elif state['guesses_left'] == 0:
			state['message'] = 'You lose :('
			state['word_so_far'] = 'the answer was: ' + state['word']
			#done=True
		# check if letter has already been guessed
		# and generate a response to guess again
		# else check if letter is in word
		# then see if the word is complete
		# if letter not in word, then tell them
		return render_template('play.html',state=state)

@app.route('/miranda')
def miranda():
	""" generates a bio page with links and images """
	return render_template('miranda.html')

@app.route('/sonia')
def sonia():
	""" generates a bio page with links and images """
	return render_template('sonia.html')

@app.route('/charisma')
def charisma():
	""" generates a bio page with links and images """
	return render_template('charisma.html')

@app.route('/about')
def about():
    """generates an about page with information about the game"""
    return render_template('about.html')

if __name__ == '__main__':
	app.run(port=3000)
