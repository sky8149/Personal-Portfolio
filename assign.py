import streamlit as st

def main():
    st.title("Akash Shinde -M.sc Statistics")

    # Header section
    st.text("I am currently pursuing my master's degree in statistics from RJ college and i have completed my bachelor's degree in statistics from  BN Bandodakar clg")
    st.text("with related to statistics i have done courses in several data analysis and visualization tools like Python, R, and Excel which i have used in my coursework ")
    st.text("and projects. my goal is to work with the organisation where i can apply these skills to drive meaningful impact.")

    # Navigation menu
    navigation_menu = st.sidebar.radio("Navigation", ["Projects", "Education", "Skills", "Contact"])
    
    # Main content based on navigation menu
    if navigation_menu == "Projects":
        display_projects()
    elif navigation_menu == "Education":
        display_education()
    elif navigation_menu == "Skills":
        display_skills()
    elif navigation_menu == "Contact":
        display_contact()

def display_projects():
    st.header("Projects")

    # Display images and descriptions for each project
    # Project 1
    project1_image = "image1.jpg"  # Replace with your actual image path or URL
    project1_description = """In September 2023, I undertook a project focused on predicting Heart Disease and Diabetes.
                            The primary objectives included building a Disease Prediction System and gaining hands-on experience
                            with end-to-end machine learning processes. The project encompassed data pre-processing, feature
                            selection, model building, model selection, and ultimately deploying the model on Streamlit Cloud.
                            Utilizing the SVM classification algorithm, the prediction system achieved an accuracy of 85%.
                            The project was implemented using Python, Jupyter IDE, NumPy, Pandas, and scikit-learn."""

    # Project 2
    project2_image = "image2.jpg"  # Replace with your actual image path or URL
    project2_description = """In August 2023, I conducted a Time Series Analysis project focused on predicting Rossmann 
                            store sales for the next year. The project aimed to uncover meaningful patterns and trends 
                            through exploratory data analysis to inform future predictions. Employing ARIMA, SARIMA, and 
                            Exponential Smoothing methods, I assessed model adequacy using a Normal Q-Q plot and Correlogram. 
                            The final forecasting utilized the SARIMA model, achieving a Root Mean Square Error (RMSE) of 739.061164.
                            Python, with Jupyter notebook, served as the primary tool for this analysis."""

    st.image(project1_image, caption="Project 1 Image", use_column_width=True)
    st.write("Project 1 Description:", project1_description)

    st.image(project2_image, caption="Project 2 Image", use_column_width=True)
    st.write("Project 2 Description:", project2_description)

def display_education():
    st.header("Education")

    # Display educational background
    st.write("""Currently pursuing M.Sc. Statistics at Ramniranjan Jhunjhunwala College, Mumbai, with an expected completion in 2024. 
                Completed B.Sc. Statistics at B.N.Bandodakar College, Thane, from 2019 to 2022, achieving a GPA of 7.54. 
                Completed H.S.C at M.G.V. Dhasai in 2019 with a score of 71.38%. 
                Completed S.S.C at J.V. Dhasai in 2017 with a score of 80.60%.""")

def display_skills():
    st.header("Skills")

    # Display skills and proficiency level
    st.write("R Programming - Intermediate")
    st.write("Python - Intermediate")
    st.write("Advance Excel ")
    st.write("PowerBI")
    st.write("SQL - Intermediate")

def display_contact():
    st.header("Contact")
    st.write("Name: Akash Shinde ")
    st.write("Phone : 8149841507 ")
    st.write("Email : as3840740@gmail.com ")
    st.write("Address : Vangani, Maharashtra  ")
    st.write("Languages Known : Marathi, Hindi, English.  ")
    
    st.markdown(" Thank You !")




    # Simple contact form
    name = st.text_input("Name:")
    email = st.text_input("Email:")
    message = st.text_area("Message:")
    submit_button = st.button("Send Message")

    # Handle form submission
    if submit_button:
        st.success(f"Message sent! \n\nName: {name} \nEmail: {email} \nMessage: {message}")

if __name__ == "__main__":
    main()
