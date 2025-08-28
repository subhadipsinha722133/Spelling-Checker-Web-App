import streamlit as st
from spellchecker import SpellChecker

# Step 1: Set up the page
st.set_page_config(
    page_title="Spell Checker App",
    page_icon="📝",
    layout="centered"
)


# Step 2: Create the app class
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()
    
    def correct_text(self, text):
        words = text.split()
        corrected_words = []
        corrections = []
        
        for word in words:
            # Clean the word (remove punctuation, etc.)
            cleaned_word = ''.join(char for char in word if char.isalnum())
            
            if cleaned_word:  # Only process if word is not empty after cleaning
                corrected_word = self.spell.correction(word)
                
                # Handle None values from spell checker
                if corrected_word is None:
                    corrected_word = word  # Keep original if no correction found
                
                if corrected_word != word.lower():
                    corrections.append(f'Correcting "{word}" to "{corrected_word}"')
                    corrected_words.append(corrected_word)
                else:
                    corrected_words.append(word)
            else:
                # Keep non-alphanumeric characters as they are
                corrected_words.append(word)
        
        return ' '.join(corrected_words), corrections

# Step 3: Initialize the app
spell_checker = SpellCheckerApp()

# Step 4: Create the Streamlit UI
st.title("📝 Spell Checker App")
st.write("Made by Subhadip Sinha 😎 ")
st.markdown("---")

# Input text area
text_input = st.text_area(
    "Enter text to check:",
    placeholder="Type your text here...",
    height=150
)

# Check button
if st.button("Check Spelling", type="primary"):
    if text_input.strip():
        # Perform spell checking
        corrected_text, corrections = spell_checker.correct_text(text_input)
        
        # Display original text
        st.subheader("Original Text:")
        st.write(text_input)
        
        # Display corrections if any
        if corrections:
            st.subheader("Corrections Made:")
            for correction in corrections:
                st.info(correction)
        else:
            st.success("No spelling errors found! 🎉")
        
        # Display corrected text
        st.subheader("Corrected Text:")
        st.success(corrected_text)
        
        # Show some stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Original Words", len(text_input.split()))
        with col2:
            st.metric("Corrections", len(corrections))
        with col3:
            st.metric("Corrected Words", len(corrected_text.split()))
        
    else:
        st.warning("Please enter some text to check.")

# Sidebar information
with st.sidebar:
    st.header("About")
    st.info("""
    This Spell Checker app uses the `spellchecker` Python library 
    to identify and correct spelling errors in your text.
    
    **Features:**
    - Real-time spell checking
    - Shows individual corrections
    - Displays statistics
    - Clean and user-friendly interface
    """)
    
    st.markdown("---")
    st.caption("Type your text and click 'Check Spelling' to see corrections.")

# Footer
st.markdown("---")
st.caption("🔧 Built with Streamlit & SpellChecker library")