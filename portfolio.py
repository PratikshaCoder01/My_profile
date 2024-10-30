import streamlit as st

# Setting the page layout
st.set_page_config(page_title="My Portfolio", layout="wide")

# Header Section
st.title("👨‍💻 Pratiksha Patil Portfolio")


# Navigation bar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Contact"])

# Home Section
if page == "Home":
    st.header("About Me")
    st.image("My photo.png", caption="My Photo")
    st.write("""

    Hi, I’m Pratiksha Patil, a passionate and results-driven software engineer with 1 year of experience in designing, 
    developing, and maintaining scalable software solutions. I specialize in full-stack development and have a deep 
    understanding of both frontend and backend systems.

    Throughout my career, I’ve had the opportunity to work on a wide range of projects, from building robust enterprise 
    applications to creating innovative tools that streamline complex workflows. I thrive in collaborative environments 
    where I can contribute to solving challenging problems through clean, efficient code, and am always keen on learning 
    and applying the latest technologies and best practices.

    When I’m not coding, you can find me listening music and watching web series, reading novels, cooking and travelling etc.

    """)


    #st.write("""
    #I'm a passionate [Your Profession] with experience in [your expertise areas].
    # My work is driven by creativity and innovation.
    #""")



# Projects Section
elif page == "Projects":
    st.header(" 🏭 Projects")
    st.write("Here are some of my projects:")

    project_data = [
        {"name": " 🍿 Cinemate-MovieMood App", "description": """
        The Movie Recommendation App is a web application built with React that provides personalized movie suggestions based on user preferences. By leveraging third-party APIs (such as The Movie Database - TMDb), the app delivers dynamic and real-time movie recommendations, allowing users to explore trending films, search for specific titles, and receive tailored suggestions based on genres, ratings, and other criteria.

Features

Personalized Recommendations: Users can input their favorite genres, actors, or keywords, and the app will provide movie suggestions based on their preferences.
Search Functionality: A powerful search feature that lets users search for movies by title, genre, or actor.
Trending Movies: A section that displays popular and trending movies, updated in real-time via API calls.
Movie Details: View detailed information about any movie, including synopsis, release date, ratings, cast, and trailers.
Favorites List: Users can create a personal list of favorite movies for future reference.
Responsive Design: The app is optimized for all screen sizes, providing a seamless experience on both desktop and mobile devices.
Tech Stack

Frontend: React.js (with hooks and context for state management)
API Integration: Integrated with TMDb API for fetching real-time movie data and recommendations
UI/UX: Styled with CSS modules and responsive design for a smooth user experience across devices
Routing: React Router for seamless navigation between different sections of the app
State Management: React Context API for managing user preferences and app state globally
Future Enhancements

User Accounts: Enabling user authentication to save preferences and create custom watchlists.
Collaborative Filtering: Incorporating machine learning algorithms for better recommendation accuracy based on user interaction history.
Social Features: Allowing users to share movie recommendations with friends or leave reviews.
    
            
            
            
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         """
         
         ,"link": "https://cinemate-moviemood.netlify.app"},

        {"name": "📚 Ebook store ",
         "description":
         """
         This website deals with book purchasing contains followings features:
         1. User Authentication
         2. Product Catalogue
         3. Cart and checkout
         4. Book review and rating
         5. Customer support and help
         """,
         "link": "https://codebook-bookhaven.netlify.app/"},

        {"name": "🎯 Taskmate-quickcheck",
         "description":
         """
         
         The To-Do App is a task management application that allows users to track their tasks. The app is built using
         React and follows a component-based architecture to maintain clear separation of concerns and reusable UI 
         elements. Users can add, edit, delete, and mark tasks as complete. The app provides a clean and interactive 
         user interface, and its functionality is driven by React’s state management and event handling.
         
         """ ,
         "link": "https://taskmate-quickcheck.netlify.app/"},

    ]

    for project in project_data:
        st.subheader(project["name"])
        st.write(project["description"])
        st.write(f"[Project Link]({project['link']})")

# Skills Section
elif page == "Skills":
    st.header("Skills")

    skills = {
        "✒️ Programming Languages": ["Python", "JavaScript", "Java","MySQL","MS SQL server",".net"],
        "🪩 Web Development": ["HTML", "CSS", "Django", "Flask","React Js","Spring Boot","Tailwind Css"," Boot strap"],
        #"📊 Data Science": ["Pandas", "NumPy"],
        "⚒️ Tools": ["Git", "Pycharm", "VS Code", "Eclipse"]
    }

    for skill_category, skill_list in skills.items():
        st.subheader(skill_category)
        st.write(", ".join(skill_list))

# Contact Section
elif page == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out to me on the following platforms:")

    st.write("📧 Email: pratikshapatil8987@gmail.com")
    st.write("🔗 LinkedIn: linkedin.com/in/pratiksha-patil-6a8743102")
    st.write("📞 Phone: +91 9503268963")
    #st.write("🐦 Twitter: [Your Twitter](https://twitter.com/yourhandle)")

# Footer
st.sidebar.title("Stay Connected")
st.sidebar.write("You can also check out my [GitHub](https://github.com/yourprofile) for more projects.")
