
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

st.title("🧬 Cancer Subtype Discovery Dashboard")
st.markdown("Explore gene expression clustering using unsupervised learning.")

uploaded_file = st.file_uploader("Upload your gene expression matrix (CSV)", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file, index_col=0)
    data_t = data.T  # Samples as rows

    # PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(data_t)
    pca_df = pd.DataFrame(pca_result, columns=["PC1", "PC2"])

    # KMeans
    kmeans = KMeans(n_clusters=3, random_state=42)
    pca_df["Cluster"] = kmeans.fit_predict(pca_df)

    st.subheader("📊 PCA + KMeans Clustering")
    fig, ax = plt.subplots()
    sns.scatterplot(data=pca_df, x="PC1", y="PC2", hue="Cluster", palette="Set2", ax=ax)
    st.pyplot(fig)

    st.subheader("📈 Explained Variance by PCA")
    explained_var = pca.explained_variance_ratio_
    st.bar_chart({"Explained Variance": explained_var})
else:
    st.info("Upload a CSV file to begin analysis.")
