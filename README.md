# cancer-subtype-discovery
##run this in powershell (replace with your path)
& "C:\Users\ekramah\AppData\Roaming\Python\Python310\Scripts\streamlit.exe" run "F:\cancer-subtype-discovery\cancer-subtype-discovery\app.py"
Here is a fully detailed and recruiter-friendly `README.md` for your **Cancer Subtype Discovery Tool**:

---

````markdown
# 🧬 Cancer Subtype Discovery using Unsupervised Learning

This project is an interactive **Streamlit-based bioinformatics dashboard** designed to discover **cancer subtypes** using gene expression data. It applies machine learning techniques like **PCA**, **t-SNE**, **UMAP**, and **K-Means clustering** to analyze high-dimensional transcriptomic datasets. The tool is ideal for bioinformatics research, educational demos, and showcasing machine learning skills in biology.

---

## 🚀 Live Demo (Local)

> Make sure Streamlit is installed (see instructions below)

```bash
streamlit run app.py
````

---

## 📁 Project Structure

```
cancer-subtype-discovery/
│
├── app.py                     # Main Streamlit app
├── requirements.txt           # All dependencies
├── notebooks           
├── data/               # (Optional) Example gene expression files
├── report/                    # Summary PDF output
├── docs/                      # GitHub Pages static site (optional)
└── README.md                  # You're here
```

---

## 🛠 Features

| Feature                    | Description                                                 |
| -------------------------- | ----------------------------------------------------------- |
| 📥 Upload CSV              | Upload your gene expression matrix (genes × samples) (or download from GEOWEBSITE
GEO Dataset Example:
Go to GEO: GSE25066
Click "Series Matrix File(s)" under Download section
Open the .txt.gz file in Excel or Python and save it as .csv
|
| 📊 PCA + KMeans Clustering | Visualize sample clusters with silhouette score             |
| 🔁 t-SNE / 🔀 UMAP         | Explore nonlinear manifold projections                      |
| 📉 Expression Heatmap      | Gene-level heatmap (with hierarchical clustering)           |
| ⚙️ Variance Filter         | Select top-variant genes to reduce noise                    |
| 📤 Download Results        | Export cluster assignments as `.csv`                        |
| 🧾 (Optional) PDF Export   | Add-on to generate summary report (not included by default) |

---

## 📈 Example Outputs

* Dimensionality reduction (PCA, t-SNE, UMAP)
* Cluster assignments
* Interactive plots with color-coded samples
* Heatmap of top-expressed genes

---

## 📦 Installation

### Option 1: Using `pip`

```bash
pip install -r requirements.txt
```

### Option 2: Install Manually

```bash
pip install streamlit pandas scikit-learn matplotlib seaborn umap-learn
```

---

## 📄 How to Use

1. Run the app:

```bash
streamlit run app.py
```

2. In your browser, go to:

```
http://localhost:8501
```

3. Upload a **gene expression matrix**:

   * Rows = genes (e.g., `TP53`, `BRCA1`)
   * Columns = samples (e.g., `Sample_1`, `Sample_2`)
   * Values = expression levels (e.g., log2(TPM), counts)

4. Adjust filters:

   * `Number of clusters (KMeans)`
   * `Variance threshold` to exclude low-signal genes

5. Switch between tabs:

   * 📈 PCA
   * 🔁 t-SNE
   * 🔀 UMAP
   * 📉 Heatmap

6. Download `.csv` with cluster assignments.

---

## 🧪 Sample Test Files

Try these for testing (if not already included):

* `gene_expression_test_1.csv`
* `gene_expression_test_2.csv`
* `gene_expression_test_3.csv`

---

## 📚 Acknowledgments

This project was inspired and supported by the following Coursera specializations
#
#
#
## 🎓 Project Purpose
>
> * Biological data handling
> * Real-world machine learning application
> * Interactive visualization and research communication

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🤝 Let's Connect

If you like this project or have suggestions, feel free to fork, star ⭐, or connect with me on GitHub and LinkedIn.

``` & "C:\Users\ramla\AppData\Roaming\Python\Python310\Scripts\streamlit.exe" run "F:\cancer-subtype-discovery\cancer-subtype-discovery\app.py"

