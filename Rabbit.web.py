import streamlit as st
import pyrebase
from datetime import datetime
from streamlit_option_menu import option_menu
from PIL import Image
import requests
import streamlit.components.v1 as components
import random
import json
from io import BytesIO
import feedparser
import urllib.request




#streamlit-1.16.0


im = Image.open("icons8-rabbit-100.png")
st.set_page_config(
    page_title="Rabbit.web",
    page_icon=im
   
)


#https://i.gifer.com/Cal.gif




hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


firebaseConfig = {
  "apiKey": "AIzaSyCHnlRFW1_RTgZVVga8E-Rj4g7noddYzXA",
  "authDomain": "rabbit1-bd232.firebaseapp.com",
  "databaseURL": "https://rabbit1-bd232-default-rtdb.firebaseio.com",
  "projectId": "rabbit1-bd232",
  "storageBucket": "rabbit1-bd232.appspot.com",
  "messagingSenderId": "291333251174",
  "appId": "1:291333251174:web:6daeb9908880347a6ecda7",
  "measurementId": "G-H1NRRJQRHT"
}

firebase= pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

data=firebase.database()
storage=firebase.storage()



query_params = {
  "orderBy": "\"timestamp\"",
  "limitToLast": 1
}
query_string = "?" + "&".join([f"{key}={value}" for key, value in query_params.items()])

latest_post = data.child("Posts").get(query_string).val()











st.markdown("<center><img src=https://img.icons8.com/ios-filled/100/228BE6/rabbit.png; alt=centered image; height=100; width=100> </center>",unsafe_allow_html=True)
labela=("<h1 style='font-family:arial;color:#228BE6;text-align:center'>Rabbit.web</h1>")
st.markdown(labela,unsafe_allow_html=True)
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

placeholder = st.empty()
with placeholder.container():
    label=("<h1 style='font-family:arial;color:#228BE6;text-align:center'>Welcome to  Rabbit.web</h1>")
    st.markdown(label,unsafe_allow_html=True)
    label=("<h5 style='font-family:arial;color:#228BE6;text-align:left'>At  Rabbit.web you can do the following thing's :</h5>")
    st.markdown(label,unsafe_allow_html=True)
    labelc=("<h5 style='font-family:arial;color:#228BE6;text-align:left'>~You can share your thought's </h5>")
    st.markdown(labelc,unsafe_allow_html=True)


    labeld=("<h5 style='font-family:arial;color:#228BE6;text-align:left'>~You can see the post's from people</h5>")
    st.markdown(labeld,unsafe_allow_html=True)
    labeld=("<h5 style='font-family:arial;color:#228BE6;text-align:left'>~You can check the latest new's</h5>")
    st.markdown(labeld,unsafe_allow_html=True)
  




label=("<h1 style='font-family:arial;color:#228BE6;text-align:center'>Rabbit.web</h1>")
st.sidebar.markdown(label,unsafe_allow_html=True)

labelb=("<h4 style='font-family:arial;color:#228BE6;text-align:center'>A perfect place to chat with your friend's</h4>")
st.sidebar.markdown(labelb,unsafe_allow_html=True)

choice=st.sidebar.selectbox("Sign in to your account or create an account :",["sign in","create an account"])



email=st.sidebar.text_input("",placeholder="Hello please enter you email")
passw=st.sidebar.text_input("",placeholder="Hello please enter your password",type="password")



if choice=="create an account":
    handle=st.sidebar.text_input("",placeholder="Hello please enter your name")
    subbt=st.sidebar.button("Create an new account")

    if subbt:
        placeholder.empty()
        user=auth.create_user_with_email_and_password(email,passw)
        st.success("Your Rabbit.web account has created successfully !")
     
        user=auth.sign_in_with_email_and_password(email,passw)
        data.child(user["localId"]).child("Handle").set(handle)
        data.child(user["localId"]).child("ID").set(user["localId"])
        st.info("You can now log in")



       
