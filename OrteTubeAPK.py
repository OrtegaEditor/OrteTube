import streamlit as st
import os
from pytubefix import YouTube

st.set_page_config(page_title="OrteTube", layout="wide")

st.markdown("# 📱 **OrteTube**")
st.markdown("*Fonctionne sur Android/PC/iOS*")

# Interface simple
col1, col2 = st.columns([3, 1])

with col1:
    url = st.text_input("📎 **URL YouTube**", 
                       placeholder="https://youtu.be/XXXXX")
    dossier = st.text_input("📁 **Dossier**", value=os.getcwd())

with col2:
    st.markdown("### **Statut**")
    if 'status' not in st.session_state:
        st.session_state.status = "🟢 Prêt"

if st.button("🚀 **TÉLÉCHARGER**", type="primary"):
    if not url.strip():
        st.error("❌ URL manquante")
    else:
        with st.spinner("🔄 Téléchargement en cours..."):
            try:
                # Analyse simple
                st.info("🔍 **Analyse vidéo...**")
                yt = YouTube(url)
                
                st.success(f"📹 **{yt.title[:50]}**")
                st.info(f"🎥 **{yt.length//60}:{yt.length%60:02d}**")
                
                # Téléchargement direct
                stream = yt.streams.get_highest_resolution()
                st.info(f"⬇️ **{stream.resolution}**")
                
                stream.download(dossier or ".")
                
                st.success("🎉 **TÉLÉCHARGÉ !**")
                st.balloons()
                st.session_state.status = "✅ OK"
                
            except Exception as e:
                st.error(f"❌ **Erreur :** {str(e)[:100]}")
                st.session_state.status = "❌ Erreur"

# Sidebar
with st.sidebar:
    st.markdown("""
    ### 📋 **Comment utiliser**
    1. Copie URL YouTube
    2. Colle ici
    3. Clique **TÉLÉCHARGER**
    4. Vidéo dans ton dossier !
    """)
    
    st.markdown("### 🛠️ **Stack**")
    st.markdown("- Streamlit")
    st.markdown("- pytubefix")
    st.markdown("- Python")

st.markdown("---")
st.markdown("* Ortega Editor - 2026 ")
