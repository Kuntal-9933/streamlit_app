# Import necessary libraries
import streamlit as st

# Define the main function for the app
def main():
    # Set the title of the app
    st.title("My Streamlit App")

    # Add a sidebar with options
    options = ["Home", "About", "Contact"]
    choice = st.sidebar.selectbox("Select Option", options)

    # Display different content based on the selected option
    if choice == "Home":
        st.write("Welcome to the Home Page!")
        # Add more content as needed
    elif choice == "About":
        st.write("This is the About Page.")
        # Add more content as needed
    elif choice == "Contact":
        st.write("Contact us at example@email.com.")
        # Add more content as needed

# Run the app
if __name__ == "__main__":
    main()