if choice=="sign in":
   
    signin=st.sidebar.checkbox("sign in")
    

    if signin:
            placeholder.empty()
            user=auth.sign_in_with_email_and_password(email,passw)

          
            #"Follower's"  "list-task"
            nav = option_menu(menu_title=None,   options=["Home", "Friend's","New's", "Setting's","About us"],icons=["house","person","list-task", "gear","info"],menu_icon="cast",default_index=2,orientation="vertical",styles={
        "container": {"padding": "0!important", "background-color": "#1c1c1c"},
        "icon": {"color": "lightblue", "font-size": "15px"}, 
        "nav-link": {"text-align":"left", "margin":"1px", "--hover-color": "#1c1c1c"},
        "nav-link-selected": {"background-color": "#228BE6","color":"#1c1c1c"},})
            
            if nav =="Home":


                st.write(f"#### Share your thought's/post's :")
                post=st.text_input("",placeholder="share your thought with your friend's",max_chars=250)
                add_post=st.button("Share your thought")

                
                   

   
    
                

                    
                if add_post:
                    now=datetime.now()
                    dt=now.strftime("%d / %m / %y")
                    dtt=now.strftime("%I:%M %p")

                    post="Post: "+post+ ";"+"  Posted on:"+ dt +"  at  "+dtt
                    results=data.child(user["localId"]).child("Posts").push(post)
                    st.balloons()


         #      st.write("Upload an image")
                
              #  caption = st.text_input("",placeholder="Add a caption to your image")
               # expan=st.expander("Upload an image")

               # with expan:
                 #   image = st.file_uploader("", type=["jpg", "jpeg", "png","mp3"])
                   
                   # if image is None:
                      #  st.warning("Please select an image")
                    #upbta=st.button("Upload the image and caption")

                   # if upbta:
                       # with st.spinner("Uploading image..."):
                           # storage.child("images/" + image.name).put(image)
                           # post_data = {"caption": caption,"image_url": storage.child("images/" + image.name).get_url(None) }
                           # data.child("posts").push(post_data)
                            #st.success("Post added successfully")'''
                components.html("""<hr style="height:2px;border:none;color:#333;background-color:white;" /> """)
                col1,col2=st.columns(2)

                with col1:
                    nimg=data.child(user["localId"]).child("Image").get().val()
                    if nimg is not None:
                        v=data.child(user["localId"]).child("Image").get()
                        for img in v.each():
                            imgc=img.val()
                        
                        st.markdown(f'<img src="{imgc}" width="200" height="200" style="border-radius:50%;">', unsafe_allow_html=True)
                        
                       
                    else:
                         st.info("Oop's no profile pic till now ")
                    
                
            

                with col2:
                    st.title("Post's :")
                    st.write(f"###### ______________________________________________________")
                    all_posts=data.child(user['localId']).child("Posts").get()
                    all_imgs=data.child(user['localId']).child("images").get()
                    
                    if all_posts.val() is not None:
                        for Posts in reversed(all_posts.each()):
                            
                            st.success(Posts.val())
                            if st.button("🗑 Delete this post ",key=f"Delete_({Posts.key()})"):
                                 data.child(user["localId"]).child("Posts").child(Posts.key()).remove()
                                 
                       
                            
                             
                            st.write(f"###### ______________________________________________________")
                            
                             
                             
                             
                 
                            
                   
                    else:
                            st.info("Oop's no thought till now")


                  #  posts = data.child("posts").get()
                    #for post in posts.each():
                        #caption = post.val()["caption"]
                        #image_url = post.val()["image_url"]
                      
                        #st.write(caption)
                        #response = requests.get(image_url)
                        #img = Image.open(BytesIO(response.content))
                        #st.image(img, caption=caption, use_column_width=True)
                        #components.html("""<hr style="height:2px;border:none;color:#333;background-color:white;" /> """)
                    
                        
                col3=st.columns(1)
                with col1:
                    st.title("Bio :")
                    all_bio=data.child(user["localId"]).child("Bio").get()

                    if all_bio.val() is not None:
                        
                        bio=data.child(user["localId"]).child("Bio").get()
                        for bio in bio.each():
                            bioc=bio.val()
                        st.info(bioc)
                    else:
                        st.info("Oop's no Bio  till now")
                
                
            elif nav =="Setting's":
                    nimg=data.child(user["localId"]).child("Image").get().val()
                    
                    if nimg is not None:
                        Image=data.child(user["localId"]).child("Image").get()
                        for img in Image.each():
                            imgc=img.val()
                        
                        st.markdown(f'<img src="{imgc}" width="200" height="200" style="border-radius:50%;">', unsafe_allow_html=True)

                        expa=st.expander("Change your profile pic")

                        with expa:
                            newimgp=st.file_uploader("Please choose  your profile pic")
                            upbt=st.button("Upload profile pic")
                            if upbt:
                                uid=user["localId"]
                                dataup=storage.child(uid).put(newimgp,user["idToken"])
                                aimgdata=storage.child(uid).get_url(dataup["downloadTokens"])

                                data.child(user["localId"]).child("Image").push(aimgdata)
                               

                                st.info("Your profile pic is set successfully")
                                st.balloons()
                    else:
                                st.info("Oop's no profile pic till now")
                                newimgp=st.file_uploader("Please  choose your profile pic")
                                upbt=st.button("Upload profile pic")
                                if upbt:
                                    uid=user["localId"]
                                    dataup=storage.child(uid).put(newimgp,user["idToken"])
                                    aimgdata=storage.child(uid).get_url(dataup["downloadTokens"])
                                    data.child(user["localId"]).child("Image").push(aimgdata)

                    bio=data.child(user["localId"]).child("Bio").get().val()
                    if bio is not None:
                        bio=data.child(user["localId"]).child("Bio").get()
                        for bio in bio.each():
                            bioc=bio.val()
                        st.info(bioc)

                        bioin=st.text_area("",placeholder="Enter your Bio to be uploaded eg: name,date of birth etc")
                        upbtn=st.button("Upload Bio")

                        if upbtn:
                           
                            

                            data.child(user["localId"]).child("Bio").push(bioin)

                            st.info("Your Bio is set successfully")
                            st.balloons()
                    
                    else:
                        st.info("Oop's no Bio till now")
                        bioin=st.text_area("",placeholder="Enter your Bio to be uploaded eg: name,date of birth etc")
                        upbtn=st.button("Upload Bio")

                        if upbtn:
                           
                           
                            data.child(user["localId"]).child("Bio").push(bioin)

                            st.info("Your Bio is set successfully")
                            st.balloons()
                   
               

            elif nav=="Friend's":
                

                allu=data.get()
                resa=[]

                for ush in allu.each():
                  
                    k=ush.val().get("Handle")
                    resa.append(k)
            
                n = len(resa)
            
                st.title("Search your Friend's :")
                cho = st.selectbox('',resa)
                pusha = st.button('Show Profile')


                
                if pusha:
                    for ush in allu.each():
                        k=ush.val().get("Handle")
                        if k==cho:
                            l=ush.val().get("ID")

                            hn=data.child(l).child("Handle").get().val()

                            st.markdown(hn,unsafe_allow_html=True)
                            components.html("""<hr style="height:2px;border:none;color:#333;background-color:white;" /> """)
                            col1,col2=st.columns(2)
                            with col1:
                                nimg=data.child(l).child("Image").get().val()
                                if nimg is not None:
                                    v=data.child(l).child("Image").get()
                                    for img in v.each():
                                        imgc=img.val()
                                    
                                    st.markdown(f'<img src="{imgc}" width="200" height="200" style="border-radius:50%;">', unsafe_allow_html=True)
                       
                                else:
                                    st.info("Oop's no profile pic till now ")
                                
                                
                
                                
                            

                            with col2:
                                st.title("Post's :")
                                st.write(f"###### ______________________________________________________")
                                all_posts=data.child(l).child("Posts").get()
                                if all_posts.val() is not None:
                                    for Posts in reversed(all_posts.each()):
                                         st.success(Posts.val())
                                         
                                         st.write(f"###### ______________________________________________________")
                                       
                                else:
                                    st.info("Oop's no thought till now")
                               
                    
                            col3=st.columns(1)
                            with col1:
                                st.title("Bio :")
                                all_bio=data.child(l).child("Bio").get()

                                if all_bio.val() is not None:
                                    bio=data.child(l).child("Bio").get()
                                    for bio in bio.each():
                                        bioc=bio.val()
                                        st.info(bioc)
                                else:
                                   st.info("Oop's no Bio  till now")
            elif nav=="New's":

                st.title("Have a look at today's latest new's :")
                components.html("""<hr style="height:2px;border:none;color:#333;background-color:white;" /> """)
                news_feed = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/World.xml")
                
               
                for item in news_feed.entries:
                    try:
                        st.write(f"## {item.title}")
                        st.write(item.summary)
                        image_url = item.media_content[0]["url"]
                        image_file = urllib.request.urlopen(image_url)
                        image = Image.open(image_file)
                        st.write(f"[Read more]({item.link})")
                   
                        st.image(image, caption="", use_column_width=True)
                        st.write(f"###### ______________________________________________________")
                    except:
                        st.write("")
                    
                    
                   
                #st.info("Sorry this page is currently under construction")
                #st.markdown("<center><h1>⚠️</h1>  </center>",unsafe_allow_html=True)
                #st.components.v1.html('<iframe src="https://giphy.com/embed/hV1dkT2u1gqTUpKdKy" frameBorder=0></iframe>', width=800, height=800)


              
            else:
                 st.write("Rabbit.web")
                 st.write("Created and maintained by Navpreet Singh")
                 st.write("For help,feedback or suggestion contact our company at rabbitweb854@gmail.com")
                 st.write("For reporting a user on Rabbit.web  contact us at rabbitweb854@gmail.com")
                

#{"rules": {
 #   ".read": "now < 1682706600000",  // 2023-4-29
   # ".write": "now < 1682706600000",  // 2023-4-29
  #}
#}
      
                  

                  
                 

                    
                    
            
                
            
                                    
