import streamlit as st
from spellchecker import SpellChecker


class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def check_spelling(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                st.write(f'Correcting {word} to {corrected_word}')
            corrected_words.append(corrected_word)  # Always append corrected word
        return ' '.join(corrected_words)

# Instantiate the app
spell_checker = SpellCheckerApp()

# Streamlit UI
st.title('Spell Checker')

text = st.text_area("Enter Text:", value='', height=100)

if st.button('Correct Spelling'):
    if text.strip() == '':
        st.warning('Please enter text for checking.') 
    else: 
        corrected_text = spell_checker.check_spelling(text)
        st.markdown('### ✅ Corrected Text:')
        st.text_area("Corrected Text", value=corrected_text+'.', height=100)
