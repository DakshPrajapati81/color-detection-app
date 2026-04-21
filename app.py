"""
Color Detection Web Application
---------------------------------
An interactive web app that detects colors from uploaded images using ML concepts.
Built with Python, OpenCV, Streamlit, and Machine Learning techniques.

Author: Your Name
Date: April 2026
Academic Project Submission
"""

import streamlit as st
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import io

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Color Detection App",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS FOR BEAUTIFUL UI
# ============================================================================

st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #FF6B6B;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #4ECDC4;
        margin-bottom: 2rem;
    }
    .color-box {
        width: 150px;
        height: 150px;
        border-radius: 10px;
        margin: 10px auto;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 3px solid #fff;
    }
    .color-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin: 10px 0;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF6B6B;
        color: white;
        border-radius: 5px;
        padding: 10px;
        font-weight: bold;
    }
    .palette-box {
        width: 80px;
        height: 80px;
        border-radius: 5px;
        display: inline-block;
        margin: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# LOAD COLOR DATASET
# ============================================================================

@st.cache_data
def load_color_data():
    """
    Load the color dataset from CSV file.
    
    Returns:
        pandas.DataFrame: DataFrame containing color names and RGB values
    """
    try:
        df = pd.read_csv('colors.csv')
        return df
    except FileNotFoundError:
        st.error("⚠️ Error: colors.csv file not found! Please ensure it's in the same directory.")
        st.stop()
    except Exception as e:
        st.error(f"⚠️ Error loading dataset: {str(e)}")
        st.stop()

# Load the color dataset
colors_df = load_color_data()

# ============================================================================
# COLOR DETECTION FUNCTIONS
# ============================================================================

def get_color_name(R, G, B):
    """
    Find the closest color name from the dataset using Manhattan distance.
    
    Machine Learning Concept: K-Nearest Neighbors (K-NN) with k=1
    Distance Formula: Manhattan Distance = |R - r| + |G - g| + |B - b|
    
    Args:
        R (int): Red channel value (0-255)
        G (int): Green channel value (0-255)
        B (int): Blue channel value (0-255)
    
    Returns:
        tuple: (color_name, hex_code)
    """
    minimum_distance = float('inf')
    closest_color_name = None
    closest_hex = None
    
    # Iterate through all colors in the dataset
    for idx, row in colors_df.iterrows():
        # Calculate Manhattan distance between clicked color and dataset color
        distance = abs(R - int(row['R'])) + abs(G - int(row['G'])) + abs(B - int(row['B']))
        
        # Update if this is the closest match so far
        if distance < minimum_distance:
            minimum_distance = distance
            closest_color_name = row['color_name']
            closest_hex = row['hex']
    
    return closest_color_name, closest_hex

def rgb_to_hex(r, g, b):
    """
    Convert RGB values to hexadecimal color code.
    
    Args:
        r, g, b (int): RGB values (0-255)
    
    Returns:
        str: Hexadecimal color code (e.g., #FF5733)
    """
    return '#{:02x}{:02x}{:02x}'.format(r, g, b).upper()

def get_dominant_colors(image, k=5):
    """
    Extract dominant colors from image using K-Means clustering.
    
    Machine Learning Concept: K-Means Clustering
    - Groups similar colored pixels together
    - Finds k cluster centers (dominant colors)
    
    Args:
        image (numpy.ndarray): Input image in BGR format
        k (int): Number of dominant colors to extract
    
    Returns:
        list: List of dominant colors in RGB format
    """
    # Reshape image to be a list of pixels
    pixels = image.reshape(-1, 3)
    pixels = np.float32(pixels)
    
    # Define criteria for K-Means
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    
    # Apply K-Means clustering
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    # Convert centers to integer RGB values
    dominant_colors = centers.astype(int)
    
    # Convert BGR to RGB
    dominant_colors = dominant_colors[:, ::-1]
    
    # Count pixels in each cluster to sort by frequency
    unique, counts = np.unique(labels, return_counts=True)
    sorted_indices = np.argsort(-counts)
    
    return dominant_colors[sorted_indices]

def resize_image(image, max_width=800):
    """
    Resize image while maintaining aspect ratio for better performance.
    
    Args:
        image (numpy.ndarray): Input image
        max_width (int): Maximum width in pixels
    
    Returns:
        numpy.ndarray: Resized image
    """
    height, width = image.shape[:2]
    
    if width > max_width:
        ratio = max_width / width
        new_width = max_width
        new_height = int(height * ratio)
        resized = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
        return resized
    
    return image

# ============================================================================
# MAIN APPLICATION UI
# ============================================================================

def main():
    """
    Main application function with Streamlit UI components.
    """
    
    # Application Header
    st.markdown('<h1 class="main-header">🎨 Color Detection Application</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Upload an image and click to detect colors using Machine Learning!</p>', unsafe_allow_html=True)
    
    # Sidebar Information
    with st.sidebar:
        st.markdown("### 📚 About This Project")
        st.info("""
        **Technologies Used:**
        - Python 3.x
        - OpenCV (Computer Vision)
        - Streamlit (Web Framework)
        - Pandas & NumPy (Data Processing)
        - K-Means Clustering (ML)
        
        **Features:**
        ✅ Color Detection from Images  
        ✅ RGB & HEX Code Display  
        ✅ Dominant Color Extraction  
        ✅ Interactive Color Palette  
        ✅ Real-time Processing
        """)
        
        st.markdown("### 🎯 How to Use")
        st.markdown("""
        1. Upload an image (JPG, PNG, JPEG)
        2. Click anywhere on the image
        3. View detected color details
        4. Explore dominant colors
        """)
        
        st.markdown("### 👨‍💻 Developer Info")
        st.markdown("""
        **Project Type:** Academic Submission  
        **Course:** Machine Learning  
        **Year:** 2026
        """)
    
    # File uploader
    uploaded_file = st.file_uploader(
        "📁 Upload an Image",
        type=['jpg', 'jpeg', 'png'],
        help="Supported formats: JPG, JPEG, PNG"
    )
    
    if uploaded_file is not None:
        try:
            # Read and process the uploaded image
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            
            # Resize for better performance
            image = resize_image(image)
            
            # Convert BGR to RGB for display
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Create two columns for layout
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown("### 🖼️ Uploaded Image")
                st.markdown("**👆 Click on any part of the image to detect color**")
                
                # Display image using Streamlit
                st.image(image_rgb, use_column_width=True)
                
                # Get image dimensions for click detection
                height, width = image_rgb.shape[:2]
                
                # Initialize session state for click coordinates
                if 'clicked' not in st.session_state:
                    st.session_state.clicked = False
                    st.session_state.x = 0
                    st.session_state.y = 0
                
                # Click detection using columns (simulation)
                st.markdown("**Click coordinates (x, y):**")
                click_col1, click_col2, click_col3 = st.columns([1, 1, 2])
                
                with click_col1:
                    x_coord = st.number_input("X", min_value=0, max_value=width-1, value=width//2, key="x_input")
                with click_col2:
                    y_coord = st.number_input("Y", min_value=0, max_value=height-1, value=height//2, key="y_input")
                with click_col3:
                    if st.button("🎯 Detect Color at Position", type="primary"):
                        st.session_state.clicked = True
                        st.session_state.x = x_coord
                        st.session_state.y = y_coord
                
                # Alternative: Auto-detect center color
                if st.button("🎨 Detect Center Color", use_container_width=True):
                    st.session_state.clicked = True
                    st.session_state.x = width // 2
                    st.session_state.y = height // 2
            
            with col2:
                st.markdown("### 🎯 Color Detection Result")
                
                if st.session_state.clicked:
                    x = st.session_state.x
                    y = st.session_state.y
                    
                    # Get RGB values at clicked position
                    b, g, r = image[y, x]
                    R, G, B = int(r), int(g), int(b)
                    
                    # Get closest color name from dataset
                    color_name, hex_code = get_color_name(R, G, B)
                    
                    # Display color preview box
                    st.markdown(
                        f'<div class="color-box" style="background-color: rgb({R},{G},{B});"></div>',
                        unsafe_allow_html=True
                    )
                    
                    # Display color information
                    st.markdown(f"""
                    <div class="color-info">
                        <h3 style="margin:0; text-align:center;">🏷️ {color_name}</h3>
                        <hr style="margin:10px 0;">
                        <p><strong>RGB:</strong> ({R}, {G}, {B})</p>
                        <p><strong>HEX:</strong> {rgb_to_hex(R, G, B)}</p>
                        <p><strong>Closest Match:</strong> {hex_code}</p>
                        <p><strong>Position:</strong> ({x}, {y})</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Success message
                    st.success("✅ Color detected successfully!")
                    
                else:
                    st.info("👆 Enter coordinates or click 'Detect Color' button to start")
            
            # Dominant Colors Section
            st.markdown("---")
            st.markdown("### 🌈 Dominant Colors in Image")
            st.markdown("*Extracted using K-Means Clustering Algorithm*")
            
            # Add a button to extract dominant colors
            if st.button("🔍 Extract Dominant Colors", use_container_width=True):
                with st.spinner("Analyzing image colors..."):
                    # Get dominant colors
                    dominant_colors = get_dominant_colors(image, k=6)
                    
                    # Create color palette display
                    palette_cols = st.columns(6)
                    
                    for idx, (col, color) in enumerate(zip(palette_cols, dominant_colors)):
                        R, G, B = color
                        color_name, _ = get_color_name(R, G, B)
                        
                        with col:
                            st.markdown(
                                f'<div class="palette-box" style="background-color: rgb({R},{G},{B});"></div>',
                                unsafe_allow_html=True
                            )
                            st.markdown(f"**{color_name}**")
                            st.caption(f"RGB: ({R},{G},{B})")
                
                st.success("✅ Dominant colors extracted successfully!")
            
            # Statistics
            st.markdown("---")
            st.markdown("### 📊 Image Statistics")
            stat_col1, stat_col2, stat_col3 = st.columns(3)
            
            with stat_col1:
                st.metric("Width", f"{width} px")
            with stat_col2:
                st.metric("Height", f"{height} px")
            with stat_col3:
                st.metric("Total Pixels", f"{width * height:,}")
        
        except Exception as e:
            st.error(f"⚠️ Error processing image: {str(e)}")
            st.info("Please try uploading a different image.")
    
    else:
        # Display instructions when no image is uploaded
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.info("### 📤 Step 1\nUpload an image using the file uploader above")
        with col2:
            st.info("### 🖱️ Step 2\nClick on the image or enter coordinates")
        with col3:
            st.info("### 🎨 Step 3\nView the detected color information")
        
        # Sample information
        st.markdown("---")
        st.markdown("### 🔬 How It Works")
        
        tech_col1, tech_col2 = st.columns(2)
        
        with tech_col1:
            st.markdown("""
            **Color Detection Algorithm:**
            1. Extract RGB values from clicked pixel
            2. Calculate Manhattan distance with dataset colors
            3. Formula: `d = |R-r| + |G-g| + |B-b|`
            4. Find minimum distance (closest color)
            5. Return color name and hex code
            """)
        
        with tech_col2:
            st.markdown("""
            **Machine Learning Concepts:**
            - **K-NN (K=1):** Find nearest neighbor
            - **Distance Metric:** Manhattan distance
            - **K-Means Clustering:** Dominant colors
            - **Feature Extraction:** RGB color space
            - **Pattern Recognition:** Color matching
            """)
        
        # Dataset Information
        st.markdown("---")
        st.markdown("### 📊 Color Dataset")
        st.markdown(f"**Total Colors in Database:** {len(colors_df)}")
        
        with st.expander("🔍 View Sample Colors from Dataset"):
            st.dataframe(colors_df.head(20), use_container_width=True)

# ============================================================================
# RUN APPLICATION
# ============================================================================

if __name__ == "__main__":
    main()
