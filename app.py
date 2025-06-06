
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from io import BytesIO

st.set_page_config(page_title="Cancer Subtype Discovery", layout="wide")
st.title("🧬 Advanced Cancer Subtype Discovery Dashboard")

# Upload CSV
uploaded_file = st.sidebar.file_uploader("Upload gene expression matrix (CSV)", type=["csv"])
min_var = st.sidebar.slider("Filter genes by minimum variance:", 0.0, 2.0, 0.2, step=0.05)

if uploaded_file:
    df = pd.read_csv(uploaded_file, index_col=0)

    # Transpose: samples as rows
    df = df.loc[df.var(axis=1) > min_var]
    data = df.T

    st.subheader("📊 Dataset Overview")
    st.write(f"Shape: {data.shape}")
    st.write("Top 5 genes by variance:")
    st.dataframe(df.var(axis=1).sort_values(ascending=False).head())

    # PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(data)
    pca_df = pd.DataFrame(pca_result, columns=["PC1", "PC2"])
    explained_var = pca.explained_variance_ratio_

    # KMeans
    k = st.sidebar.slider("Number of clusters (KMeans):", 2, 10, 3)
    kmeans = KMeans(n_clusters=k, random_state=42)
    pca_df["Cluster"] = kmeans.fit_predict(pca_df)
    sil_score = silhouette_score(pca_df[["PC1", "PC2"]], pca_df["Cluster"])

    # t-SNE
    tsne = TSNE(n_components=2, random_state=42, perplexity=10)
    tsne_result = tsne.fit_transform(data)
    tsne_df = pd.DataFrame(tsne_result, columns=["tSNE1", "tSNE2"])
    tsne_df["Cluster"] = pca_df["Cluster"]

    # UMAP (optional)
    try:
        import umap
        reducer = umap.UMAP(random_state=42)
        umap_result = reducer.fit_transform(data)
        umap_df = pd.DataFrame(umap_result, columns=["UMAP1", "UMAP2"])
        umap_df["Cluster"] = pca_df["Cluster"]
    except ImportError:
        umap_df = None

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📈 PCA", "🔁 t-SNE", "🔀 UMAP", "📉 Expression Heatmap"])

    with tab1:
        st.write(f"Silhouette Score: {sil_score:.2f}")
        fig, ax = plt.subplots()
        sns.scatterplot(data=pca_df, x="PC1", y="PC2", hue="Cluster", palette="tab10", ax=ax)
        st.pyplot(fig)

    with tab2:
        fig, ax = plt.subplots()
        sns.scatterplot(data=tsne_df, x="tSNE1", y="tSNE2", hue="Cluster", palette="tab10", ax=ax)
        st.pyplot(fig)

    with tab3:
        if umap_df is not None:
            fig, ax = plt.subplots()
            sns.scatterplot(data=umap_df, x="UMAP1", y="UMAP2", hue="Cluster", palette="tab10", ax=ax)
            st.pyplot(fig)
        else:
            st.warning("UMAP not installed. Run `pip install umap-learn` to enable.")

    with tab4:
        if df.shape[0] <= 50:
            fig = sns.clustermap(df, cmap="vlag", standard_scale=1)
            st.pyplot(fig.fig)
        else:
            st.warning("Too many genes for heatmap. Lower variance threshold to view.")

    # Download cluster assignments
    output_df = pd.DataFrame(data.index)
    output_df["Cluster"] = pca_df["Cluster"].values
    csv = output_df.to_csv(index=False).encode()
    st.download_button("📤 Download Cluster Assignments", csv, "cluster_assignments.csv", "text/csv")
else:
    st.info("Upload a CSV file to begin analysis.")
