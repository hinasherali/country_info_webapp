import streamlit as st  
import matplotlib.pyplot as plt 
import plotly.express as px 

# Dictionary for country flags
country_flags = {
    "palestine": "https://i0.wp.com/www.middleeastmonitor.com/wp-content/uploads/2021/12/20211210_2_51256406_71491009.jpg?fit=1200%2C800&ssl=1",
    "jordan": "https://media.istockphoto.com/id/182826898/photo/jordan-flag.jpg?s=612x612&w=0&k=20&c=fgvRQ5EmJQwta-Su75eDrN5EuI5RWDRAkGvmOcU4TQM=",
    "egypt": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flag_of_Egypt.svg/1920px-Flag_of_Egypt.svg.png"
}

# Function to get country information  
country_data = { 
    "palestine":{
            "Borders": "Palestine shares borders with Israel. It also borders Jordan to the east and Egypt to the southwest.",  
            "Total Area": "6,020 square kilometers (2,320 sq mi)",  
            "Population": "Exceeds five million people",  
            "Capital": "Jerusalem (proclaimed); Ramallah (administrative center)",  
            "Cultural Significance": (  
                "This region has played a major role throughout history as it is important to several of the world's major religions. "  
                "Nearly 98% of all Palestinians are Muslim, and it includes the city of Jerusalem and other holy lands."  
            ),  
            "Humanitarian Situation": (  
                "At least 51,266 Palestinians have been confirmed killed and 116,991 wounded in Israel's war on Gaza since it began 18 months ago. "  
                "The Gaza Government Media Office updated its death toll to more than 61,700, saying thousands of people missing under the rubble are presumed dead."  
            )  
        },
       "jordan": {  
        "Borders": "Jordan shares borders with Saudi Arabia to the south, Iraq to the northeast, Syria to the north, and Israel to the west.",  
        "Total Area": "89,342 square kilometers (34,495 sq mi)",  
        "Population": "10 million",  
        "Capital": "Amman",  
        "Cultural Significance": "Jordan is home to many historical sites, including Petra, a UNESCO World Heritage Site.",  
        "Humanitarian Situation": "Jordan hosts a large number of refugees from neighboring countries."  
    },  
    "egypt": {  
        "Borders": "Egypt shares borders with Libya to the west, Sudan to the south, and Israel to the northeast.",  
        "Total Area": "1,001,450 square kilometers (386,662 sq mi)",  
        "Population": "104 million",  
        "Capital": "Cairo",  
        "Cultural Significance": "Egypt is known for its ancient civilization and monuments, including the Pyramids of Giza.",  
        "Humanitarian Situation": "Egypt faces challenges related to poverty and economic development."  
    }
}  
def get_country_info(country):   
        return country_data.get(country.lower(), {"error": "Country information not available."}) 

# Set the title of the app  
st.title("Country Information Web App")  
 
# Search bar  
country_name = st.text_input("Enter the name of the country  (e.g. Palestine, Jordan, Egypt):", "Palestine")   

# Add the flag based on the country selected
flag_url = country_flags.get(country_name.lower(), "")
if flag_url:
    st.image(flag_url, width=200)
else:
   st.warning("Flag not available.")

# Retrieve country information  
country_info = get_country_info(country_name)  

if "error" in country_info:  
    st.error(country_info["error"])  
else:  
    # Column layout for country information cards  
    st.header(f"Overview of {country_name.title()}")  

    # Create columns for cards  
    col1, col2, col3 = st.columns(3)  

    # Borders Card  
    with col1:  
        st.subheader("Borders")  
        st.write(country_info["Borders"])  

    # Capital Card  
    with col2:  
        st.subheader("Capital")  
        st.write(country_info["Capital"])  

    # Language Card  
    with col3:  
        st.subheader("Primary Language")  
        st.write("Arabic")  

    # Area and Population Cards  
    col4, col5 = st.columns(2)  

    with col4:  
        st.subheader("Total Area")  
        st.write(country_info["Total Area"])  

    with col5:  
        st.subheader("Population")  
        st.write(country_info["Population"])  

    # Cultural Significance Card  
    st.subheader("Cultural Significance")  
    st.write(country_info["Cultural Significance"])  

    # Humanitarian Situation  
    st.header("Humanitarian Situation")  
    st.markdown(country_info["Humanitarian Situation"])  

    # Population and Area Data for Graphs  
    population = 5.0  # Population in millions for Palestine  
    land_area = 6020  # Land area in square kilometers for Palestine  

    # Create a pie chart for population distribution  
    fig1 = plt.figure(figsize=(6, 4))  
    labels = ['Population', 'Remaining Area']  
    sizes = [population, 7.5 - population]  # Hypothetical total population  
    colors = ['#ff9999', '#66b3ff']  
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)  
    plt.axis('equal')  # Equal aspect ratio ensures the pie is circular.  
    st.subheader("Population Distribution")  
    st.pyplot(fig1)  

    # Create a bar chart for Land Area and Population  
    area_data = {'Category': ['Total Land Area', 'Population'], 'Values': [land_area, population * 1000]}  # Convert population to thousands  

    fig2 = px.bar(area_data, x='Category', y='Values', color='Category',  
                   title='Land Area vs. Population',  
                   color_discrete_sequence=['#66c2a5', '#fc8d62'])  
    st.subheader("Land Area vs. Population")  
    st.plotly_chart(fig2)  

    # Fact Meter showing various attributes with colors  
    st.header("Fact Meter")  
    facts  = {  
    "Cultural Significance": 80,  
    "Religious Importance": 90,  
    "Language": 100,  
    "Historical Role": 70  
} 
facts = country_info.get("facts",{}) 
fact_labels = list(facts.keys())  
fact_values = list(facts.values())  

# Create a fact meter for various attributes  
fig3, ax = plt.subplots(figsize=(10, 5))  
colors = ['#4CAF50' if value >= 75 else '#FFC107' if value >= 50 else '#F44336' for value in fact_values]  
bars = ax.barh(fact_labels, fact_values, color=colors)  
ax.set_xlim(0, 100)  
ax.set_xlabel('Percentage')  
ax.set_title('Fact Meter: Different Attributes of Palestine')  

# Add data labels  
for bar in bars:  
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, f'{bar.get_width()}%', va='center')  

st.pyplot(fig3)  

# Footer  
st.markdown("---")  
st.write("This app provides a comprehensive overview of Palestine's geography, culture, and humanitarian situation.")  
st.write("Made with ❤️ for Palestine by Hina Sher using Streamlit — thanks for using it!❤️")
