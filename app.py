import streamlit as st

def main():
    # Add title to the app
    st.title("Favorite Animal App")

    # Add a description or instructions
    st.write("Please tell me your favorite animal below:")

    # Ask the user for their favorite animal
    favorite_animal = st.text_input("What's your favorite animal?")

    # Display message if the user has provided an input
    if favorite_animal:
        st.markdown(f"<h2 style='color: green;'>My favorite animal is also <b>{favorite_animal}</b>!</h2>", unsafe_allow_html=True)

    # Add some extra style with a button
    if st.button("Try Again"):
        st.experimental_rerun()

# This runs the Streamlit app
if __name__ == '__main__':
    main()
