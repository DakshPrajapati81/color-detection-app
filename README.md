# 🎨 Color Detection Web Application

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A powerful and interactive web application that detects colors from uploaded images using **Machine Learning** concepts, **Computer Vision**, and **Python**. Built with Streamlit for a clean, user-friendly interface.

## 🌐 Live Demo

**Deployed Application:** [Your Deployment Link Here]

*Replace with your actual deployment link from Streamlit Cloud, Render, or Hugging Face Spaces*

---

## 📸 Screenshots

### Main Interface
![Main Interface](screenshots/main_interface.png)

### Color Detection
![Color Detection](screenshots/color_detection.png)

### Dominant Colors
![Dominant Colors](screenshots/dominant_colors.png)

*Note: Add screenshots folder with actual images of your running application*

---

## ✨ Features

### Core Features
- ✅ **Image Upload:** Support for JPG, JPEG, PNG formats
- ✅ **Real-time Color Detection:** Click on any pixel to detect its color
- ✅ **RGB & HEX Values:** Display precise color values
- ✅ **Color Name Recognition:** Match with 140+ predefined colors
- ✅ **Interactive UI:** Beautiful, responsive design with Streamlit

### Advanced Features
- 🌈 **Dominant Color Extraction:** Uses K-Means clustering to find top 6 colors
- 🎨 **Color Palette Display:** Visual representation of dominant colors
- 📊 **Image Statistics:** Display width, height, and pixel count
- 🔍 **Manhattan Distance Algorithm:** Accurate color matching using ML distance formula
- ⚡ **Performance Optimization:** Automatic image resizing for faster processing

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Web framework for interactive UI |
| **OpenCV (cv2)** | Image processing and computer vision |
| **NumPy** | Numerical computations and array operations |
| **Pandas** | Data manipulation and CSV handling |
| **Pillow (PIL)** | Image handling and conversion |

### Machine Learning Concepts Applied
1. **K-Nearest Neighbors (K-NN):** Finding closest color match (K=1)
2. **Manhattan Distance:** Distance metric for color similarity
   ```
   distance = |R - r| + |G - g| + |B - b|
   ```
3. **K-Means Clustering:** Extracting dominant colors from images
4. **Feature Extraction:** RGB color space as feature vectors

---

## 📋 Prerequisites

Before running this application, ensure you have:

- Python 3.8 or higher installed
- pip (Python package manager)
- Basic understanding of command line/terminal

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/color-detection-app.git
cd color-detection-app
```

### Step 2: Create Virtual Environment (Recommended)

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install streamlit opencv-python pandas numpy pillow
```

### Step 4: Verify Installation

Check if all packages are installed correctly:
```bash
pip list
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your default browser at `http://localhost:8501`

---

## 📁 Project Structure

```
color-detection-app/
│
├── app.py                  # Main Streamlit application
├── colors.csv              # Color dataset (140+ colors)
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore file
│
├── screenshots/           # Application screenshots
│   ├── main_interface.png
│   ├── color_detection.png
│   └── dominant_colors.png
│
└── LICENSE                # MIT License
```

---

## 💡 How to Use

### Basic Usage

1. **Launch the Application**
   ```bash
   streamlit run app.py
   ```

2. **Upload an Image**
   - Click on "Browse files" button
   - Select an image (JPG, PNG, JPEG)
   - Image will be displayed automatically

3. **Detect Colors**
   - **Method 1:** Enter X and Y coordinates, then click "Detect Color at Position"
   - **Method 2:** Click "Detect Center Color" for quick detection
   
4. **View Results**
   - Color Name (e.g., "Sky Blue")
   - RGB Values (e.g., 135, 206, 235)
   - HEX Code (e.g., #87CEEB)
   - Visual color preview box

5. **Extract Dominant Colors**
   - Scroll down to "Dominant Colors" section
   - Click "Extract Dominant Colors" button
   - View color palette with names and RGB values

---

## 🧮 Algorithm Explanation

### Color Detection Algorithm

```python
def get_color_name(R, G, B):
    minimum_distance = infinity
    
    for each color in dataset:
        # Calculate Manhattan distance
        distance = |R - color.R| + |G - color.G| + |B - color.B|
        
        if distance < minimum_distance:
            minimum_distance = distance
            closest_color = color
    
    return closest_color.name, closest_color.hex
```

### Distance Formula
**Manhattan Distance** (L1 Norm):
```
d = |R₁ - R₂| + |G₁ - G₂| + |B₁ - B₂|
```

Where:
- (R₁, G₁, B₁) = Clicked pixel RGB values
- (R₂, G₂, B₂) = Dataset color RGB values
- d = Total distance

The color with minimum distance is the closest match!

---

## 📊 Dataset Information

The `colors.csv` file contains **140+ colors** with the following structure:

| Column | Description | Example |
|--------|-------------|---------|
| color_name | Name of the color | "Sky Blue" |
| hex | Hexadecimal code | "#87CEEB" |
| R | Red channel (0-255) | 135 |
| G | Green channel (0-255) | 206 |
| B | Blue channel (0-255) | 235 |

---

## 🌐 Deployment Guide

### Deploy on Streamlit Cloud (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your GitHub repository
   - Choose `app.py` as main file
   - Click "Deploy"

3. **Get Deployment URL**
   - URL will be: `https://your-username-app-name.streamlit.app`

### Alternative: Deploy on Render

1. Create `render.yaml`:
```yaml
services:
  - type: web
    name: color-detection-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

2. Connect GitHub repo to Render
3. Deploy automatically

### Alternative: Hugging Face Spaces

1. Create new Space on [huggingface.co/spaces](https://huggingface.co/spaces)
2. Choose "Streamlit" as SDK
3. Upload your files
4. Deploy automatically

---

## 📦 requirements.txt

```txt
streamlit==1.28.0
opencv-python==4.8.1.78
numpy==1.24.3
pandas==2.0.3
Pillow==10.0.1
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

---

## 🐛 Known Issues & Troubleshooting

### Issue: "colors.csv not found"
**Solution:** Ensure `colors.csv` is in the same directory as `app.py`

### Issue: ModuleNotFoundError
**Solution:** Install all requirements:
```bash
pip install -r requirements.txt
```

### Issue: Image not displaying
**Solution:** Check image format (must be JPG, PNG, or JPEG)

### Issue: Slow performance
**Solution:** Image is automatically resized. If still slow, reduce max_width in resize_image() function

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/your-profile)
- Email: your.email@example.com

---

## 🎓 Academic Information

**Project Type:** Machine Learning Academic Project  
**Course:** Machine Learning & Computer Vision  
**Institution:** Your University Name  
**Year:** 2026  
**Submission Date:** April 20, 2026

---

## 🙏 Acknowledgments

- Color dataset compiled from web standards
- Built with [Streamlit](https://streamlit.io) framework
- OpenCV for image processing capabilities
- Python community for excellent libraries

---

## 📈 Project Statistics

![GitHub stars](https://img.shields.io/github/stars/your-username/color-detection-app)
![GitHub forks](https://img.shields.io/github/forks/your-username/color-detection-app)
![GitHub issues](https://img.shields.io/github/issues/your-username/color-detection-app)
![GitHub pull requests](https://img.shields.io/github/issues-pr/your-username/color-detection-app)

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-username/color-detection-app/issues) page
2. Create a new issue with detailed description
3. Contact via email: your.email@example.com

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!

---

**Made with ❤️ and Python**
