import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO

# App description
st.markdown('''
# Image Background Remover

- Author: `Steven Ngo`
- Source Code: https://github.com/steven-ngo/Image-Background-Remover
- Language: `Python`
- Libraries: `streamlit` `rembg` `Pillow`
''')
st.write('---')

uploaded = st.file_uploader('Upload an image Here', type=[ 'jpg', 'png', 'jpeg'])

st.markdown('\n')

col1, col2 = st.columns(2)

if (uploaded):
   if uploaded.size > 5242880:  #if greater than 5MB
        st.error("The Image is too large. Must less than 5MB.")
   else:
      original = Image.open(uploaded)
      edited = remove(original)

      buf = BytesIO()
      edited.save(buf, format="PNG")
      
      st.download_button("Download edited image", buf.getvalue(), "edited.png", "image/png")


      col1.image(original, caption='Original')
      col2.image(edited,caption='Edited')

else:
   col1.image('./cat.png', caption='Original')
   col2.image('./edited.png',caption='Edited')
