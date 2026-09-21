import streamlit as st
import urllib.parse

WHATSAPP_NUMBER = "+923190223849"

st.set_page_config(
    page_title="TechCart",
    page_icon="🎬",
    layout="wide"
)

st.title("💻 TechCart")
st.write("✨ Smart Products, Simple Shopping ✨")

menu = st.radio("Menu",
                ["Home","Products","Categories","About","Contact"],
                horizontal=True)

st.divider()

if menu == "Home":

    st.header("Welcome to TechCart")
    
    st.subheader("Smart Products. Simple Shopping.")
    
    st.write(
        "Discover useful and affordable technology products "
        "for your everyday needs."
    )

    st.button("🛍️ Shop Now")

    st.divider()

    st.header("Why Shop With Us?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("✅ Quality Products")
        st.write("We offer reliable and useful products.")

    with col2:
        st.subheader("💰 Affordable Prices")
        st.write("Get great products at reasonable prices.")

    with col3:
        st.subheader("🚚 Easy Ordering")
        st.write("Order your favorite products easily.")

elif menu == "Products":
    st.header("Our Products")
    st.write("Explore our products collection....")
    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("earbuds.PNG", use_container_width=True)
        st.subheader("Premium Earbuds")
        st.write("Comfortable wireless earbuds")
        st.write("Price: Rs. 1500")
        message = """Hello! I am Intereted in ordering:
        Product: Premium Earbuds
        Price: 1500 RS
        Please provide more details
        """
        # FIXED LINE BELOW: Added the missing forward slash after wa.me
        whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(message)}"
        
        st.link_button("🛍️ Shop Now",whatsapp_url)

    with col2:
        st.image("laptop.PNG", use_container_width=True)
        st.subheader("Laptop")
        st.write("8th generation laptop")
        st.write("Price: Rs. 15000")
        message = """Hello! I am Intereted in ordering:
        Product: HP Laptop
        Price: 15000 RS
        Please provide more details
        """
        # FIXED LINE BELOW: Added the missing forward slash after wa.me
        whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(message)}"
        
        st.link_button("🛍️ Shop Now",whatsapp_url)


    with col3:
        st.image("mouse.PNG", use_container_width=True)
        st.subheader("Mouse")
        st.write("Wireless laptop mouse")
        st.write("Price: Rs. 3000")
        message = """Hello! I am Intereted in ordering:
        Product: Mouse
        Price: 3000 RS
        Please provide more details
        """
        # FIXED LINE BELOW: Added the missing forward slash after wa.me
        whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(message)}"
        
        st.link_button("🛍️ Shop Now",whatsapp_url)



    
elif menu == "Categories":
    st.header("Product Categories")
    st.write("Our product categories will appear here...")

elif menu == "About":
    st.header("About TechCart")
    st.write("Learn more about our store.......")

elif menu == "Contact":
    st.header("Contact Us")
    st.write("Contact Section will appear here")